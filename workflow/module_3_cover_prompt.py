import json
import re

import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"


def extract_json(text):
    cleaned = text.strip()
    if cleaned.startswith("```json"):
        cleaned = cleaned[7:]
    if cleaned.startswith("```"):
        cleaned = cleaned[3:]
    if cleaned.endswith("```"):
        cleaned = cleaned[:-3]
    cleaned = cleaned.strip()

    if cleaned.startswith("{") and cleaned.endswith("}"):
        return cleaned

    match = re.search(r"\{.*\}", cleaned, flags=re.S)
    if match:
        return match.group(0)

    return cleaned


def generate_cover_prompt(title, excerpt, story_text, model="qwen2.5:7b"):
    prompt = f"""
你是「咖啡時光廊」的封面美術指導。

任務：根據故事內容，產生封面圖方向。現在不需要真的生圖，只要給搜尋詞與未來生圖 prompt。

要求：
- 不要商業廣告感。
- 不要卡通、不要動漫、不要誇張戲劇化。
- 要像紀實攝影、老照片、午後窗光、生活感、溫暖但克制。
- 避免直接描繪車禍、暴力、血腥、痛苦表情。
- 若故事是長者生命故事，重點放在時間感、手、老照片、窗光、舊物、安靜神情。

只輸出 JSON：
{{
  "cover_mood": "一句話描述封面氣質",
  "image_search_keywords": ["搜尋詞1", "搜尋詞2", "搜尋詞3"],
  "image_prompt_zh": "可直接貼到生圖工具的繁體中文提示詞，具體描述主體、光線、構圖、風格、情緒",
  "image_prompt_en": "英文備用提示詞",
  "avoid_words": ["不要出現的元素"]
}}

標題：{title}
摘要：{excerpt}
故事正文：
{story_text[:2500]}
"""
    try:
        print("正在產生封面圖策略...")
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0.35,
                    "num_ctx": 4096,
                    "num_predict": 900,
                },
            },
            timeout=300,
        )
        response.raise_for_status()
        text = response.json().get("response", "")
        return json.loads(extract_json(text))
    except Exception as e:
        print(f"⚠️ 封面圖策略產生失敗：{e}")
        return None


def write_cover_prompt(path, cover_data, image_path):
    if not cover_data:
        return

    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# 封面圖策略",
        "",
        f"目前實際圖片：{image_path}",
        "",
        "目前流程會優先找 Wikimedia Commons 相關圖片；找不到才使用 Picsum 隨機佔位圖。",
        "",
        "## 目前圖片來源",
        "",
        f"- source: {cover_data.get('image_source', {}).get('source', '')}",
        f"- title: {cover_data.get('image_source', {}).get('title', '')}",
        f"- url: {cover_data.get('image_source', {}).get('url', '')}",
        f"- page: {cover_data.get('image_source', {}).get('page', '')}",
        f"- license: {cover_data.get('image_source', {}).get('license', '')}",
        f"- query: {cover_data.get('image_source', {}).get('query', '')}",
        "",
        "## 封面氣質",
        "",
        cover_data.get("cover_mood", ""),
        "",
        "## 可搜尋關鍵字",
        "",
    ]
    lines.extend(f"- {keyword}" for keyword in cover_data.get("image_search_keywords", []))
    lines.extend(
        [
            "",
            "## 中文生圖 Prompt",
            "",
            cover_data.get("image_prompt_zh", ""),
            "",
            "## English Image Prompt（備用）",
            "",
            cover_data.get("image_prompt_en", ""),
            "",
            "## 避免元素",
            "",
        ]
    )
    lines.extend(f"- {word}" for word in cover_data.get("avoid_words", []))
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
