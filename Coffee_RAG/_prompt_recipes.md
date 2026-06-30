# Codex 指令食譜

這份檔案放常用指令。你可以直接複製其中一段給 Codex。

## 建立單篇文章

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：建立一篇 Markdown 文章
分類：06_沖煮
主題：粉水比
深度：草稿
完成後：更新 Coffee_RAG/_index.md
```

## 批次建立文章

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：批次建立文章
分類：02_產區
主題：衣索比亞、巴西、哥倫比亞、瓜地馬拉
深度：草稿
完成後：更新 Coffee_RAG/_index.md 與 Coffee_RAG/_queue.md
```

## 把貼上的內容整理進知識庫

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：把我貼上的內容整理成 RAG-ready Markdown
規則：判斷最適合的分類，必要時拆成多篇
完成後：更新 Coffee_RAG/_index.md

以下是內容：
[貼上你的筆記、逐字稿、訪談、文章]
```

## 從影片逐字稿建立 QA

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：從以下逐字稿整理 10 題 QA 與 10 題 FAQ
輸出位置：Coffee_RAG/11_QA 與 Coffee_RAG/12_FAQ
完成後：更新 Coffee_RAG/_index.md

逐字稿：
[貼上逐字稿]
```

## 登錄圖片素材

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：建立圖片素材 Markdown 登錄資料
分類：13_圖片
素材來源：[檔案路徑或 URL]
授權狀態：[自有 / 已授權 / 待確認]
完成後：更新 Coffee_RAG/_index.md
```

## 登錄影片素材

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：建立影片素材 Markdown 登錄資料
分類：14_影片
素材來源：[檔案路徑或 URL]
是否有逐字稿：[有 / 無]
完成後：更新 Coffee_RAG/_index.md
```

## 品質檢查

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：檢查 Coffee_RAG
範圍：frontmatter、內部連結、重複主題、待補來源
輸出：直接修正低風險問題，另列需要我確認的問題
```

## 準備 RAG 匯出前整理

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：把 Coffee_RAG 整理成 RAG-ready 狀態
範圍：只處理 status 為 review 的文章
要求：段落短、標題清楚、補同義詞 tags、檢查內部連結
完成後：列出仍缺來源的文章
```

## 登錄產品知識來源

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：登錄產品知識來源
來源 URL：[貼上產品頁、庫存頁或供應商頁]
輸出位置：Coffee_RAG/16_產品知識
要求：整理欄位、可用於 RAG 的規則、代表品項、後續任務
完成後：更新 Coffee_RAG/_index.md 與 Coffee_RAG/_queue.md
```

## 從產品來源建立銷售 QA

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：從 16_產品知識 建立產品諮詢 QA
範圍：[指定來源或品項]
輸出位置：Coffee_RAG/11_QA
要求：庫存、價格、供貨狀態必須標示需即時確認
完成後：更新 Coffee_RAG/_index.md
```

## 登錄外部知識來源

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：登錄外部知識來源
來源 URL：[貼上部落格、文章列表、報告或影片頁]
輸出位置：Coffee_RAG/00_來源資料
要求：整理可用欄位、文章或素材清單、建議拆分方向、使用限制
完成後：更新 Coffee_RAG/_index.md 與 Coffee_RAG/_queue.md
```

## 從外部來源拆成正式文章

```text
請依照 Coffee_RAG/AGENTS.md 執行：
任務：從 00_來源資料 的指定來源拆成正式知識文章
來源：[指定來源檔]
範圍：[指定文章或主題]
要求：逐篇讀取原文，用自己的結構重寫，不搬運全文，保留來源連結
完成後：更新 Coffee_RAG/_index.md
```
