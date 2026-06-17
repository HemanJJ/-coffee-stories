import os
import time
import asyncio
import json
import argparse
from pathlib import Path
from module_1_youtube import fetch_transcript
from module_2_story import generate_story
from module_2_dialogue import generate_dialogue
from module_3_cover_prompt import generate_cover_prompt, write_cover_prompt
from module_3_image import generate_image
from module_4_voice import generate_dialogue_voice, generate_voice_with_fallback

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


def input_multiline_text(prompt):
    print(prompt)
    print("貼上後另起一行輸入 END 結束。")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        marker = line.strip().upper()
        if marker == "END" or marker.startswith("END ") or line.strip() == "結束":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def parse_args():
    parser = argparse.ArgumentParser(description="Generate coffee story audio assets.")
    parser.add_argument(
        "--mode",
        choices=["single", "dialogue"],
        default="single",
        help="single = formal monologue story; dialogue = male/female preview conversation.",
    )
    return parser.parse_args()


async def main():
    args = parse_args()
    print("=========================================")
    print("☕ 咖啡時光廊 - 自動化生成工作流")
    print("=========================================")
    print(f"模式：{args.mode}")
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
            raw_text = input_multiline_text(
                "請貼上可用文字：影片描述、留言、你自己的筆記，或你看完後的摘要。"
            )
            if not raw_text:
                print("沒有文字來源，無法生成故事。")
                return
        print(f"✅ 文字來源準備完成，長度: {len(raw_text)} 字")
    else:
        raw_text = input_multiline_text("請貼上一段文字來寫故事。")
        if not raw_text:
            return

    if args.mode == "dialogue":
        print(f"\n[2/4] 正在請 Ollama/{story_model} 產生男女對話試聽稿...")
        dialogue_data = generate_dialogue(raw_text, story_model)
        if not dialogue_data:
            return

        timestamp = str(int(time.time()))
        dialogue_dir = REPO_ROOT / "assets" / "audio" / f"dialogue_{timestamp}"
        audio_paths = await generate_dialogue_voice(dialogue_data.get("turns", []), dialogue_dir)

        export_path = WORKFLOW_DIR / "dialogue_preview.json"
        export_data = {
            "title": dialogue_data.get("title", ""),
            "excerpt": dialogue_data.get("excerpt", ""),
            "turns": dialogue_data.get("turns", []),
            "audioFiles": [str(path) for path in audio_paths],
            "sourceUrl": url,
        }
        with export_path.open("w", encoding="utf-8") as f:
            json.dump(export_data, f, ensure_ascii=False, indent=4)

        print("\n=========================================")
        print(f"🎧 對話試聽完成：{export_path}")
        print(f"音檔資料夾：{dialogue_dir}")
        print("這是內部聽題材用，不是正式上架故事。")
        print("=========================================")
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

    # 3. 封面圖策略 + 佔位圖
    print("\n[3/5] 正在準備故事封面圖...")
    cover_data = generate_cover_prompt(title, excerpt, text, story_model)
    # 用 Pollinations.ai 替代 Imagen 3
    image_bytes = generate_image(title)
    if image_bytes:
        with image_path.open("wb") as f:
            f.write(image_bytes)
        print("✅ 封面佔位圖生成完畢")
    else:
        print("⚠️ 封面圖生成失敗，稍後請手動處理")
    write_cover_prompt(WORKFLOW_DIR / "cover_prompt.md", cover_data, image_path)
    if cover_data:
        print("✅ 封面圖策略已寫入 workflow/cover_prompt.md")

    # 4. 配音
    print("\n[4/5] 正在準備配音...")
    
    while True:
        try:
            voice_choice = input("請選擇說故事的聲音 (1: 溫暖女聲-曉臻, 2: 沉穩男聲-雲哲) [預設 1]: ").strip()
            if voice_choice in ["", "1"]:
                voice_type = "female"
                print("👉 已選擇：溫暖女聲")
                break
            elif voice_choice == "2":
                voice_type = "male"
                print("👉 已選擇：沉穩男聲")
                break
            else:
                print("❌ 無效的選擇，請輸入 1 或 2。")
        except EOFError:
            voice_type = "female"
            break
    
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
    
    # 執行配音。先寫暫存檔，成功才換成正式檔，避免留下 0 byte mp3。
    audio_ok, actual_voice_type, audio_error = await generate_voice_with_fallback(
        voice_text,
        str(audio_path),
        voice_type,
    )
    if audio_ok:
        if actual_voice_type != voice_type:
            print("⚠️ 男聲配音失敗，已自動改用女聲完成。")
        print("✅ 語音生成完畢")
    else:
        print(f"⚠️ 語音生成失敗，先保留文字與封面：{audio_error}")

    # 5. 上傳提示
    print("\n[5/5] 圖片與聲音已存入本機資料夾！")
    print("👉 請打開您熟悉的 GitHub Desktop，點擊 Commit 和 Push origin 來上傳檔案。")

    # 6. 輸出 CMS 填寫資料
    image_url = f"{GITHUB_PAGES_URL}/assets/images/{image_filename}"
    audio_url = f"{GITHUB_PAGES_URL}/assets/audio/{audio_filename}" if audio_ok else ""
    
    # 將資料存成 JSON，供 CMS 直接匯入
    story_export = {
        "title": title,
        "excerpt": excerpt,
        "mediaUrl": audio_url,
        "externalLink": url,
        "cover": image_url,
        "coverPrompt": cover_data or {},
        "text": text,
        "type": "audio",
        "category": "愛", # 預設分類
        "status": "published" if audio_ok else "draft"
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
