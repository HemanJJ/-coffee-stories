import json
import re
import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MAX_SOURCE_CHARS = 5000


def warn_if_too_promotional(text):
    coffee_terms = ["咖啡"]
    brand_terms = ["光碼創意", "LightCode", "品牌", "AI", "設計"]
    sales_terms = ["購買", "品嚐本品牌", "精心烘焙", "每一杯", "傳遞光", "媒介"]
    narration_noise_terms = ["【", "】", "#", "Hashtag", "FB/LINE", "包裝", "標題：", "摘要："]

    coffee_count = sum(text.count(term) for term in coffee_terms)
    brand_count = sum(text.count(term) for term in brand_terms)
    sales_hits = [term for term in sales_terms if term in text]
    narration_noise_hits = [term for term in narration_noise_terms if term in text]

    if coffee_count > 1 or brand_count > 1 or sales_hits or narration_noise_hits:
        print("⚠️ 這次輸出可能不適合直接朗讀，建議人工複查：")
        if coffee_count > 1:
            print(f"   - 咖啡出現 {coffee_count} 次")
        if brand_count > 1:
            print(f"   - 品牌/技術詞出現 {brand_count} 次")
        if sales_hits:
            print(f"   - 出現推銷感詞語：{', '.join(sales_hits)}")
        if narration_noise_hits:
            print(f"   - 出現朗讀雜訊：{', '.join(narration_noise_hits)}")


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

任務：把以下 YouTube 字幕整理成一篇真正像故事的散文短文。
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
11. text 是要直接交給語音朗讀的故事文本。它必須像散文、小篇短文、文藝作品。
12. text 裡禁止出現欄位標籤、章節標題、hashtags、項目符號、Markdown、包裝文案、FB/LINE 字樣。
13. text 裡不要寫「【故事】」「【故事裡的光】」「#咖啡時光廊」這類會被朗讀出來的雜訊。
14. 請嚴格輸出以下 JSON 格式，不要加任何 markdown 標記：
15. 【極度重要】在 JSON 的字串值中，絕對不可使用半形雙引號 `"`！若需引號請一律使用全形 `「` 和 `」`！
16. 【極度重要】所有換行都必須使用字串 `\\n`，絕對不可產生真實的換行符號！
{{
    "title": "動人的標題(不超過15個字)",
    "excerpt": "像故事卡片的摘要(約30字，不要廣告語)",
    "text": "約 700 字左右，可直接朗讀的散文故事正文。只寫正文，不要任何標籤、章節名、hashtags、包裝文案或行銷欄位。"
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
