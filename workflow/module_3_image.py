import requests


COMMONS_API_URL = "https://commons.wikimedia.org/w/api.php"
PICSUM_URL = "https://picsum.photos/1536/1920"
HEADERS = {
    "User-Agent": "coffee-stories/0.1 (local story cover research; https://hemanjj.github.io/-coffee-stories/)"
}


def search_commons_image(search_terms):
    for term in search_terms:
        query = str(term).strip()
        if not query:
            continue

        try:
            response = requests.get(
                COMMONS_API_URL,
                params={
                    "action": "query",
                    "format": "json",
                    "generator": "search",
                    "gsrnamespace": 6,
                    "gsrsearch": query,
                    "gsrlimit": 8,
                    "prop": "imageinfo",
                    "iiprop": "url|mime|extmetadata",
                },
                headers=HEADERS,
                timeout=20,
            )
            response.raise_for_status()
        except Exception as exc:
            print(f"⚠️ Wikimedia 搜圖失敗 ({query}): {exc}")
            continue

        pages = response.json().get("query", {}).get("pages", {})
        for page in pages.values():
            imageinfo = page.get("imageinfo", [])
            if not imageinfo:
                continue
            info = imageinfo[0]
            mime = info.get("mime", "")
            image_url = info.get("url", "")
            if mime not in {"image/jpeg", "image/png"} or not image_url:
                continue

            metadata = info.get("extmetadata", {})
            return {
                "url": image_url,
                "page": f"https://commons.wikimedia.org/wiki/{page.get('title', '').replace(' ', '_')}",
                "title": page.get("title", ""),
                "license": metadata.get("LicenseShortName", {}).get("value", ""),
                "artist": metadata.get("Artist", {}).get("value", ""),
                "source": "Wikimedia Commons",
                "query": query,
            }

    return None


def download_image(image_url):
    response = requests.get(image_url, allow_redirects=True, headers=HEADERS, timeout=30)
    response.raise_for_status()
    return response.content


def generate_image(prompt, search_terms=None):
    """
    Prefer a related, reusable Wikimedia Commons image. If none is found,
    fall back to a Picsum random placeholder so the story pipeline continues.
    """
    terms = list(search_terms or [])
    if prompt:
        terms.append(prompt)

    commons_match = search_commons_image(terms)
    if commons_match:
        try:
            print(f"✅ 找到相關 Wikimedia 圖片：{commons_match['title']}")
            return {
                "content": download_image(commons_match["url"]),
                "source": commons_match,
            }
        except Exception as exc:
            print(f"⚠️ Wikimedia 圖片下載失敗，改用 Picsum：{exc}")

    try:
        print("⚠️ 找不到合適 Wikimedia 圖片，改用 Picsum 隨機佔位圖。")
        return {
            "content": download_image(PICSUM_URL),
            "source": {
                "source": "Picsum placeholder",
                "url": PICSUM_URL,
                "title": "Random placeholder image",
                "license": "",
                "artist": "",
                "query": "",
            },
        }
    except Exception as exc:
        print(f"❌ 圖片取得失敗: {exc}")
        return None
