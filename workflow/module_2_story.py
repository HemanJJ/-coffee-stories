from google import genai
import json
import re

def generate_story(api_key, raw_text):
    client = genai.Client(api_key=api_key)
    prompt = f"""
你現在是「光碼創意 LightCode Creative」的福音咖啡品牌故事與包裝行銷顧問。

品牌核心：AI × 設計 × 福音 × 咖啡
品牌標語：用一杯咖啡，傳遞一道光。(Every Cup Carries Light.)

請將以下 YouTube 字幕內容，轉化成一篇有溫度、有信仰、適合配著咖啡閱讀的故事，並為我們的社群與包裝產出文案。

要求：
1. 語氣溫暖、真誠、有信仰感、接地氣。適合 50～70 歲的人也看得懂。
2. 結尾帶出一點盼望、平安或饒恕的福音意涵（不要強迫推銷信仰，用祝福、陪伴來表達）。
3. 請嚴格輸出以下 JSON 格式，不要加任何 markdown 標記：
{{
    "title": "動人的標題(不超過15個字)",
    "excerpt": "簡短的卡片摘要(約30字)",
    "text": "【品牌故事】\\n(約300-500字的故事內容)\\n\\n【包裝文案 - 正面】\\n(一句溫暖的短語)\\n\\n【包裝文案 - 背面祝福】\\n(一段祝福的話與適合的聖經經文)\\n\\n【FB/LINE 社群推播文字】\\n(開場吸引句 + 故事引導 + 呼籲行動)\\n\\n【Hashtag】\\n#光碼創意 #福音咖啡 ..."
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
        return data
    except Exception as e:
        print(f"❌ 故事生成失敗: {e}")
        return None
