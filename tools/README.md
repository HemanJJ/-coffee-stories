# YouTube 題材搜尋工具

## 最簡單入口

回到專案根目錄後，只記這個：

```bash
python3 menu.py
```

選 `1` 後，menu 會問你：

- 今天的 `hook`
- 只要可用影片？Yes/No
- 只要故事型，排除歌曲/MV/劇集/vlog？Yes/No
- 需要有字幕/文字可抓？Yes/No

例如想找「回家」：

```text
請選擇: 1
今天的 hook，例如 一封信 / 回家 / 阿嬤 [一封信]: 回家
只要可用影片？ [Y/n]:
只要故事型，排除歌曲/MV/劇集/vlog？ [Y/n]:
需要有字幕/文字可抓？ [Y/n]:
```

或直接指定 sub name：

```bash
python3 menu.py yt-find
```

目前 menu 裡有兩個 sub name：

- `yt-find`：找 YouTube 題材，產出 `youtube_topic_candidates.csv`
- `yt-find` 也會產出好找的短名 `shortlist.csv`
- `story-make`：用本機 Ollama/Qwen 把 YouTube 字幕或文字轉成咖啡故事，產出 `workflow/ai_stories.json`

這個工具是拿來幫你從 YouTube 找「比較像咖啡時光廊」的小人物故事題材。

它不是直接告訴你答案，
而是先幫你把雜訊濾掉一大半。

## 這工具會做什麼

- 用 YouTube Data API 搜尋影片
- 盡量排除政治、宗教、娛樂名人、遊戲、靈異、測驗雜訊
- 盡量排除歌曲、MV、歌詞、劇集片段、vlog
- 比較偏向：
  - 家庭
  - 告別
  - 陪伴
  - 回家
  - 小人物故事
- 產出一份完整候選名單
- 產出一份比較短的 shortlist
- 預設只保留公開、已處理、非直播、可嵌入的影片
- 從 menu 跑時，預設也只保留有字幕/文字可抓的影片

## 你要先準備什麼

1. 一把可用的 `YouTube Data API v3` key
2. Terminal 可以跑 `python3`

## 怎麼跑

在專案根目錄執行：

```bash
python3 tools/search_youtube_topics.py --api-key "你的API_KEY" --output youtube_topic_candidates.csv
```

比較推薦的做法是建立本機 `.env`，之後不用每次 `export`。

在專案根目錄建立 `.env`：

```bash
YOUTUBE_API_KEY="你的API_KEY"
```

然後直接跑：

```bash
python3 tools/search_youtube_topics.py --output youtube_topic_candidates.csv
```

## 每天換一個 hook

如果每天都跑同一批 query，結果很容易重複。

可以用 `--hook` 指定今天的入口：

```bash
python3 tools/search_youtube_topics.py --hook "一封信" --output youtube_topic_candidates.csv
```

也可以用 `--intent` 先縮小方向：

```bash
python3 tools/search_youtube_topics.py --intent object --hook "老照片" --sample-queries 5 --output youtube_topic_candidates.csv
```

常用 intent：
- `object`：家書、老照片、舊物、錄音
- `family`：父親、母親、外公、外婆
- `home`：回家、故鄉、離家
- `care`：陪伴、照顧者、陪病
- `restart`：重新開始、中年、人生下半場
- `dialect`：方言、台語、客語、潮汕話

`--sample-queries 5` 代表今天只抽 5 組 query 跑，省 quota，也比較不會每天都看到同一批結果。

用 `hook` 和 `sample` 時，結果會比較少，分數也可能比較低。這是正常的，因為它是在找更窄的題材，不是在撈最大眾的影片。

如果你只想臨時跑一次，也可以用環境變數：

```bash
export YOUTUBE_API_KEY="你的API_KEY"
python3 tools/search_youtube_topics.py --output youtube_topic_candidates.csv
```

`.env` 已經被 `.gitignore` 忽略，不會進 git。

## 跑完會出現什麼

### 1. `youtube_topic_candidates.csv`

完整候選名單。

常看欄位：
- `title`
- `channel`
- `availability`
- `transcript_status`
- `view_count`
- `comment_count`
- `score`
- `auto_suggestion`
- `url`
- `description`

### 2. `youtube_topic_shortlist.csv`

比較高分的短名單，適合先看。

如果你從 `menu.py` 跑 `yt-find`，也會另外產出一份同內容的短名：

```text
shortlist.csv
```

如果這輪沒有任何影片達到 shortlist 分數門檻，工具會把前 5 筆候選放進 `shortlist.csv` 當作「待人工看」清單。這代表它們不是好名單，只是避免檔案空白。

## 你現在最實用的看法

先不要一次看全部。

建議順序：

1. 先看 `youtube_topic_shortlist.csv`
2. 先跳過太有名的人
3. 先跳過太私人、太像家屬自製追思的片
4. 只挑 2 到 3 支最像的回來看

## 常見卡住

### `Quota exceeded`

代表同一個 Google Cloud project 的 YouTube 搜尋每日配額用完了。

不是程式壞掉，
也不是同 project 換一把 key 就會好。

### `API key expired` 或 `API_KEY_INVALID`

代表這把 key 本身不能用，要重建。

### 有結果，但很不像你要的

這通常不是 API 壞掉，
而是搜尋詞或篩選規則還要再調。

可改的地方：
- `tools/topic_queries.txt`
- `tools/search_youtube_topics.py`

### 好不容易找到，結果不能用

現在工具會先用 YouTube API 檢查影片狀態。

預設只留下：
- 公開影片
- 已處理完成
- 非直播 / 非預告直播
- 可嵌入影片

CSV 裡的 `availability` 會顯示 `usable`。

如果只是想研究題材，不管能不能嵌入，可以加：

```bash
python3 tools/search_youtube_topics.py --allow-unusable --output youtube_topic_candidates.csv
```

### 找到的是歌、MV、劇集片段

從 menu 跑時，這個開關請回答 `Y`：

```text
只要故事型，排除歌曲/MV/劇集/vlog？ [Y/n]:
```

如果直接下指令，可以加：

```bash
python3 tools/search_youtube_topics.py --story-only --output youtube_topic_candidates.csv
```

### 要給 agent 用，需要有文字

從 menu 跑時，這個開關請回答 `Y`：

```text
需要有字幕/文字可抓？ [Y/n]:
```

如果直接下指令，可以加：

```bash
python3 tools/search_youtube_topics.py --require-transcript --output youtube_topic_candidates.csv
```

CSV 裡的 `transcript_status` 會顯示這支是否有字幕/文字可抓。

## 這工具目前的定位

它不是最後判官。

它比較像第一層篩網：

先把 100 個亂結果，
縮成 20 到 40 個比較像樣的候選。

最後還是要靠你人工看 2 到 3 支，
再決定哪支真的對味。
