import json
import re

import requests


OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
MAX_SOURCE_CHARS = 5000


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
    return text[:MAX_SOURCE_CHARS] + "\n\n[文字過長，後段已省略，請根據前段材料整理對話。]"


def warn_if_simplified_chinese(data):
    simplified_markers = ["这", "个", "为", "后", "里", "听", "说", "过", "对", "会", "与", "岁", "时", "亲"]
    text_parts = [data.get("title", ""), data.get("excerpt", "")]
    text_parts.extend(turn.get("text", "") for turn in data.get("turns", []))
    joined = " ".join(text_parts)
    hits = sorted({char for char in simplified_markers if char in joined})
    if hits:
        print(f"⚠️ 對話稿可能混入簡體字，建議人工複查：{''.join(hits[:12])}")


def generate_dialogue(raw_text, model="qwen2.5:7b"):
    source_text = trim_source_text(raw_text)
    prompt = f"""
你現在是「咖啡時光廊」的音訊節目編輯。

任務：把以下素材改寫成男女雙人對話版，用來內部試聽題材，不是正式上架故事。

風格：
- 像 NotebookLM 的男女對話摘要，但更溫柔、安靜、少綜藝感。
- 男聲負責提問、承接、整理。
- 女聲負責說出故事細節、情緒、人物處境。
- 不要推銷品牌，不要講大道理，不要一直提咖啡。
- 不要 hashtags、欄位標籤、Markdown。
- 每段 1 到 3 句，適合 TTS 分段朗讀。
- 共 8 到 12 段。
- title、excerpt、turns 裡所有 text 一律使用繁體中文。不要輸出簡體中文、英文標題或中英混雜。
- 若原始素材是簡體中文，請自然轉寫為台灣讀者聽得懂的繁體中文。

只輸出 JSON，不要解釋：
{{
  "title": "不超過15字的標題",
  "excerpt": "約30字摘要",
  "turns": [
    {{"speaker": "male", "text": "男聲第一段"}},
    {{"speaker": "female", "text": "女聲第一段"}}
  ]
}}

原始素材：
{source_text}
"""
    try:
        print(f"使用本機 Ollama 模型產生對話：{model}")
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False,
                "format": "json",
                "options": {
                    "temperature": 0.45,
                    "num_ctx": 4096,
                    "num_predict": 1800,
                },
            },
            timeout=600,
        )
        response.raise_for_status()
        text = response.json().get("response", "")
        data = json.loads(extract_json(text))
        warn_if_simplified_chinese(data)
        return data
    except Exception as e:
        print(f"❌ Ollama 對話生成失敗: {e}")
        return None
