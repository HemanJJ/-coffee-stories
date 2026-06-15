import os
import time
import asyncio
import json
from pathlib import Path
from module_1_youtube import fetch_transcript
from module_2_story import generate_story
from module_3_image import generate_image
from module_4_voice import generate_voice

WORKFLOW_DIR = Path(__file__).resolve().parent
REPO_ROOT = WORKFLOW_DIR.parent
GITHUB_PAGES_URL = "https://hemanjj.github.io/-coffee-stories"


def read_env_file(path):
    values = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def get_ollama_model():
    env_file_model = read_env_file(REPO_ROOT / ".env").get("OLLAMA_MODEL", "").strip()
    if env_file_model:
        return env_file_model
    return os.environ.get("OLLAMA_MODEL", "qwen2.5:7b").strip()


async def main():
    print("=========================================")
    print("☕ 咖啡時光廊 - 自動化生成工作流")
    print("=========================================")
    story_model = get_ollama_model()

    try:
        url = input("請輸入 YouTube 網址 (或直接按 Enter 跳過測試純文本): ").strip()
    except EOFError:
        print("已取消。")
        return

    raw_text = ""
    if url:
        # 1. 抓取字幕
        print("\n[1/5] 正在抓取 YouTube 字幕...")
        raw_text = fetch_transcript(url)
        if not raw_text:
            print("無法抓取字幕，可能該影片沒有中英文字幕。")
            return
        print(f"✅ 成功抓取字幕，長度: {len(raw_text)} 字")
    else:
        try:
            raw_text = input("請輸入一段文字來寫故事: ").strip()
        except EOFError:
            print("已取消。")
            return
        if not raw_text:
            return

    # 2. 寫作
    print(f"\n[2/5] 正在請 Ollama/{story_model} 撰寫咖啡故事...")
    story_data = generate_story(raw_text, story_model)
    if not story_data:
        return
    
    title = story_data['title']
    excerpt = story_data['excerpt']
    text = story_data['text']
    print(f"✅ 標題: {title}")
    
    # 用時間戳記作為唯一檔名
    timestamp = str(int(time.time()))
    image_filename = f"story_{timestamp}.jpg"
    audio_filename = f"story_{timestamp}.mp3"
    
    image_path = REPO_ROOT / "assets" / "images" / image_filename
    audio_path = REPO_ROOT / "assets" / "audio" / audio_filename
    
    # 建立資料夾
    image_path.parent.mkdir(parents=True, exist_ok=True)
    audio_path.parent.mkdir(parents=True, exist_ok=True)

    # 3. 生圖
    print("\n[3/5] 正在生成 2K 故事封面圖...")
    # 用 Pollinations.ai 替代 Imagen 3
    image_bytes = generate_image(title)
    if image_bytes:
        with image_path.open("wb") as f:
            f.write(image_bytes)
        print("✅ 封面圖生成完畢")
    else:
        print("⚠️ 封面圖生成失敗，稍後請手動處理")

    # 4. 配音
    print("\n[4/5] 正在請曉臻朗讀故事...")
    
    # 清理要配音的文字：我們只希望語音唸出「真正的故事正文」，不該唸出分享文案或標籤！
    import re
    voice_text = text
    
    # 如果內容包含【故事裡的光】，則切斷，只保留前面的正文
    if "【故事裡的光】" in voice_text:
        voice_text = voice_text.split("【故事裡的光】")[0]
    elif "【包裝短句】" in voice_text:
        voice_text = voice_text.split("【包裝短句】")[0]
        
    # 清理殘留的標題，例如 【故事】
    voice_text = re.sub(r'【.*?】', '', voice_text)
    # 清理 Hashtag
    voice_text = re.sub(r'#\S+', '', voice_text)
    # 清理多餘空白行
    voice_text = '\n'.join([line for line in voice_text.splitlines() if line.strip()])
    
    # 預設使用女聲
    await generate_voice(voice_text, str(audio_path), "female")
    print("✅ 語音生成完畢")

    # 5. 上傳提示
    print("\n[5/5] 圖片與聲音已存入本機資料夾！")
    print("👉 請打開您熟悉的 GitHub Desktop，點擊 Commit 和 Push origin 來上傳檔案。")

    # 6. 輸出 CMS 填寫資料
    image_url = f"{GITHUB_PAGES_URL}/assets/images/{image_filename}"
    audio_url = f"{GITHUB_PAGES_URL}/assets/audio/{audio_filename}"
    
    # 將資料存成 JSON，供 CMS 直接匯入
    story_export = {
        "title": title,
        "excerpt": excerpt,
        "mediaUrl": audio_url,
        "externalLink": url,
        "cover": image_url,
        "text": text,
        "type": "audio",
        "category": "愛", # 預設分類
        "status": "published"
    }
    
    # 每次執行都「覆蓋」舊檔案，確保裡面永遠只有「最新產生的一次」的故事
    export_path = WORKFLOW_DIR / "ai_stories.json"
    stories_list = [story_export]
    
    with export_path.open("w", encoding="utf-8") as f:
        json.dump(stories_list, f, ensure_ascii=False, indent=4)
    
    print("\n=========================================")
    print(f"🎉 全部完成！已自動將本故事寫入【 {export_path} 】檔案中。")
    print("👉 請前往您的 Google CMS 後台，點擊【 📥 匯入 AI 生成故事 】按鈕，選擇這個 json 檔案即可一鍵匯入！")
    print("=========================================")

if __name__ == "__main__":
    asyncio.run(main())
