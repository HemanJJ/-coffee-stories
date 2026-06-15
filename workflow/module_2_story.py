from google import genai
import json
import re


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


def generate_story(api_key, raw_text):
    client = genai.Client(api_key=api_key)
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
{{
    "title": "動人的標題(不超過15個字)",
    "excerpt": "像故事卡片的摘要(約30字，不要廣告語)",
    "text": "【故事】\\n(約600-900字。沉浸式敘事，有人物、有場景、有轉折；不要置入行銷。)\\n\\n【故事裡的光】\\n(80-120字。只說這個故事留下的盼望或提醒，可自然對照一句短經文。)\\n\\n【包裝短句】\\n(一句像故事標籤的短語，不要推銷。)\\n\\n【背面祝福】\\n(一段安靜祝福，可附一節短聖經經文；不要講道。)\\n\\n【FB/LINE 分享文字】\\n(像朋友推薦一則故事，不像銷售文案；不要硬性呼籲購買。)\\n\\n【Hashtag】\\n#咖啡時光廊 #聽故事 #真實人生"
}}

原始字幕：
{raw_text}
"""
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
        )
        
        # 嘗試清理可能帶有 Markdown 的 JSON 格式字串
        text = response.text.strip()
        if text.startswith("```json"):
            text = text[7:]
        if text.startswith("```"):
            text = text[3:]
        if text.endswith("```"):
            text = text[:-3]
            
        data = json.loads(text.strip())
        warn_if_too_promotional(data.get("text", ""))
        return data
    except Exception as e:
        print(f"❌ 故事生成失敗: {e}")
        return None
