# YouTube 題材搜尋工具

這個工具是拿來幫你從 YouTube 找「比較像咖啡時光廊」的小人物故事題材。

它不是直接告訴你答案，
而是先幫你把雜訊濾掉一大半。

## 這工具會做什麼

- 用 YouTube Data API 搜尋影片
- 盡量排除政治、宗教、娛樂名人、遊戲、靈異、測驗雜訊
- 比較偏向：
  - 家庭
  - 告別
  - 陪伴
  - 回家
  - 小人物故事
- 產出一份完整候選名單
- 產出一份比較短的 shortlist

## 你要先準備什麼

1. 一把可用的 `YouTube Data API v3` key
2. Terminal 可以跑 `python3`

## 怎麼跑

在專案根目錄執行：

```bash
python3 tools/search_youtube_topics.py --api-key "你的API_KEY" --output youtube_topic_candidates.csv
```

如果你有先設環境變數，也可以：

```bash
export YOUTUBE_API_KEY="你的API_KEY"
python3 tools/search_youtube_topics.py --output youtube_topic_candidates.csv
```

## 跑完會出現什麼

### 1. `youtube_topic_candidates.csv`

完整候選名單。

常看欄位：
- `title`
- `channel`
- `view_count`
- `comment_count`
- `score`
- `auto_suggestion`
- `url`
- `description`

### 2. `youtube_topic_shortlist.csv`

比較高分的短名單，適合先看。

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

## 這工具目前的定位

它不是最後判官。

它比較像第一層篩網：

先把 100 個亂結果，
縮成 20 到 40 個比較像樣的候選。

最後還是要靠你人工看 2 到 3 支，
再決定哪支真的對味。
