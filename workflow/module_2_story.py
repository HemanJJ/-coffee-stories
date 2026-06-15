import json
import re
import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MAX_SOURCE_CHARS = 5000


def warn_if_too_promotional(text):
    coffee_terms = ["咖啡"]
    brand_terms = ["光碼創意", "LightCode", "品牌", "AI", "設計"]
    sales_terms = ["購買", "品嚐本品牌", "精心烘焙", "每一杯", "傳遞光", "媒介"]

    coffee_count = sum(text.count(term) for term in coffee_terms)
    brand_count = sum(text.count(term) for term in brand_terms)
    sales_hits = [term for term in sales_terms if term in text]

    if coffee_count > 1 or brand_count > 1 or sales_hits:
        print("⚠️ 這次輸出可能仍偏行銷，建議人工複查：")
        if coffee_count > 1:
            print(f"   - 咖啡出現 {coffee_count} 次")
        if brand_count > 1:
            print(f"   - 品牌/技術詞出現 {brand_count} 次")
        if sales_hits:
            print(f"   - 出現推銷感詞語：{', '.join(sales_hits)}")


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


def trim_source_text(raw_text):
    text = (raw_text or "").strip()
    if len(text) <= MAX_SOURCE_CHARS:
        return text
    return text[:MAX_SOURCE_CHARS] + "\n\n[字幕過長，後段已省略，請根據前段材料整理故事。]"


def generate_story(raw_text, model="qwen2.5:7b"):
    source_text = trim_source_text(raw_text)
    prompt = f"""
你現在是「咖啡時光廊」的沉浸式故事編輯，不是品牌行銷顧問。

任務：把以下 YouTube 字幕整理成一篇真正像故事的作品。
重點是人、處境、選擇、失去、等待、和解、盼望；不是推銷品牌，也不是推銷咖啡。

寫作規則：
1. 先讓讀者進入場景，再慢慢看見人物的心，不要一開始就講大道理。
2. 全文以故事為主，不要一直提「咖啡」、「品牌」、「光碼創意」、「AI」、「設計」。
3. 「咖啡」最多只能出現 1 次，而且只能像閱讀情境一樣自然出現，不能當商品。
4. 「品牌」或「光碼創意」最多只能出現 1 次，只能放在社群文案或 hashtag，不要放進主故事。
5. 不要使用推銷句，例如：購買、品嚐本品牌、為你準備、每一杯、精心烘焙、媒介、傳遞光。
6. 不要一直傳福音。信仰只能像一盞小燈，在結尾或祝福中輕輕對照。
7. 若引用經文，只用聖經，不用國學、成語式勸世或心靈雞湯。
8. 經文要短，像句點，不要講道；可用「詩篇23篇」「馬太福音11:28」「約翰福音14:27」「傳道書3:11」這類方向。
9. 適合 50～70 歲的人讀，文字要清楚、克制、真誠，不煽情。
10. 不要捏造字幕中沒有的重大情節；可以重組敘事，但要忠於原始材料。
11. 請嚴格輸出以下 JSON 格式，不要加任何 markdown 標記：
12. 【極度重要】在 JSON 的字串值中，絕對不可使用半形雙引號 `"`！若需引號請一律使用全形 `「` 和 `」`！
13. 【極度重要】所有換行都必須使用字串 `\\n`，絕對不可產生真實的換行符號！
{{
    "title": "動人的標題(不超過15個字)",
    "excerpt": "像故事卡片的摘要(約30字，不要廣告語)",
    "text": "【故事】\\n(約 500 字左右。沉浸式敘事，有人物、有場景、有轉折；不要置入行銷。)\\n\\n【故事裡的光】\\n(80-120字。只說這個故事留下的盼望或提醒，可自然對照一句短經文。)\\n\\n【包裝短句】\\n(一句像故事標籤的短語，不要推銷。)\\n\\n【背面祝福】\\n(一段安靜祝福，可附一節短聖經經文；不要講道。)\\n\\n【FB/LINE 分享文字】\\n(像朋友推薦一則故事，不像銷售文案；不要硬性呼籲購買。)\\n\\n【Hashtag】\\n#咖啡時光廊 #聽故事 #真實人生"
}}

原始字幕：
{source_text}
"""
    try:
        print(f"使用本機 Ollama 模型：{model}")
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
                    "num_predict": 1800,
                },
            },
            timeout=600,
        )
        response.raise_for_status()
        
        text = response.json().get("response", "")
        try:
            data = json.loads(extract_json(text))
        except json.JSONDecodeError as e:
            print(f"❌ JSON 解析失敗: {e}")
            print(f"--- 原始 Ollama 輸出 ---\n{text}\n----------------")
            return None
            
        warn_if_too_promotional(data.get("text", ""))
        return data
    except Exception as e:
        print(f"❌ Ollama 故事生成失敗: {e}")
        print("請確認 Ollama 已啟動，且模型已安裝，例如：ollama pull qwen2.5:7b")
        return None
