# Coffee Knowledge Base

這是一個全 Markdown 的咖啡知識庫，設計給人閱讀，也方便日後轉成 RAG 語料。

## 怎麼讓 Codex 自動執行

最簡單的格式：

```text
請依照 Coffee_RAG/AGENTS.md 執行：
[你的任務]
```

建議加上三個條件，會更穩：

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：建立 06_沖煮 的手沖基礎文章
範圍：研磨、水溫、粉水比、注水
深度：草稿
完成後：更新 _index.md 與 _queue.md
```

## 常用任務指令

```text
請依照 Coffee_RAG/AGENTS.md 執行：
建立 Coffee_RAG 的下一批優先文章，每個分類先 3 篇草稿。
```

```text
請依照 Coffee_RAG/AGENTS.md 執行：
把我貼上的內容整理成 RAG-ready Markdown，放到正確分類，並更新索引。
```

```text
請依照 Coffee_RAG/AGENTS.md 執行：
檢查 Coffee_RAG 的 frontmatter、內部連結、重複主題，列出修正建議。
```

```text
請依照 Coffee_RAG/AGENTS.md 執行：
根據 11_QA 與 12_FAQ，整理一份客服問答集。
```

## 結構

- `_index.md`: 全知識庫索引。
- `_queue.md`: 建議工作清單。
- `_taxonomy.md`: 分類、標籤、主題邊界。
- `_style_guide.md`: Markdown 寫作規範。
- `_source_policy.md`: 來源與查證規則。
- `_templates/`: 新增內容時使用的模板。
- `00_來源資料/`: 外部來源登錄與拆分規劃。
- `01_咖啡歷史/` 到 `16_產品知識/`: 知識庫主要內容。

## 工作節奏

建議分三階段：

1. 建骨架：分類、模板、索引、待辦。
2. 建草稿：每個分類先建立核心主題。
3. 精修成 RAG-ready：補來源、拆細主題、建立內部連結。

## 目前狀態

目前已完成知識庫骨架，並登錄產品知識來源與外部部落格來源。下一步可從 `_queue.md` 的 Batch 1、Batch 4 或 Batch 5 開始。
