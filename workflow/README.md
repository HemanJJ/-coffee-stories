# Python 咖啡故事生成流程

## 最簡單入口

回到專案根目錄後，只記這個：

```bash
python3 menu.py
```

或直接指定 sub name：

```bash
python3 menu.py story-make-single
```

目前 menu 裡有三個主要 sub name：

- `yt-find`：找 YouTube 題材，產出 `youtube_topic_candidates.csv`
- `story-make-single`：單口說故事，正式上架用，產出 `workflow/ai_stories.json`
- `story-make-dialogue`：男女對話試聽，像 NotebookLM，用來內部聽題材，產出 `workflow/dialogue_preview.json`

這個流程會把一支 YouTube 影片字幕，或一段你自己貼上的文字，交給本機 Ollama/Qwen 7B 轉成：

- 咖啡故事文案
- 封面圖片
- 語音 MP3
- `workflow/ai_stories.json`

最後的 `ai_stories.json` 可以拿去 CMS 匯入。

## 第一次設定

先進專案根目錄：

```bash
cd "/Users/hohe/Documents/GitHub/ coffee-stories"
```

如果還沒有虛擬環境：

```bash
python3 -m venv workflow/venv
```

啟用虛擬環境：

```bash
source workflow/venv/bin/activate
```

安裝套件：

```bash
pip install -r workflow/requirements.txt
```

先確認 Ollama 已啟動，並且有 Qwen 7B 模型：

```bash
ollama pull qwen2.5:7b
```

在專案根目錄的 `.env` 裡設定本機模型：

```bash
OLLAMA_MODEL="qwen2.5:7b"
```

如果同一個 `.env` 已經有 YouTube key，可以長這樣：

```bash
YOUTUBE_API_KEY="你的YouTube API key"
OLLAMA_MODEL="qwen2.5:7b"
```

`.env` 已經被 `.gitignore` 忽略，不會進 git。故事生成現在不需要 Gemini API key。

## 平常怎麼跑

每次開新 Terminal，先進專案並啟用環境：

```bash
cd "/Users/hohe/Documents/GitHub/ coffee-stories"
source workflow/venv/bin/activate
```

執行主流程：

```bash
python3 workflow/main.py --mode single
```

如果要產生男女對話試聽：

```bash
python3 workflow/main.py --mode dialogue
```

程式會問你：

```text
請輸入 YouTube 網址 (或直接按 Enter 跳過測試純文本):
```

你可以貼 YouTube 網址。

如果影片沒有字幕，程式會請你貼上替代文字，例如影片描述、留言、你自己的筆記，或你看完後的摘要。

貼完後另起一行輸入：

```text
END
```

程式就會繼續生成故事。

## 跑完會產出什麼

圖片：

```text
assets/images/story_時間戳.jpg
```

語音：

```text
assets/audio/story_時間戳.mp3
```

CMS 匯入檔：

```text
workflow/ai_stories.json
```

男女對話試聽檔：

```text
workflow/dialogue_preview.json
assets/audio/dialogue_時間戳/
```

## 常見問題

### Ollama 連不上

請先確認 Ollama app 或背景服務已啟動。

可以先測：

```bash
ollama list
workflow/venv/bin/python workflow/test_ollama.py
```

### 找不到模型

如果看到找不到 `qwen2.5:7b`，請先安裝：

```bash
ollama pull qwen2.5:7b
```

如果你本機模型名稱不同，改 `.env`：

```bash
OLLAMA_MODEL="你的模型名稱"
```

### 無法抓取字幕

代表該 YouTube 影片沒有可用字幕，或字幕語言不支援。

現在不會直接中斷。你可以貼：

- 影片描述
- 觀眾留言
- 你自己的觀看筆記
- 影片大意摘要

貼完輸入 `END`，仍然可以生成故事。

### 圖片很隨機

目前封面圖是用 Picsum 佔位圖，不是正式生圖。

未來可以再接回真正的生圖服務。
