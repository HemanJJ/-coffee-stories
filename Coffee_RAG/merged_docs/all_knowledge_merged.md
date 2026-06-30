# Coffee RAG 合併知識庫

此檔案由自動化腳本生成，合併了所有主題資料夾內之 Markdown 知識文件。



---
### 📄 來源檔案：`00_來源資料/README.md`
---

---
title: 來源資料
category: 00_來源資料
type: index
tags: [source]
status: draft
updated: 2026-06-30
sources: []
---

# 來源資料

## 範圍

登錄外部網站、部落格、報告、型錄、影片逐字稿、訪談與其他待整理來源。

## 優先主題

- `001_cometrue_coffee_部落格來源.md`

## 收錄原則

- 來源資料只登錄 metadata、摘要與拆分方向。
- 不把外部文章全文搬進知識庫。
- 若要轉成正式文章，需放到最合適的分類並保留來源連結。
- 涉及趨勢、價格、法規、品牌現況時，使用前需重新查證。



---
### 📄 來源檔案：`00_來源資料/001_cometrue_coffee_部落格來源.md`
---

---
title: 成真咖啡部落格來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, trend, brewing, equipment, sensory, cafe-operation, needs-review]
status: review
updated: 2026-06-30
source_url: https://www.cometrue-coffee.com/blog
accessed: 2026-06-30
sources:
  - type: web
    title: 部落格
    url: https://www.cometrue-coffee.com/blog
    accessed: 2026-06-30
---

# 成真咖啡部落格來源

## 摘要

這個來源是成真咖啡的部落格總覽頁。頁面可作為咖啡趨勢、沖煮變因、義式吧台、感官、設備、飲品趨勢與咖啡店營運題材的外部參考。

本知識庫於 `2026-06-30` 讀取頁面。來源頁由 Strikingly 產生，頁面內可解析到 `blogPosts` 資料結構。

這份檔案只登錄來源與拆分方向，不搬運文章全文。若後續要建立正式知識文章，需逐篇讀取原文、重寫成 Coffee_RAG 格式，並保留來源連結。

## 可用資料

來源頁可解析出的資料欄位包含：

- `title`：文章標題。
- `publicUrl`：文章 URL。
- `publishedAt`：發布時間。
- `updatedAt`：更新時間。
- `allTagsList`：站內標籤。
- `longBlurb`：文章摘要或前導文字。

本次讀取到 20 筆已發布文章 metadata。

## 文章或素材清單

以下是本次解析到的文章 metadata。時間以來源資料中的 `publishedAt` 為準。

| publishedAt | tags | title | url |
| --- | --- | --- | --- |
| 2026-06-24T16:00:03.049-07:00 | 品味生活 | 從感官到數據，用 AI 繪製一張咖啡的風味地圖 | https://www.cometrue-coffee.com/blog/ai |
| 2026-06-18T16:00:34.654-07:00 | 品味生活 | 抹茶之後的紫色風潮 你有聽過「紫山藥」嗎？ | https://www.cometrue-coffee.com/blog/491be319cd6 |
| 2026-06-12T16:00:46.280-07:00 | 生活實用 | 抹茶搶咖啡地盤？ | https://www.cometrue-coffee.com/blog/f1005b94933 |
| 2026-05-31T16:00:01.532-07:00 | 手沖玩家 | 濾紙品牌 Sibarist，又想重新定義手沖咖啡了？ | https://www.cometrue-coffee.com/blog/sibarist |
| 2026-05-26T20:23:53.082-07:00 | 生活實用 | 自動壓粉器進化中：咖啡吧台，正悄悄進入「無線時代」 | https://www.cometrue-coffee.com/blog/f049a50024f |
| 2026-05-12T03:00:19.973-07:00 | 生活實用 | 除了濃縮咖啡馬丁尼之外：咖啡店還能提供哪些雞尾酒？ | https://www.cometrue-coffee.com/blog/977284c7607 |
| 2026-04-30T16:00:25.980-07:00 | 品味生活 | 當咖啡遇上潮流設計：為什麼現在的品牌都在瘋「聯名」？ | https://www.cometrue-coffee.com/blog/4d12e5dae3b |
| 2026-04-24T16:00:01.197-07:00 |  | 流量對濃縮咖啡萃取的重要性 | https://www.cometrue-coffee.com/blog/f791c644bf0 |
| 2026-04-19T20:38:13.382-07:00 |  | 一眼看懂咖啡熟度！破解咖啡色澤密碼 | https://www.cometrue-coffee.com/blog/c88783add39 |
| 2026-04-08T16:00:04.333-07:00 | 品味生活 | 咖啡裡的甜從哪裡來？ | https://www.cometrue-coffee.com/blog/a590b583554 |
| 2026-03-31T16:00:31.728-07:00 | 生活實用 | 「斑蘭Pandan」可能成為下一個咖啡風味趨勢？ | https://www.cometrue-coffee.com/blog/pandan |
| 2026-03-26T16:00:04.198-07:00 | 職人專區 | 如何讓義式咖啡的研磨更穩定？ | https://www.cometrue-coffee.com/blog/61b9bdb1ecc |
| 2026-03-22T23:35:48.104-07:00 | 生活實用 | 為什麼水，是影響咖啡風味的主要關鍵？ | https://www.cometrue-coffee.com/blog/633013842b7 |
| 2026-02-09T15:00:11.007-08:00 | 手沖玩家 | 咖啡濾紙的演變 | https://www.cometrue-coffee.com/blog/081b1c5075e |
| 2026-01-09T15:00:01.881-08:00 | 生活實用 | 咖啡價格一直上漲，接下來會發生什麼事呢? | https://www.cometrue-coffee.com/blog/39f4958bb42 |
| 2025-12-15T19:32:39.182-08:00 | 職人專區 | 新興厭氧發酵處理法改寫了咖啡風味輪？ | https://www.cometrue-coffee.com/blog/1674a52e4d1 |
| 2025-11-30T15:00:24.372-08:00 | 生活實用 | 沙烏地阿拉伯的精品咖啡熱潮 一杯咖啡，喚醒整個王國！ | https://www.cometrue-coffee.com/blog/30dae1fbe59 |
| 2025-11-03T15:00:05.812-08:00 | 生活實用 | 咖啡瑕疵豆是什麼味道？ 沖一壺試試 | https://www.cometrue-coffee.com/blog/b20187de466 |
| 2025-10-30T01:43:36.267-07:00 | 品味生活 | 永續包裝，讓咖啡產業邁向循環經濟 | https://www.cometrue-coffee.com/blog/7f88ed20f80 |
| 2025-10-15T23:10:45.156-07:00 | 職人專區 | 好咖啡不只靠技術，乾淨的設備才是真正的神隊友！ | https://www.cometrue-coffee.com/blog/3dcbab75ab5 |

## 建議拆分方向

- `06_沖煮/`：水質、義式流量、研磨穩定、濾紙、手沖萃取。
- `07_設備/`：自動壓粉器、濾紙品牌、設備清潔。
- `08_感官/`：AI 風味地圖、咖啡甜感、瑕疵豆風味。
- `04_處理法/`：新興厭氧發酵處理法。
- `09_開店/`：咖啡店飲品趨勢、雞尾酒、抹茶與 Ube 等非咖啡飲品需求。
- `10_創業/`：聯名、品牌趨勢、價格上漲、永續包裝。
- `02_產區/`：沙烏地阿拉伯精品咖啡市場與產區題材。

## 使用限制

- 此檔案只作為來源索引，不作為正式知識文章。
- 涉及 2026 年趨勢、價格、品牌、市場預測的內容，回答或發布前需重新查證。
- 若要引用文章重點，應先打開單篇文章讀取完整上下文。
- 不要直接複製部落格全文；需整理為 Coffee_RAG 的文章格式並保留來源。

## 來源

- [成真咖啡部落格](https://www.cometrue-coffee.com/blog)，讀取日期：2026-06-30。



---
### 📄 來源檔案：`00_來源資料/002_idrip_官網來源.md`
---

---
title: iDrip 官網來源
category: 00_來源資料
type: source_catalog
tags: [source, product, equipment, brewing, app, ecommerce, needs-review]
status: review
updated: 2026-06-30
source_url: https://www.idrip.coffee/
accessed: 2026-06-30
sources:
  - type: web
    title: iDrip | 全世界第一台還原世界冠軍的智能手沖咖啡機
    url: https://www.idrip.coffee/
    accessed: 2026-06-30
---

# iDrip 官網來源

## 摘要

這個來源是 iDrip 官網首頁，可作為智能手沖咖啡機、咖啡市集、咖啡包與咖啡豆、手沖教學、咖啡知識、FAQ、App 與商務方案的外部參考。

首頁 title 為「iDrip | 全世界第一台還原世界冠軍的智能手沖咖啡機」。頁面 description 說明 iDrip 咖啡機結合世界咖啡冠軍、物聯網技術與精品工藝，主打能輕鬆享用冠軍精品手沖咖啡。

本知識庫於 `2026-06-30` 讀取首頁。商品、價格、庫存、方案與活動 banner 都屬於會變動的資訊，回答或發布前需回源查證。

## 可用資料

來源頁可用資訊包含：

- 品牌定位：智能手沖咖啡機、世界咖啡冠軍手法、物聯網、精品咖啡。
- 產品入口：咖啡機、加值方案、咖啡市集、品牌旗艦店、咖啡包/豆、周邊商品。
- 知識入口：咖啡包特色、手沖教學、咖啡尋味、咖啡地圖、咖啡知識部落格。
- 支援入口：操作影片、使用教學、常見問題、聯絡我們。
- 商務入口：商務方案、App 下載、合作店家、會員條款、隱私權保護政策。
- 首頁推薦品項：商品名稱、品牌、類型、價格、產地、烘焙度、處理法、風味與庫存資料。

## 文章或素材清單

### 主要入口

| 類型 | 名稱 | URL |
| --- | --- | --- |
| 產品 | 購買咖啡機 | https://www.idrip.coffee/machine |
| 產品 | 加值方案 | https://www.idrip.coffee/plan |
| 產品 | 咖啡市集 | https://www.idrip.coffee/coffee |
| 產品 | 品牌旗艦店 | https://www.idrip.coffee/store |
| 產品 | 周邊商品 | https://www.idrip.coffee/product |
| 產品 | 手法市集 | https://www.idrip.coffee/recipe |
| 活動 | 冷萃咖啡 | https://www.idrip.coffee/event/coldbrew |
| 活動 | 西西里咖啡 | https://www.idrip.coffee/event/sicily |
| 教學 | 咖啡包特色 | https://www.idrip.coffee/coffee/intro |
| 教學 | 手沖教學 | https://www.idrip.coffee/coffee/pourover |
| 互動 | 咖啡尋味 | https://www.idrip.coffee/coffee/questionnaire |
| 互動 | 咖啡地圖 | https://www.idrip.coffee/coffee/map |
| 知識 | 咖啡知識 | https://blog.idrip.coffee |
| 品牌 | 最新消息 | https://www.idrip.coffee/news |
| 品牌 | 品牌故事 | https://www.idrip.coffee/brand |
| 支援 | 操作影片 | https://www.idrip.coffee/tutorials/videos |
| 支援 | 使用教學 | https://www.idrip.coffee/tutorials/ |
| 支援 | 常見問題 | https://www.idrip.coffee/faq |
| 商務 | 商務方案 | https://www.idrip.coffee/enterprise |
| App | App 下載 | https://www.idrip.coffee/download |
| 商務 | 合作店家 | https://www.idrip.coffee/cooperation |

### 首頁推薦品項樣例

以下只作為來源結構樣例，不代表完整商品清單，也不代表目前價格、庫存或供貨狀態。

| 類型 | 品牌 | 品名 | 來源欄位觀察 |
| --- | --- | --- | --- |
| 咖啡豆 | 龍火咖啡 | 龍火咖啡 花園太妃糖 | 首頁資料包含價格、優惠價、庫存、產地、烘焙度、處理法、風味。 |
| 咖啡豆 | 拾穗咖啡 | 拾穗咖啡 哥倫比亞 美德琳 | 首頁資料包含價格、產地、區域、烘焙度、處理法、風味。 |
| 咖啡包 | 拾穗咖啡 | 拾穗咖啡 獨家特調 濃情蜜蜜 濾掛式咖啡 | 首頁資料包含每包價格、包裝入數、產地、處理法、風味。 |

## 建議拆分方向

- `16_產品知識/`：iDrip 智能手沖咖啡機、咖啡市集、咖啡包/豆、加值方案、App、商務方案。
- `07_設備/`：智能手沖咖啡機、操作影片、使用教學、常見問題。
- `06_沖煮/`：手沖教學、咖啡包特色、手法市集。
- `08_感官/`：咖啡尋味、咖啡地圖、風味描述欄位。
- `09_開店/`：商用精品咖啡方案、合作店家、商務應用情境。
- `11_QA/` 與 `12_FAQ/`：咖啡機使用、濾掛包使用、加值方案、商品選購、App 使用。

## 使用限制

- 此檔案只作為來源索引，不作為正式產品頁。
- 商品價格、優惠價、庫存、加值方案、活動 banner 與合作資訊會變動，使用前需重新查證。
- 首頁宣稱與產品規格應以官方產品頁或人工確認為準。
- 若要建立正式產品知識文章，需逐頁讀取對應 URL，保留來源連結，不只依首頁摘要撰寫。

## 來源

- [iDrip 官網](https://www.idrip.coffee/)，讀取日期：2026-06-30。



---
### 📄 來源檔案：`00_來源資料/003_first_cafe_手沖小學堂來源.md`
---

---
title: First Cafe 手沖小學堂來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, brewing, hand-pour, beginner, equipment, sensory, needs-review]
status: review
updated: 2026-06-30
source_url: https://first-cafe.com/category/hand-punching-primary-school/
accessed: 2026-06-30
sources:
  - type: web
    title: 手沖小學堂 - 咖啡知識家
    url: https://first-cafe.com/category/hand-punching-primary-school/
    accessed: 2026-06-30
  - type: web
    title: WordPress posts API for category 16
    url: https://first-cafe.com/wp-json/wp/v2/posts?categories=16
    accessed: 2026-06-30
---

# First Cafe 手沖小學堂來源

## 摘要

這個來源是 First Cafe 咖啡知識家的「手沖小學堂」分類頁。內容集中在手沖咖啡入門、沖煮變因、器具、粉水比、水質、悶蒸、注水方式、藝伎咖啡沖煮、風味搭配與常見錯誤。

本知識庫於 `2026-06-30` 讀取分類頁與 WordPress API。分類頁 title 為「手沖小學堂 - 咖啡知識家」。

WordPress API 顯示此分類目前共有 135 篇文章、2 頁。這份檔案只登錄來源與拆分方向，不搬運文章全文。

## 可用資料

來源頁與 API 可用資訊包含：

- 分類名稱：手沖小學堂。
- 分類 URL：`https://first-cafe.com/category/hand-punching-primary-school/`。
- API category id：`16`。
- 文章 metadata：發布日期、修改日期、文章 URL、標題、摘要、分類、標籤 id。
- 分頁資訊：`X-WP-Total: 135`、`X-WP-TotalPages: 2`。
- 分類頁第一頁顯示下一頁：`https://first-cafe.com/category/hand-punching-primary-school/page/2/`。

## 文章或素材清單

以下是依 API 讀取的前 20 筆代表文章。為避免大量搬運來源文字，`主題摘要` 使用本知識庫自行整理的短描述，不照抄原文標題。

| date | 主題摘要 | url |
| --- | --- | --- |
| 2025-07-20 | 沖泡方法如何影響咖啡風味，涵蓋手沖與義式差異 | https://first-cafe.com/coffee-brewing-method-8/ |
| 2025-06-30 | 手沖咖啡的生活感、儀式感與吸引力 | https://first-cafe.com/hand-brewed-coffee-14/ |
| 2025-06-20 | 新手從零開始學手沖咖啡 | https://first-cafe.com/hand-brewed-coffee-13/ |
| 2025-06-10 | 手沖咖啡必備器具與基礎流程 | https://first-cafe.com/hand-brewed-coffee-12/ |
| 2025-05-13 | 咖啡新手常見沖泡法入門 | https://first-cafe.com/coffee-brewing-method-6/ |
| 2025-04-30 | 新手挑豆與手沖起步方式 | https://first-cafe.com/hand-brewed-coffee-11/ |
| 2025-04-28 | 咖啡新手基礎常識總覽 | https://first-cafe.com/coffee-knowledge-4/ |
| 2025-03-25 | 新手如何選擇不酸的手沖咖啡豆 | https://first-cafe.com/hand-brewed-coffee-10/ |
| 2025-03-20 | 用手沖技巧凸顯果香與花香 | https://first-cafe.com/hand-brewed-coffee-9/ |
| 2025-03-10 | 水質對手沖咖啡風味的影響 | https://first-cafe.com/hand-brewed-coffee-water-quality/ |
| 2025-03-05 | 藝伎咖啡的手沖水溫、研磨與注水 | https://first-cafe.com/geisha-coffee-4/ |
| 2025-02-27 | 手沖咖啡與起司、堅果、果乾搭配 | https://first-cafe.com/hand-brewed-coffee-8/ |
| 2025-02-25 | 繞圈注水與直接注水比較 | https://first-cafe.com/hand-brewed-coffee-7/ |
| 2025-02-20 | 新手常見手沖錯誤與苦酸問題 | https://first-cafe.com/hand-brewed-coffee-6/ |
| 2025-02-17 | 手沖咖啡中的茶感、產地、處理法與烘焙關係 | https://first-cafe.com/hand-brewed-coffee-5/ |
| 2025-02-10 | 咖啡悶蒸原理與沖煮技巧 | https://first-cafe.com/coffee-blooming/ |
| 2025-01-30 | 義式咖啡與手沖咖啡差異 | https://first-cafe.com/hand-brewed-coffee-4/ |
| 2025-01-26 | 新手手沖咖啡必知事項 | https://first-cafe.com/hand-brewed-coffee-knowledge/ |
| 2025-01-15 | 手沖咖啡與點心搭配 | https://first-cafe.com/hand-brewed-coffee-3/ |
| 2024-12-25 | 手沖、冷萃等沖泡法與風味選擇 | https://first-cafe.com/coffee-brewing-method-3/ |

## 建議拆分方向

- `06_沖煮/`：手沖入門、粉水比、水溫、水質、悶蒸、注水方式、萃取率、沖泡法比較。
- `07_設備/`：濾杯、V60、愛樂壓、磨豆機、手沖壺、濾掛包與器具選擇。
- `08_感官/`：茶感、甜感、果香、花香、苦酸調整、食物搭配。
- `03_品種/`：藝伎、古吉與適合手沖的品種或產地題材。
- `04_處理法/`：處理法如何影響手沖風味。
- `11_QA/`：新手手沖問題、太苦太酸、水質、粉水比、器具選擇。
- `12_FAQ/`：短答型手沖常見問題。

## 使用限制

- 此檔案只作為來源索引，不作為正式知識文章。
- 此分類文章數量多，正式拆文時應逐篇讀取原文，不只依分類頁摘要撰寫。
- 文章中若涉及特定建議數值、器具、產品或市場資訊，需回源查證並標示查詢日期。
- 不要直接複製文章全文；需整理為 Coffee_RAG 的文章格式並保留來源。

## 來源

- [First Cafe 手沖小學堂](https://first-cafe.com/category/hand-punching-primary-school/)，讀取日期：2026-06-30。
- [First Cafe WordPress posts API, category 16](https://first-cafe.com/wp-json/wp/v2/posts?categories=16)，讀取日期：2026-06-30。



---
### 📄 來源檔案：`00_來源資料/004_first_cafe_首頁來源.md`
---

---
title: First Cafe 咖啡知識家首頁來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, coffee-knowledge, origin, brewing, sensory, equipment, needs-review]
status: review
updated: 2026-06-30
source_url: https://first-cafe.com/
accessed: 2026-06-30
sources:
  - type: web
    title: 咖啡知識家 - 咖啡知識家
    url: https://first-cafe.com/
    accessed: 2026-06-30
  - type: web
    title: WordPress page API for homepage
    url: https://first-cafe.com/wp-json/wp/v2/pages/56970
    accessed: 2026-06-30
  - type: web
    title: WordPress categories API
    url: https://first-cafe.com/wp-json/wp/v2/categories
    accessed: 2026-06-30
  - type: web
    title: WordPress latest posts API
    url: https://first-cafe.com/wp-json/wp/v2/posts
    accessed: 2026-06-30
---

# First Cafe 咖啡知識家首頁來源

## 摘要

這個來源是 First Cafe「咖啡知識家」首頁。首頁定位是咖啡知識部落格入口，主題涵蓋咖啡歷史、沖煮技巧、全球風味、咖啡豆選擇、感官描述、產地介紹與新手入門。

本知識庫於 `2026-06-30` 讀取首頁、WordPress 首頁 API、分類 API 與最新文章 API。首頁 title 為「咖啡知識家 - 咖啡知識家」。首頁 OpenGraph modified time 為 `2024-11-22T07:34:50+00:00`，WordPress page API 顯示 modified 為 `2024-11-22T15:34:50`。

這份檔案只登錄全站入口與可拆分方向。正式知識文章應逐篇回源讀取，不直接依首頁摘要撰寫。

## 可用資料

首頁與 API 可用資訊包含：

- 首頁 URL：`https://first-cafe.com/`。
- WordPress page id：`56970`。
- 主要導覽：咖啡知識、手沖教學、產地探尋、茶葉知識。
- 社群入口：Facebook、YouTube。
- 外部入口：購買推薦連到 `https://www.bestbet.tw/`，不屬於本站文章來源。
- 最新文章 metadata：發布日期、修改日期、文章 URL、標題、摘要、分類 id、標籤 id。
- 分類 metadata：分類 id、文章數、slug、分類 URL。

## 分類索引

以下依 WordPress categories API 讀取。文章數會變動，使用時需重新查證。

| category id | 分類 | slug | count | url | RAG 用途 |
| --- | --- | --- | ---: | --- | --- |
| 10 | 咖啡知識 | coffee-knowledge | 1031 | https://first-cafe.com/category/coffee-knowledge/ | 咖啡常識、感官、選豆、沖煮、保存與新手問題 |
| 6 | 咖啡產地介紹 | introduction-of-coffee-origin | 246 | https://first-cafe.com/category/introduction-of-coffee-origin/ | 產區、品種、處理法、風土與風味輪廓 |
| 16 | 手沖小學堂 | hand-punching-primary-school | 135 | https://first-cafe.com/category/hand-punching-primary-school/ | 手沖入門、器具、粉水比、水質、悶蒸與注水 |
| 11 | 咖啡知識家 | coffee-knowledgeable | 90 | https://first-cafe.com/category/coffee-knowledgeable/ | 站內品牌或綜合文章，需逐篇判斷用途 |
| 254 | 茶葉知識 | tea-knowledge | 7 | https://first-cafe.com/category/tea-knowledge/ | 非咖啡主題；只在比較茶感、飲品經營或跨品類內容時使用 |
| 1 | Uncategorized | uncategorized | 0 | https://first-cafe.com/category/uncategorized/ | 暫不使用 |

## 文章或素材清單

以下是最新文章 API 讀取的前 20 筆代表文章。為避免大量搬運來源文字，`主題摘要` 使用本知識庫自行整理的短描述，不照抄原文標題。

| date | 主題摘要 | url | 可能分類 |
| --- | --- | --- | --- |
| 2026-06-26 | 咖啡 Body 的定義與厚實口感判讀 | https://first-cafe.com/coffee-body/ | 08_感官 |
| 2026-06-23 | 義式濃縮 Crema 的形成與判讀限制 | https://first-cafe.com/coffee-crema/ | 06_沖煮, 08_感官 |
| 2026-06-12 | 咖啡豆出油、深焙與保存狀態判斷 | https://first-cafe.com/coffee-beans-produce-oil/ | 05_烘焙, 16_產品知識 |
| 2026-05-30 | 空腹喝咖啡與飲用時機注意事項 | https://first-cafe.com/is-it-okay-to-drink-coffee-on-an-empty-stomach/ | 12_FAQ |
| 2026-05-25 | 咖啡澀感與萃取、研磨、水溫、粉水比關係 | https://first-cafe.com/why-is-coffee-bitter/ | 06_沖煮, 08_感官 |
| 2026-05-14 | 研磨後咖啡粉保存與風味流失 | https://first-cafe.com/how-long-can-coffee-powder-be-stored/ | 05_烘焙, 12_FAQ |
| 2026-04-29 | 手沖如何放大果香、花香與堅果焦糖調性 | https://first-cafe.com/want-to-make-your-pour-over-coffee-even-more-fragrant-master-these-pour-over-techniques-to-make-the-fruity-and-floral-aromas-more-pronounced/ | 06_沖煮, 08_感官 |
| 2026-03-27 | 新手手沖器具清單與準備順序 | https://first-cafe.com/pour-over-coffee-equipment/ | 07_設備 |
| 2026-03-25 | 繞圈注水對粉層、水流與風味的影響 | https://first-cafe.com/hand-drip-coffee-in-a-circle/ | 06_沖煮 |
| 2026-03-23 | 藝伎與阿拉比卡的品種關係 | https://first-cafe.com/are-geisha-coffee-beans-arabica/ | 03_品種 |
| 2026-03-18 | 甜感型咖啡豆的選豆方向 | https://first-cafe.com/recommended-sweet-coffee-beans/ | 08_感官, 16_產品知識 |
| 2026-03-14 | 熱門咖啡豆與產區、處理法、烘焙度的選擇邏輯 | https://first-cafe.com/popular-coffee-bean-recommendations/ | 02_產區, 16_產品知識 |
| 2026-03-11 | 阿拉比卡豆的香氣、酸甜與風味選擇 | https://first-cafe.com/arabica-coffee-bean-recommendations/ | 03_品種 |
| 2026-03-03 | 黑咖啡選豆與酸甜、尾韻、乾淨度判斷 | https://first-cafe.com/recommended-black-coffee-beans/ | 08_感官, 16_產品知識 |
| 2026-02-27 | 冰咖啡選豆、焙度與風味表現 | https://first-cafe.com/recommended-coffee-beans-for-iced-coffee-2/ | 06_沖煮, 16_產品知識 |
| 2026-02-25 | 茶感型咖啡豆與清爽風味選擇 | https://first-cafe.com/tea-flavored-coffee-bean-recommendations/ | 08_感官 |
| 2026-02-23 | 果酸型咖啡豆與明亮酸質選擇 | https://first-cafe.com/recommended-fruit-acid-coffee-beans/ | 08_感官 |
| 2026-02-20 | 花香型咖啡豆與品種、處理法、焙度關係 | https://first-cafe.com/floral-coffee-bean-recommendations/ | 03_品種, 08_感官 |
| 2026-02-18 | 美式咖啡選豆與義式配方、單品豆的差異 | https://first-cafe.com/american-coffee-bean-recommendations-2/ | 06_沖煮, 16_產品知識 |
| 2026-02-16 | 義式咖啡豆與濃縮、美式日常飲用選擇 | https://first-cafe.com/recommended-italian-espresso-beans/ | 06_沖煮, 16_產品知識 |

## 建議拆分方向

- `02_產區/`：從「咖啡產地介紹」拆出產區總覽、國家/地區介紹、風土、常見處理法與代表風味。
- `03_品種/`：阿拉比卡、藝伎與其他品種文章，可與既有品種骨架互相連結。
- `05_烘焙/`：出油、保存、烘焙度、咖啡粉保存與風味衰退。
- `06_沖煮/`：Crema、手沖技巧、繞圈注水、冰咖啡、美式與義式沖泡差異。
- `07_設備/`：手沖器具、濾杯、手沖壺、磨豆設備與新手入門清單。
- `08_感官/`：Body、澀感、甜感、果酸、花香、茶感、乾淨度與尾韻。
- `11_QA/`：整理「為什麼會澀」「Crema 是否代表好喝」「空腹能不能喝咖啡」等長答問答。
- `12_FAQ/`：保存期限、飲用時機、咖啡粉保存、出油是否正常等短答。
- `16_產品知識/`：所有推薦型文章只能當作選品語彙與分類參考，實際商品、價格、購買建議需另行查證。

## 使用限制

- 首頁與 API metadata 只適合建立來源地圖，不足以取代逐篇閱讀原文。
- 分類文章數與最新文章會變動，使用時需重新抓取或標示查詢日期。
- 推薦型文章涉及商品、健康、價格或購買決策時，必須回源查證並搭配其他可靠來源。
- `茶葉知識` 不是 Coffee_RAG 主軸；除非做茶感、飲品菜單或跨品類比較，不優先拆文。
- `購買推薦` 是外部站點入口，需另建來源卡，不混入 First Cafe 站內來源。

## 來源

- [First Cafe 咖啡知識家首頁](https://first-cafe.com/)，讀取日期：2026-06-30。
- [First Cafe WordPress page API, page 56970](https://first-cafe.com/wp-json/wp/v2/pages/56970)，讀取日期：2026-06-30。
- [First Cafe WordPress categories API](https://first-cafe.com/wp-json/wp/v2/categories)，讀取日期：2026-06-30。
- [First Cafe WordPress latest posts API](https://first-cafe.com/wp-json/wp/v2/posts)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`00_來源資料/005_first_cafe_咖啡產地介紹來源.md`
---

---
title: First Cafe 咖啡產地介紹來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, origin, country, estate, variety, processing, sensory, product-reference, needs-review]
status: review
updated: 2026-06-30
source_url: https://first-cafe.com/category/introduction-of-coffee-origin/
accessed: 2026-06-30
sources:
  - type: web
    title: 咖啡產地介紹 - 咖啡知識家
    url: https://first-cafe.com/category/introduction-of-coffee-origin/
    accessed: 2026-06-30
  - type: web
    title: WordPress posts API for category 6
    url: https://first-cafe.com/wp-json/wp/v2/posts?categories=6
    accessed: 2026-06-30
---

# First Cafe 咖啡產地介紹來源

## 摘要

這個來源是 First Cafe 咖啡知識家的「咖啡產地介紹」分類頁，首頁導覽也稱為「產地探尋」。內容集中在咖啡產區、莊園、處理廠、品種、處理法、風味描述與咖啡豆推薦語彙。

本知識庫於 `2026-06-30` 讀取分類頁與 WordPress API。分類頁 title 為「咖啡產地介紹 - 咖啡知識家」。

WordPress API 顯示此分類目前共有 246 篇文章、3 頁。API 讀到的文章日期範圍為 `2022-09-05` 到 `2026-01-30`。這份檔案只登錄來源與拆分方向，不搬運文章全文。

## 可用資料

來源頁與 API 可用資訊包含：

- 分類名稱：咖啡產地介紹。
- 首頁導覽名稱：產地探尋。
- 分類 URL：`https://first-cafe.com/category/introduction-of-coffee-origin/`。
- API category id：`6`。
- 文章 metadata：發布日期、修改日期、文章 URL、標題、摘要、分類、標籤 id。
- 分頁資訊：`X-WP-Total: 246`、`X-WP-TotalPages: 3`。
- 分類頁第一頁顯示下一頁：`https://first-cafe.com/category/introduction-of-coffee-origin/page/2/`。

## 標題關鍵字觀察

以下是依 246 篇文章標題做的輕量關鍵字統計，只用來安排拆文優先順序。單篇文章可能同時計入多個關鍵字，正式文章仍需逐篇回源查證。

| 關鍵字 | 標題出現數 | 初步用途 |
| --- | ---: | --- |
| 巴拿馬 | 51 | `02_產區`、藝伎、競標批次、莊園案例 |
| 衣索比亞 | 36 | `02_產區`、耶加雪菲、古吉、處理法 |
| 肯亞 | 22 | `02_產區`、處理廠、AA、圓豆 |
| 哥斯大黎加 | 22 | `02_產區`、蜜處理、厭氧、塔拉珠 |
| 哥倫比亞 | 19 | `02_產區`、莊園、品種、特殊處理 |
| 耶加雪菲 | 18 | `02_產區`、衣索比亞子產區、風味描述 |
| 古吉 | 13 | `02_產區`、衣索比亞子產區、日曬與水洗 |
| 瓜地馬拉 | 12 | `02_產區`、安提瓜、莊園、帕卡瑪拉 |
| 台灣/臺灣 | 15 | `02_產區`、本土咖啡、案例 |
| 巴西 | 8 | `02_產區`、日常豆、商業與精品連結 |
| 薩爾瓦多 | 7 | `02_產區`、中美洲產區 |
| 牙買加 | 6 | `02_產區`、藍山 |
| 宏都拉斯 | 5 | `02_產區`、中美洲產區 |
| 夏威夷 | 5 | `02_產區`、可娜 |

## 文章或素材清單

以下是依 API 讀取的前 20 筆代表文章。為避免大量搬運來源文字，`主題摘要` 使用本知識庫自行整理的短描述，不照抄原文標題。

| date | 主題摘要 | url |
| --- | --- | --- |
| 2026-01-30 | 曼特寧的低酸、厚實口感與挑選重點 | https://first-cafe.com/mandheling-coffee-bean-recommendations/ |
| 2026-01-05 | 尼加拉瓜產區特色與甜感、乾淨度取向 | https://first-cafe.com/recommended-nicaraguan-coffee-beans/ |
| 2025-12-15 | 衣索比亞產區、咖啡風味與選豆方向 | https://first-cafe.com/ethiopian-coffee-bean-recommendations/ |
| 2025-11-25 | 古吉產區風味、處理法與烘焙選擇 | https://first-cafe.com/guji-coffee-bean-recommendations-2/ |
| 2025-11-15 | 藝伎咖啡由來、香氣特色與飲用方式 | https://first-cafe.com/geisha-coffee-bean-recommendations/ |
| 2025-11-10 | 哥斯大黎加高海拔、蜜處理與平衡風味 | https://first-cafe.com/recommended-costa-rican-coffee-beans/ |
| 2025-11-05 | 古吉蔻薩村藝伎日曬與果香型風味 | https://first-cafe.com/guji-coffee-bean-recommendations/ |
| 2025-10-30 | 瓜地馬拉代表產區與花神等風味印象 | https://first-cafe.com/guatemalan-coffee-bean-recommendations/ |
| 2025-06-25 | 產區與處理法如何影響手沖風味 | https://first-cafe.com/coffee-origin/ |
| 2025-04-11 | 新手從風味與文化理解精品咖啡豆 | https://first-cafe.com/coffee-culture-2/ |
| 2025-03-15 | 新手入門咖啡豆、產區、烘焙與沖煮總覽 | https://first-cafe.com/coffee-beans-recommended-3/ |
| 2024-11-30 | 莊園咖啡與一般咖啡的差異、追溯性與價格因素 | https://first-cafe.com/manor-coffee/ |
| 2024-11-29 | 藝伎咖啡等級與精品咖啡品質判斷 | https://first-cafe.com/geisha-coffee-2/ |
| 2024-11-20 | 高 CP 值精品咖啡的選擇語彙 | https://first-cafe.com/high-cp-value-coffee/ |
| 2024-11-10 | 咖啡產地、品種、處理法與沖煮方法總覽 | https://first-cafe.com/coffee-knowledge-2/ |
| 2024-08-23 | 巴拿馬莊園藝伎與厭氧慢速日曬案例 | https://first-cafe.com/panama-donkey-manor-geisha-anaerobic-slow-sun-exposure/ |
| 2024-08-23 | 衣索比亞耶加雪菲日曬與中深烘焙案例 | https://first-cafe.com/ethiopia-yirgacheffe-sun-exposure/ |
| 2024-08-23 | 衣索比亞古吉莊園日曬 G1 案例 | https://first-cafe.com/ethiopia-guji-tintutelo-manor-sunshine-g1/ |
| 2024-08-23 | 肯亞處理廠、圓豆與產區案例 | https://first-cafe.com/kenya-kirinyajia-chiyamugu-processing-plant-round-bean/ |
| 2024-08-23 | 肯亞涅里、處理廠與 AA 等級案例 | https://first-cafe.com/kenya-nyeri-gasasi-treatment-plant-aa/ |

## 建議拆分方向

- `02_產區/`：優先建立巴拿馬、衣索比亞、肯亞、哥斯大黎加、哥倫比亞、瓜地馬拉、台灣、牙買加、尼加拉瓜、印尼等產區文章。
- `02_產區/`：建立耶加雪菲、古吉、塔拉珠、安提瓜、可娜、藍山等子產區或知名產地條目。
- `03_品種/`：藝伎、帕卡瑪拉、SL28、卡杜拉、帝比卡、圓豆等品種或豆型條目。
- `04_處理法/`：日曬、水洗、蜜處理、厭氧、熱發酵、二氧化碳低咖啡因處理等條目。
- `08_感官/`：厚實 Body、低酸、花香、果香、茶感、可可、草本、酸甜平衡等描述語彙。
- `15_案例/`：莊園、處理廠、競標批次、COE、ToH 等案例型素材。
- `16_產品知識/`：推薦型與品項型文章可用於選品語彙，但不可直接當成庫存或價格資料。

## 使用限制

- 此檔案只作為來源索引，不作為正式知識文章。
- 此分類混合教學文、推薦文與單一品項文；拆文時需先判斷文章類型。
- 標題關鍵字統計只能反映標題分布，不能代表完整內容權重。
- 涉及商品推薦、價格、庫存、健康或購買建議時，需回源查證並標示查詢日期。
- 不要直接複製文章全文；需整理為 Coffee_RAG 的文章格式並保留來源。

## 來源

- [First Cafe 咖啡產地介紹](https://first-cafe.com/category/introduction-of-coffee-origin/)，讀取日期：2026-06-30。
- [First Cafe WordPress posts API, category 6](https://first-cafe.com/wp-json/wp/v2/posts?categories=6)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`00_來源資料/006_buon_caffe_咖啡豆知識來源.md`
---

---
title: Buon Caffe 步昂咖啡咖啡豆知識來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, coffee-bean, variety, origin, grading, specialty-coffee, processing, roasting, sensory, beginner, needs-review]
status: review
updated: 2026-06-30
source_url: https://buoncaffe.com.tw/blog/posts/coffeebean/
accessed: 2026-06-30
sources:
  - type: web
    title: Buon Caffe coffee bean article
    url: https://buoncaffe.com.tw/blog/posts/coffeebean/
    accessed: 2026-06-30
---

# Buon Caffe 步昂咖啡咖啡豆知識來源

## 摘要

這個來源是 Buon Caffe 步昂咖啡「步昂專欄」中的咖啡豆總覽文章。內容適合當作咖啡新手知識地圖，涵蓋咖啡豆基本定義、主要品種、世界產地、生豆分級、精品咖啡、處理法、焙度、酸度與風味輪。

本知識庫於 `2026-06-30` 讀取文章頁。頁面 metadata 顯示文章發布時間為 `2021-05-29T00:00:00+08:00`，修改時間為 `2025-03-04T01:53:12+08:00`。文章區段為「步昂專欄」，頁面標籤包含咖啡、精品咖啡、處理法。

這份檔案只登錄來源與拆分方向，不搬運文章全文。

## 可用資料

來源頁可用資訊包含：

- 文章 URL：`https://buoncaffe.com.tw/blog/posts/coffeebean/`。
- 文章類型：咖啡豆基礎知識總覽。
- 文章分類：步昂專欄。
- 文章作者 metadata：`benson`。
- 發布日期：`2021-05-29`。
- 修改日期：`2025-03-04`。
- 內文目錄錨點：`#a01` 到 `#a08`。
- 相關站內延伸閱讀：咖啡樹種植、三大咖啡豆品種、世界產區、肯亞分級、杯測、精品咖啡、處理法、烘焙、風味輪。
- 站內商品連結：可作為產品命名與品項欄位參考，但不能直接當作庫存、價格或推薦結論。

## 主題地圖

| 文章段落 | 可拆到 | RAG 用途 |
| --- | --- | --- |
| 咖啡豆是什麼 | `01_咖啡歷史`, `03_品種`, `12_FAQ` | 說明咖啡豆與咖啡果實、種子的基本概念 |
| 三大咖啡豆種類 | `03_品種` | 阿拉比卡、羅布斯塔與賴比瑞亞的入門比較 |
| 世界主要咖啡產地 | `02_產區` | 非洲、中南美洲、亞洲主要產地與區域風味線索 |
| 咖啡生豆分級 | `02_產區`, `16_產品知識` | 肯亞、衣索比亞、印尼、哥倫比亞、巴西等分級制度入口 |
| 精品咖啡定義 | `08_感官`, `16_產品知識` | 精品咖啡、杯測、瑕疵、風味特色與評分語彙 |
| 咖啡處理法 | `04_處理法` | 日曬、半日曬、水洗、半水洗的入門比較 |
| 咖啡焙度與風味 | `05_烘焙`, `08_感官` | 淺焙、中焙、中深焙、深焙與風味傾向 |
| 酸度與風味 | `08_感官`, `11_QA` | 酸質、果酸、苦甜、口感與新手誤解 |
| 如何判別咖啡風味 | `08_感官` | 風味輪使用與風味描述練習 |

## 代表重點

以下為本知識庫整理的主題摘要，不照抄原文：

- 咖啡豆可從植物果實、種子與生豆/熟豆狀態切入，適合建立新手 FAQ。
- 品種段落可支援阿拉比卡、羅布斯塔、賴比瑞亞的基礎比較。
- 產地段落可支援非洲、中南美洲、亞洲三大區域的初步風味輪廓。
- 分級段落可支援各國分級制度入口，但需逐國補充更可靠來源。
- 精品咖啡段落可支援杯測、瑕疵、風味特色與 SCA/SCAA 歷史用語整理。
- 處理法段落適合拆成日曬、半日曬、水洗、半水洗四篇入門文章。
- 焙度段落適合建立焙度與酸甜苦、口感、香氣類型的關係。
- 風味輪段落適合拆成感官訓練與風味描述流程。

## 站內延伸來源

此文章列出多個延伸閱讀，可視需要逐篇另建來源卡：

| 主題 | url | 後續用途 |
| --- | --- | --- |
| 咖啡樹種植 | https://buoncaffe.com.tw/blog/posts/coffeeplant | `01_咖啡歷史`, `03_品種` |
| 三大咖啡豆品種 | https://buoncaffe.com.tw/blog/posts/coffeebean-species | `03_品種` |
| 世界產區與風味 | https://buoncaffe.com.tw/blog/posts/coffee-producing-countries | `02_產區`, `08_感官` |
| 肯亞咖啡分級 | https://buoncaffe.com.tw/blog/posts/kenyacoffeegrading | `02_產區`, `16_產品知識` |
| 步昂杯測 | https://buoncaffe.com.tw/blog/posts/blogcupping | `08_感官` |
| 精品咖啡介紹 | https://buoncaffe.com.tw/blog/posts/specialitycoffeev1 | `08_感官`, `16_產品知識` |
| 精品咖啡選擇 | https://buoncaffe.com.tw/blog/posts/knowyourcoffee | `16_產品知識`, `12_FAQ` |
| 處理法延伸 | https://buoncaffe.com.tw/blog/posts/passionfruit | `04_處理法` |
| 烘豆過程 | https://buoncaffe.com.tw/blog/posts/roast-level | `05_烘焙` |
| 焙度與風味 | https://buoncaffe.com.tw/blog/posts/roast-level-and-flavor | `05_烘焙`, `08_感官` |
| 烘豆手法 | https://buoncaffe.com.tw/blog/posts/roastrhythms | `05_烘焙` |
| 風味輪 | https://buoncaffe.com.tw/blog/posts/scaawheel | `08_感官` |

## 建議拆分方向

- `02_產區/`：建立非洲、中南美洲、亞洲產區入門，以及衣索比亞、肯亞、哥倫比亞、巴西、印尼、越南、印度等條目。
- `03_品種/`：建立阿拉比卡、羅布斯塔、賴比瑞亞比較文。
- `04_處理法/`：建立日曬、半日曬、水洗、半水洗入門文，並與 First Cafe 的處理法素材互相連結。
- `05_烘焙/`：建立焙度與風味關係、烘焙深淺、保存與新手選豆建議。
- `08_感官/`：建立酸度、Body、餘韻、風味輪與杯測描述語彙。
- `11_QA/`：整理「咖啡豆是什麼」「咖啡酸是不是壞掉」「新手要選什麼焙度」等長答。
- `12_FAQ/`：整理三大品種、處理法、焙度、風味輪的短答。
- `16_產品知識/`：商品連結只用於命名、產地、處理法、焙度欄位設計；商品狀態需另行查證。

## 使用限制

- 此檔案只作為來源索引，不作為正式知識文章。
- 文章是品牌部落格總覽文，若要建立權威條目，需搭配 SCA、ICO、產區官方資料或其他來源交叉查證。
- 文章中涉及 SCAA/SCA、精品咖啡評分與國家分級制度時，需補上官方或專業來源。
- 商品連結、優惠、價格與庫存會變動，不應直接寫入穩定知識文章。
- 不要直接複製文章全文；需整理為 Coffee_RAG 的文章格式並保留來源。

## 來源

- [Buon Caffe 步昂咖啡咖啡豆知識文章](https://buoncaffe.com.tw/blog/posts/coffeebean/)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`00_來源資料/007_咖啡專業權威資源清單.md`
---

---
title: 咖啡專業權威資源清單
category: 00_來源資料
type: source_catalog
tags: [source, authority, research, industry-news, sensory, brewing-science, education, reading-plan, needs-review]
status: review
updated: 2026-06-30
source_url: multiple
accessed: 2026-06-30
sources:
  - type: web
    title: Perfect Daily Grind
    url: https://perfectdailygrind.com/
    accessed: 2026-06-30
  - type: web
    title: Daily Coffee News by Roast Magazine
    url: https://dailycoffeenews.com/
    accessed: 2026-06-30
  - type: web
    title: Sprudge
    url: https://sprudge.com/
    accessed: 2026-06-30
  - type: web
    title: SCA Brewing Fundamentals Research
    url: https://sca.coffee/brewing-research
    accessed: 2026-06-30
  - type: web
    title: SCA Coffee Value Assessment
    url: https://sca.coffee/value-assessment
    accessed: 2026-06-30
  - type: web
    title: BrewingScience
    url: https://www.brewingscience.de/
    accessed: 2026-06-30
  - type: web
    title: Coffee Review
    url: https://www.coffeereview.com/
    accessed: 2026-06-30
  - type: web
    title: World Coffee Research Sensory Lexicon
    url: https://worldcoffeeresearch.org/resources/sensory-lexicon
    accessed: 2026-06-30
  - type: web
    title: iCoffee 咖啡學院
    url: https://icoffee.tw/
    accessed: 2026-06-30
---

# 咖啡專業權威資源清單

## 摘要

這份來源卡整理專業咖啡知識庫的長期閱讀與查證來源。用途不是立即拆成單篇文章，而是建立 Coffee_RAG 的證據層級、閱讀管線與研究入口。

本知識庫於 `2026-06-30` 讀取主要官方、研究與專業媒體網站。JimSeven 本輪以 `https://jimseven.com/` 與 `https://www.jimseven.com/` 抓取逾時，先保留為推薦來源但不引用未讀取內容。書目與課程資源先作為待查證候選，不寫成已核實資料。

## 證據層級

| 層級 | 來源類型 | 用途 | 代表來源 |
| --- | --- | --- | --- |
| A | 官方、研究、標準、期刊 | 定義、標準、方法、科學與評鑑 | SCA、WCR、BrewingScience |
| B | 專業媒體、專家評論 | 產業趨勢、新聞、文化、商業脈動 | Perfect Daily Grind、Daily Coffee News、Sprudge、Coffee Review |
| C | 教育平台、品牌部落格、產品頁 | 教學語彙、案例、產品命名、在地語境 | iCoffee、Buon Caffe、First Cafe |
| D | 社群、論壇、未查證摘要 | 顧客語言、問題靈感 | 僅作線索，不作正式來源 |

## 已讀取來源

| 來源 | 讀取狀態 | metadata 觀察 | 建議用途 |
| --- | --- | --- | --- |
| Perfect Daily Grind | 已讀取首頁 | title 顯示為咖啡新聞出版物，description 指向 brewing、roasting、production、coffee shops 等主題 | `10_創業`、`02_產區`、`05_烘焙`、`06_沖煮` 的趨勢與產業脈絡 |
| Daily Coffee News | 已讀取首頁 | title 顯示為 Roast Magazine 旗下 specialty coffee professionals 商業新聞 | `10_創業`、供應鏈、市場、設備與烘焙商業新聞 |
| Sprudge | 已讀取首頁 | description 指向 coffee news、guides、recommendations | 咖啡文化、咖啡店案例、活動與人文脈絡 |
| SCA Brewing Research | 已讀取頁面 | title 為 Brewing Fundamentals Research，頁面主標指向 coffee brewing fundamentals | `06_沖煮`、萃取、水質、沖煮變因 |
| SCA Coffee Value Assessment | 已讀取頁面 | title 為 Coffee Value Assessment，頁面包含 CVA forms、glossaries、key documents | `08_感官`、杯測、價值評估、評鑑方法 |
| BrewingScience | 已讀取首頁 | description 指向大學與研究成果到實務的知識轉移 | 科學研究入口，需逐篇讀取論文 |
| Coffee Review | 已讀取首頁 | description 指向 coffee reviews、espresso ratings、articles、blogs | 評鑑語彙、風味描述、消費者評分脈絡 |
| WCR Sensory Lexicon | 已讀取頁面 | title 為 Sensory Lexicon，description 指向咖啡風味與香氣的理解與量測工具 | `08_感官` 的標準化詞彙 |
| iCoffee 咖啡學院 | 已讀取首頁 | description 指向精品咖啡、咖啡豆、手沖、產地歷史與文化 | 中文教學語彙與在地搜尋入口 |

## 待查證來源

| 來源 | 狀態 | 下一步 |
| --- | --- | --- |
| JimSeven | 本輪抓取逾時 | 之後單獨讀取或以搜尋定位可用文章 |
| 咖啡專業知識全書 | 書目未核實 | 查作者、出版社、年份、ISBN |
| 賺錢咖啡店經營法則 | 書目未核實 | 查作者、出版社、年份、ISBN |
| SCA 課程與 CVA 教育資源 | 需逐頁確認 | 優先使用 SCA 官方頁，不以二手課程頁作標準來源 |
| 國內咖啡學院課程頁 | 需逐頁確認 | 只作課程資訊，不作科學標準來源 |

## 建議拆分方向

- `06_沖煮/`：從 SCA Brewing Research 建立萃取、水質、研磨、沖煮變因研究索引。
- `08_感官/`：從 WCR Sensory Lexicon 與 SCA CVA 建立感官詞彙、杯測、價值評估、風味描述方法。
- `10_創業/`：從 Daily Coffee News、Perfect Daily Grind、Sprudge 建立產業趨勢、供應鏈、咖啡店案例閱讀管線。
- `15_案例/`：從 Sprudge 與專業媒體拆咖啡店設計、品牌案例、永續與社會責任案例。
- `12_FAQ/`：從權威來源整理「什麼是 CVA」「風味輪怎麼用」「精品咖啡評分可信嗎」等短答。
- `00_來源資料/`：為 SCA、WCR、Coffee Review、PDG 等重要網站各自建立更細的來源卡。

## 使用限制

- 這份清單是來源地圖，不是正式知識文章。
- 科學、標準與評鑑方法應優先回到 SCA、WCR、期刊或官方文件。
- 媒體文章適合追蹤趨勢，但市場資訊與新聞需重新查證日期。
- 品牌與教育網站適合學習語彙與案例，不應單獨作為權威結論。
- 未讀取或未核實來源只能標為 lead，不可寫成已確認事實。

## 來源

- [Perfect Daily Grind](https://perfectdailygrind.com/)，讀取日期：2026-06-30。
- [Daily Coffee News](https://dailycoffeenews.com/)，讀取日期：2026-06-30。
- [Sprudge](https://sprudge.com/)，讀取日期：2026-06-30。
- [SCA Brewing Research](https://sca.coffee/brewing-research)，讀取日期：2026-06-30。
- [SCA Coffee Value Assessment](https://sca.coffee/value-assessment)，讀取日期：2026-06-30。
- [BrewingScience](https://www.brewingscience.de/)，讀取日期：2026-06-30。
- [Coffee Review](https://www.coffeereview.com/)，讀取日期：2026-06-30。
- [World Coffee Research Sensory Lexicon](https://worldcoffeeresearch.org/resources/sensory-lexicon)，讀取日期：2026-06-30。
- [iCoffee 咖啡學院](https://icoffee.tw/)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`00_來源資料/008_1980cafe_咖啡師工作內容來源.md`
---

---
title: 1980 CAFE 咖啡師工作內容來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, barista, cafe-operations, brewing, equipment, service, training, tier-c, needs-review]
status: review
updated: 2026-06-30
source_url: https://www.1980cafetw.com/blog/Barista
accessed: 2026-06-30
sources:
  - type: web
    title: 咖啡師的工作內容及養成
    url: https://www.1980cafetw.com/blog/Barista
    accessed: 2026-06-30
---

# 1980 CAFE 咖啡師工作內容來源

## 摘要

這個來源是 1980 CAFE 咖啡生活部落格的單篇文章，主題是咖啡師的工作內容與養成。內容涵蓋 Barista 的角色、服務與溝通、咖啡豆基礎知識、沖煮工具、咖啡機與磨豆機調整、吧台清潔、採購與日常營運。

本知識庫於 `2026-06-30` 讀取文章頁。頁面 metadata 顯示發布時間與修改時間皆為 `2020-01-01T17:18:47+08:00`。文章標籤包含 `roaster`、`coffee_knowledge`。

此來源屬於 Tier C 品牌部落格，可作為咖啡師職能、吧台營運與顧客服務的實務語彙參考。若要建立正式職能標準，需搭配 SCA、課程標準、職訓資料或實際門市 SOP 交叉查證。

## 可用資料

來源頁可用資訊包含：

- 文章 URL：`https://www.1980cafetw.com/blog/Barista`。
- 文章標題：咖啡師的工作內容及養成。
- 網站名稱：1980 CAFE 咖啡生活部落格。
- 發布日期：`2020-01-01`。
- 修改日期：`2020-01-01`。
- 作者 metadata：1980 CAFE 咖啡豆購物商城。
- 標籤：`roaster`、`coffee_knowledge`。
- 相關文章連結：咖啡豆選購、Hario V60、烘焙度。

## 主題地圖

| 主題 | 可拆到 | RAG 用途 |
| --- | --- | --- |
| 咖啡師角色 | `09_開店`, `10_創業` | 吧台職能、門市角色分工、服務定位 |
| 顧客服務與溝通 | `09_開店`, `11_QA` | 顧客偏好詢問、推薦咖啡、門市體驗 |
| 咖啡豆知識 | `02_產區`, `03_品種`, `16_產品知識` | 咖啡師需理解產地、品種、風味差異 |
| 沖煮技術 | `06_沖煮` | 基礎沖煮能力、依客人口味調整 |
| 咖啡機與磨豆機調整 | `07_設備`, `06_沖煮` | 粗細、粉量、設備操作與每日校正 |
| 清潔與吧台營運 | `09_開店` | 清潔、購貨、日常營運、責任分工 |
| 咖啡師養成 | `09_開店`, `11_QA` | 新人訓練、技能路徑、工作內容說明 |

## 代表重點

以下為本知識庫整理的主題摘要，不照抄原文：

- 咖啡師不只是製作咖啡，也承擔服務、溝通、門市體驗與吧台營運。
- 專業咖啡師需要理解咖啡豆、沖煮工具、設備與萃取調整。
- 咖啡豆狀態會受濕度、光線、空氣與溫度影響，因此吧台需要日常觀察與校正。
- 入職訓練可從清潔、服務、溝通、日常營運與基礎沖煮開始。
- 吧台工作包含清潔、補貨、採購或購貨協作，以及依顧客偏好調整飲品。

## 站內延伸來源

此文章列出多個延伸閱讀，可視需要逐篇另建來源卡：

| 主題 | url | 後續用途 |
| --- | --- | --- |
| 咖啡豆基礎選購 | https://www.1980cafetw.com/blog/coffee-bean-guide | `16_產品知識`, `12_FAQ` |
| Hario V60 陶瓷濾杯 | https://www.1980cafetw.com/blog/hario_v60 | `06_沖煮`, `07_設備` |
| 咖啡烘焙度 | https://www.1980cafetw.com/blog/roast_coffee_beans | `05_烘焙`, `08_感官` |

## 建議拆分方向

- `09_開店/`：建立咖啡師工作內容、吧台職責、新人訓練、吧台清潔與營運 SOP。
- `06_沖煮/`：建立每日沖煮校正、粉量與研磨調整、依客人口味調整咖啡。
- `07_設備/`：建立咖啡機、磨豆機日常檢查與調整要點。
- `11_QA/`：建立「咖啡師每天做什麼」「咖啡師需要會哪些技能」「新手怎麼成為咖啡師」等長答。
- `12_FAQ/`：建立 Barista、吧台職責、咖啡師訓練與門市服務短答。
- `10_創業/`：若做開店內容，可將咖啡師職能轉為人員配置與培訓清單。

## 使用限制

- 此檔案只作為來源索引，不作為正式知識文章。
- 此來源是品牌部落格，不是職能標準或官方課程規範。
- 文章中的品種、設備與職能描述若要成為正式條目，需搭配更高層級來源或實務 SOP。
- 文章發布於 2020 年；涉及職場現況、薪資、證照或課程資訊時必須重新查證。
- 不要直接複製文章全文；需整理為 Coffee_RAG 的文章格式並保留來源。

## 來源

- [1980 CAFE 咖啡師的工作內容及養成](https://www.1980cafetw.com/blog/Barista)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`00_來源資料/009_zhanlu_濾掛咖啡商品分類來源.md`
---

---
title: 湛盧咖啡濾掛咖啡商品分類來源
category: 00_來源資料
type: source_catalog
tags: [source, ecommerce, product-category, drip-bag, zhanlu, product-knowledge, tier-c, volatile, needs-review]
status: review
updated: 2026-06-30
source_url: https://www.zhanlu.com.tw/product-category/drip-bag-coffee/
accessed: 2026-06-30
sources:
  - type: web
    title: 手沖精品濾掛咖啡 : 湛盧咖啡
    url: https://www.zhanlu.com.tw/product-category/drip-bag-coffee/
    accessed: 2026-06-30
---

# 湛盧咖啡濾掛咖啡商品分類來源

## 摘要

這個來源是湛盧咖啡官網的「濾掛式咖啡包」商品分類頁。內容可作為濾掛咖啡產品知識、商品分類、系列命名、包裝規格、焙度分類、禮盒與銷售問答的來源。

本知識庫於 `2026-06-30` 讀取頁面。頁面 title 為「手沖精品濾掛咖啡 : 湛盧咖啡」，metadata description 指向「手沖精品濾掛咖啡」、多種掛耳式咖啡與自由選擇。頁面 schema 顯示此頁為 `CollectionPage`，分類名稱為「濾掛式咖啡包」。

此來源屬於 Tier C 品牌產品頁。價格、促銷、庫存、商品排序與商品總數都屬於易變資料，回答使用者前必須重新查證或標示查詢日期。

## 可用資料

來源頁可用資訊包含：

- 分類 URL：`https://www.zhanlu.com.tw/product-category/drip-bag-coffee/`。
- 商品分類名稱：濾掛式咖啡包。
- WooCommerce post id：`79`。
- 查詢當下結果數：顯示第 1 至 12 項結果，共 67 項。
- 分頁：第 1 至 6 頁。
- 商品卡欄位：product id、商品名稱、商品 URL、HTML `data-price`、商品分類、商品類型、加入購物車或選擇規格狀態。
- 商品分類結構：大組數、嚐鮮組合、焙度、系列、禮盒、活動與預算分類。
- 頁面 feed：`https://www.zhanlu.com.tw/product-category/drip-bag-coffee/feed/`。

## 分類結構

頁面導覽與商品分類顯示，濾掛相關入口包含：

| 分類 | url | 用途 |
| --- | --- | --- |
| 官網限定｜80-100入大組數 | https://www.zhanlu.com.tw/product-category/drip-bag-coffee-80/ | 大量採購、辦公室、長期飲用 |
| 30-60入｜嚐鮮組合 | https://www.zhanlu.com.tw/product-category/2024_dripbag30/ | 中等組數、試飲或家庭備貨 |
| 淺烘焙 | https://www.zhanlu.com.tw/product-category/light-roast-drip-bag/ | 明亮、果香、清爽取向 |
| 中烘焙 | https://www.zhanlu.com.tw/product-category/medium-roast-drip-bag/ | 平衡、層次、日常飲用 |
| 深烘焙 | https://www.zhanlu.com.tw/product-category/dark-roast-drip-bag/ | 厚實、濃郁、咖啡感取向 |
| 尊爵極精品系列 | https://www.zhanlu.com.tw/product-category/drip-bag-coffee/premium_drip_bag/ | 高端系列與送禮語彙 |
| 繽紛莊園單品系列 | https://www.zhanlu.com.tw/product-category/drip-bag-coffee/%e7%b9%bd%e7%b4%9b%e8%8e%8a%e5%9c%92%e5%96%ae%e5%93%81%e7%b3%bb%e5%88%97/ | 單品、產區、風味選擇 |
| 頂級行家系列 | https://www.zhanlu.com.tw/product-category/drip-bag-coffee/drip-bag-coffee-7/ | 行家配方與進階風味 |
| 熱銷經典系列 | https://www.zhanlu.com.tw/product-category/drip-bag-coffee/drip-bag-coffee-5/ | 入門、熱銷、穩定口味 |

## 商品樣本

以下為 `2026-06-30` 抓取第 1 頁時的商品卡樣本。`price_sample_ntd` 來自頁面 HTML 屬性或追蹤 JSON，只能作為查詢當下樣本，不可作為正式報價。

| product_id | 商品樣本 | price_sample_ntd | url |
| --- | --- | ---: | --- |
| 2200 | 全系列任選濾掛式咖啡自由選 10入袋裝 | 225 | https://www.zhanlu.com.tw/product/dripbagcoffee_mixflavor/ |
| 170674 | 新年限定禮盒單品40入禮盒 | 930 | https://www.zhanlu.com.tw/product/%e6%96%b0%e5%b9%b4%e9%99%90%e5%ae%9a%e7%a6%ae%e7%9b%92-%e5%96%ae%e5%93%8140%e5%85%a5%e7%a6%ae%e7%9b%92/ |
| 170622 | 新年限定禮盒經典40入禮盒 | 960 | https://www.zhanlu.com.tw/product/%e6%96%b0%e5%b9%b4%e9%99%90%e5%ae%9a%e7%a6%ae%e7%9b%92-%e7%b6%93%e5%85%b840%e5%85%a5%e7%a6%ae%e7%9b%92/ |
| 170623 | 新年限定禮盒單品28入禮盒 | 860 | https://www.zhanlu.com.tw/product/%e6%96%b0%e5%b9%b4%e9%99%90%e5%ae%9a%e7%a6%ae%e7%9b%92-%e5%96%ae%e5%93%8128%e5%85%a5%e7%a6%ae%e7%9b%92/ |
| 130604 | 中淺烘焙玫瑰人生 Aloha 5入盒 | 300 | https://www.zhanlu.com.tw/product/dripbag_premium_bag_rose_aloha/ |
| 110029 | 淺烘焙玫瑰人生綻放 5入盒 | 300 | https://www.zhanlu.com.tw/product/dripbag_premium_bag_rose_blossom/ |
| 109860 | 淺烘焙玫瑰人生 5入盒 | 300 | https://www.zhanlu.com.tw/product/dripbag_premium_bag_rose/ |
| 142453 | 莊園單品全系列自由選 10入袋裝 | 262 | https://www.zhanlu.com.tw/product/dripbag_singleflavor/ |
| 56183 | the V.21 和行家系列風味自選 100入袋 | 2125 | https://www.zhanlu.com.tw/product/dripbag_7_100/ |
| 153841 | 淺焙行家 30入盒 | 759 | https://www.zhanlu.com.tw/product/dripbagcoffee_light7_30_all/ |
| 157032 | 淺烘焙行家首選風味自選 100入袋 | 2125 | https://www.zhanlu.com.tw/product/dripbag_7light_100/ |
| 176512 | 中與中深烘焙 the V.21 100入袋 | 2125 | https://www.zhanlu.com.tw/product/thev21-100/ |

## 建議拆分方向

- `16_產品知識/`：建立湛盧濾掛咖啡系列、規格、包裝數、焙度、價格查詢規則與商品問答。
- `12_FAQ/`：建立「濾掛咖啡怎麼選」「10入、30入、100入差在哪」「淺焙中焙深焙怎麼選」等短答。
- `11_QA/`：建立湛盧濾掛推薦與送禮情境長答，但回答前需重新查證商品頁。
- `05_烘焙/`：整理濾掛商品用語中的淺烘焙、中烘焙、深烘焙與風味期待。
- `08_感官/`：從單品、行家、經典、玫瑰人生、V.21 等系列整理風味描述語彙。
- `10_創業/`：若做辦公室、企業採購或咖啡車備品，可用大組數與禮盒分類作情境參考。

## 使用限制

- 此檔案只作為來源索引，不作為正式產品型錄或報價單。
- 商品總數、排序、價格、折扣、庫存與活動分類會變動；回答使用者前必須重新查證。
- 商品名稱可作為產品語彙與分類參考，但口味、產區、配方細節需逐一讀取商品頁。
- 價格欄是抓取當下的樣本，不可單獨用於銷售報價。
- 若要建立正式產品 FAQ，需逐個商品頁補充規格、內容物、保存期限、有效日期與配送限制。

## 來源

- [湛盧咖啡濾掛式咖啡包分類頁](https://www.zhanlu.com.tw/product-category/drip-bag-coffee/)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`00_來源資料/010_zhanlu_咖啡生活誌來源.md`
---

---
title: 湛盧咖啡咖啡生活誌來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, zhanlu, coffee-life, brewing, drip-bag, beginner, roasting, sensory, product-knowledge, tier-c, needs-review]
status: review
updated: 2026-06-30
source_url: https://www.zhanlu.com.tw/category/coffeelife/
accessed: 2026-06-30
sources:
  - type: web
    title: 湛盧咖啡咖啡生活誌
    url: https://www.zhanlu.com.tw/category/coffeelife/
    accessed: 2026-06-30
  - type: web
    title: WordPress category API for coffeelife
    url: https://www.zhanlu.com.tw/wp-json/wp/v2/categories?slug=coffeelife
    accessed: 2026-06-30
  - type: web
    title: WordPress posts API for category 687
    url: https://www.zhanlu.com.tw/wp-json/wp/v2/posts?categories=687
    accessed: 2026-06-30
---

# 湛盧咖啡咖啡生活誌來源

## 摘要

這個來源是湛盧咖啡官網的「咖啡生活誌」分類頁。內容橫跨新手選豆、濾掛咖啡沖泡、精品咖啡開箱、送禮情境、咖啡健康、美式咖啡、產區介紹、咖啡酸質、焙度、手沖、拿鐵與咖啡風味描述。

本知識庫於 `2026-06-30` 讀取分類頁與 WordPress API。分類頁 title 為「湛盧咖啡－咖啡生活誌：創造生活的甜蜜點」。WordPress category API 顯示 category id 為 `687`、分類名稱為「咖啡生活誌」、文章數為 `50`。posts API 顯示文章日期範圍為 `2020-05-29` 到 `2026-05-27`。

此來源屬於 Tier C 品牌內容與產品導向教育文章，可作為教學語彙、產品語彙、顧客問題與內容行銷題材參考。涉及健康、商品推薦、節慶禮盒、熱銷排行、價格或品牌現況時，必須重新查證並搭配更高層級來源。

## 可用資料

來源頁與 API 可用資訊包含：

- 分類 URL：`https://www.zhanlu.com.tw/category/coffeelife/`。
- 分類名稱：咖啡生活誌。
- API category id：`687`。
- 文章總數：`50`。
- 分類頁顯示分頁：第 1 至 5 頁。
- API 欄位：文章日期、修改日期、文章 URL、標題、摘要、分類、標籤 id。
- 分類 feed：`https://www.zhanlu.com.tw/category/coffeelife/feed/`。
- 相鄰內容入口：創辦人專欄、極精品沙龍、湛盧讀味、商品分類與企業服務。

## 標題關鍵字觀察

以下是依 50 篇文章標題做的輕量統計，只用來安排拆文優先順序。單篇文章可能同時計入多個關鍵字，正式文章仍需逐篇回源查證。

| 關鍵字 | 標題出現數 | 初步用途 |
| --- | ---: | --- |
| 濾掛 | 9 | `06_沖煮`、`16_產品知識`、`12_FAQ` |
| 咖啡豆 | 6 | `03_品種`、`05_烘焙`、`16_產品知識` |
| 禮盒 | 4 | `10_創業`、`16_產品知識`、送禮情境 |
| 處理法 | 4 | `04_處理法`、選豆與風味理解 |
| 手沖 | 4 | `06_沖煮`、新手教學 |
| 烘焙 | 2 | `05_烘焙`、焙度選擇 |
| 義式 | 2 | `06_沖煮`、飲品比較 |
| 美式/黑咖啡 | 1 | `06_沖煮`、`12_FAQ` |
| 健康/咖啡因 | 1 | `12_FAQ`，需搭配更高層級健康來源 |
| 哥斯大黎加 | 1 | `02_產區`、蜜處理 |

## 文章或素材清單

以下是依 API 讀取的前 20 筆代表文章。為避免大量搬運來源文字，`主題摘要` 使用本知識庫自行整理的短描述，不照抄原文標題。

| date | modified | 主題摘要 | url |
| --- | --- | --- | --- |
| 2026-05-27 | 2026-06-02 | 新手選豆，涵蓋焙度、處理法、送禮與口味判斷 | https://www.zhanlu.com.tw/%e6%96%b0%e6%89%8b%e6%8c%91%e9%81%b8%e5%92%96%e5%95%a1%e8%b1%86%e6%8c%87%e5%8d%97/ |
| 2026-05-20 | 2026-06-02 | 濾掛咖啡沖泡步驟與常見錯誤 | https://www.zhanlu.com.tw/%e6%bf%be%e6%8e%9b%e5%92%96%e5%95%a1%e6%b2%96%e6%b3%a1%e6%ad%a5%e9%a9%9f%e6%95%99%e5%ad%b8/ |
| 2026-04-22 | 2026-04-28 | 精品咖啡與堅果的風味搭配 | https://www.zhanlu.com.tw/classic_mixed_nuts-2/ |
| 2026-04-02 | 2026-04-22 | the V.21 風味與不同沖煮型態的產品開箱 | https://www.zhanlu.com.tw/thev21-2-2/ |
| 2026-01-26 | 2026-02-25 | 濾掛咖啡不好喝的常見原因 | https://www.zhanlu.com.tw/hand-drip-coffee/ |
| 2026-01-14 | 2026-02-09 | 年節伴手禮與咖啡禮盒推薦情境 | https://www.zhanlu.com.tw/%e9%81%8e%e5%b9%b4%e4%bc%b4%e6%89%8b%e7%a6%ae/ |
| 2025-07-13 | 2026-05-27 | 濾掛咖啡推薦與熱銷排行語彙 | https://www.zhanlu.com.tw/2026%e6%bf%be%e6%8e%9b%e5%92%96%e5%95%a1%e6%8e%a8%e8%96%a6/ |
| 2025-06-16 | 2025-06-18 | 每天喝咖啡的健康功效與攝取提醒 | https://www.zhanlu.com.tw/%e5%96%9d%e5%92%96%e5%95%a1%e7%9a%84%e5%a5%bd%e8%99%95/ |
| 2025-06-02 | 2025-06-02 | 美式咖啡、黑咖啡、比例、咖啡因與熱量 | https://www.zhanlu.com.tw/%e9%bb%91%e5%92%96%e5%95%a1/ |
| 2025-04-15 | 2025-12-26 | 哥斯大黎加產區與蜜處理風味 | https://www.zhanlu.com.tw/%e5%93%a5%e6%96%af%e5%a4%a7%e9%bb%8e%e5%8a%a0%e5%92%96%e5%95%a1/ |
| 2025-02-14 | 2025-02-14 | 咖啡酸質與風味描述詞彙 | https://www.zhanlu.com.tw/%e5%92%96%e5%95%a1%e9%85%b8%e5%91%b3%e8%b6%8a%e9%87%8d%e4%bb%a3%e8%a1%a8%e5%93%81%e8%b3%aa%e8%b6%8a%e5%a5%bd%e5%97%8e%ef%bc%9f%e8%aa%8d%e8%ad%988%e5%80%8b%e5%92%96%e5%95%a1%e5%bd%a2%e5%ae%b9%e8%a9%9e/ |
| 2024-12-10 | 2024-12-26 | 冬日咖啡、焙度與甜點搭配 | https://www.zhanlu.com.tw/coffeedessert/ |
| 2024-12-06 | 2024-12-19 | 肯亞 AA 咖啡特色與分級入口 | https://www.zhanlu.com.tw/%e8%82%af%e4%ba%9eaa/ |
| 2024-08-29 | 2025-08-07 | 中秋禮盒與咖啡送禮情境 | https://www.zhanlu.com.tw/%e4%b8%ad%e7%a7%8b%e7%a6%ae%e7%9b%92/ |
| 2024-08-01 | 2024-08-02 | 巴拿馬翡翠莊園瑰夏沖煮注意事項 | https://www.zhanlu.com.tw/%e7%bf%a1%e7%bf%a0%e8%8e%8a%e5%9c%92%e7%91%b0%e5%a4%8fgeisha%e5%92%96%e5%95%a1/ |
| 2024-08-01 | 2024-08-02 | 巴拿馬翡翠莊園歷史、地理與生產案例 | https://www.zhanlu.com.tw/%e5%b7%b4%e6%8b%bf%e9%a6%ac%e7%bf%a1%e7%bf%a0%e8%8e%8a%e5%9c%92/ |
| 2024-06-24 | 2024-09-16 | 快速挑選喜歡的咖啡風味 | https://www.zhanlu.com.tw/%e5%a6%82%e4%bd%95%e5%bf%ab%e9%80%9f%e6%8c%91%e9%81%b8%e5%96%9c%e6%ad%a1%e7%9a%84%e5%92%96%e5%95%a1/ |
| 2024-02-29 | 2026-04-13 | 手沖入門、比例、義式與手沖差異 | https://www.zhanlu.com.tw/%e6%89%8b%e6%b2%96%e5%92%96%e5%95%a1-2/ |
| 2024-02-29 | 2025-11-04 | 濾掛式咖啡拿鐵做法 | https://www.zhanlu.com.tw/%e6%bf%be%e6%8e%9b%e5%bc%8f%e5%92%96%e5%95%a1%e6%8b%bf%e9%90%b5/ |
| 2024-02-16 | 2024-02-16 | 拿鐵比例與不同拿鐵飲品 | https://www.zhanlu.com.tw/%e6%8b%bf%e9%90%b5%e6%af%94%e4%be%8b/ |

## 建議拆分方向

- `06_沖煮/`：濾掛沖泡、手沖比例、美式咖啡、黑咖啡、拿鐵與義式/手沖比較。
- `05_烘焙/`：深焙與淺焙差異、焙度與甜點搭配、焙度選豆。
- `08_感官/`：酸質、風味描述、咖啡與堅果/甜點搭配、風味選擇流程。
- `02_產區/`：哥斯大黎加、肯亞、巴拿馬翡翠莊園等產區與案例。
- `03_品種/`：瑰夏/Geisha、咖啡豆種類與品種入門。
- `04_處理法/`：蜜處理、處理法如何影響選豆與風味。
- `11_QA/`：建立濾掛不好喝、新手選豆、手沖入門、拿鐵比例等長答。
- `12_FAQ/`：建立濾掛、黑咖啡、美式、咖啡因、焙度、咖啡禮盒等短答。
- `16_產品知識/`：文章中的商品推薦、熱銷排行、V.21、禮盒與濾掛產品需回連到商品頁再查證。

## 使用限制

- 此檔案只作為來源索引，不作為正式知識文章。
- 此分類是品牌內容與內容行銷頁，適合教學語彙與顧客問題整理，不宜單獨作為科學或健康結論。
- 健康、咖啡因、攝取量內容需搭配醫學或官方健康來源。
- 商品推薦、熱銷排行、節慶禮盒、價格、庫存與活動資訊會變動，回答前必須重新查證。
- 不要直接複製文章全文；需整理為 Coffee_RAG 的文章格式並保留來源。

## 來源

- [湛盧咖啡生活誌](https://www.zhanlu.com.tw/category/coffeelife/)，讀取日期：2026-06-30。
- [湛盧 WordPress category API, slug coffeelife](https://www.zhanlu.com.tw/wp-json/wp/v2/categories?slug=coffeelife)，讀取日期：2026-06-30。
- [湛盧 WordPress posts API, category 687](https://www.zhanlu.com.tw/wp-json/wp/v2/posts?categories=687)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`00_來源資料/011_simple_kaffa_興波文化來源.md`
---

---
title: Simple Kaffa 興波文化來源
category: 00_來源資料
type: source_catalog
tags: [source, blog, simple-kaffa, brewing, hand-pour, drip-bag, gold-cup, equipment, storage, sensory, tier-c, needs-review]
status: review
updated: 2026-06-30
source_url: https://simplekaffa.com/journal/category/1
accessed: 2026-06-30
sources:
  - type: web
    title: Simple Kaffa Journal category 1
    url: https://simplekaffa.com/journal/category/1
    accessed: 2026-06-30
---

# Simple Kaffa 興波文化來源

## 摘要

這個來源是 Simple Kaffa 興波咖啡 Journal 的「興波文化」頁面，頁面內的分類標示為「咖啡專欄」。內容集中在手沖咖啡、掛耳包沖煮、沖煮架構與參數、金杯理論、咖啡豆保存，以及興波雙環分水器等器具。

本知識庫於 `2026-06-30` 讀取分類頁。頁面 title 為「興波咖啡 Simple Kaffa | 喝杯世界級的咖啡」，description 描述 Simple Kaffa 從地方咖啡車到世界冠軍，並希望讓更多人喝到好咖啡。此頁是靜態 HTML 結構，本輪未找到可直接讀取的文章 API。

此來源屬於 Tier C 品牌內容與專家教學語彙。由於 Simple Kaffa 與世界咖啡競賽脈絡相關，內容具有高實務參考價值；但金杯理論、萃取率、沖煮參數等科學或標準化主題仍需搭配 SCA Brewing Research、SCA Coffee Brewing Handbook 或其他研究來源交叉查證。

## 可用資料

來源頁可用資訊包含：

- 分類 URL：`https://simplekaffa.com/journal/category/1`。
- 頁面主標：Journal。
- 分類區塊：興波文化。
- 分類導覽：ALL 全部文章、咖啡專欄、活動資訊、媒體報導、SHOP LIST 門市總覽。
- 商品導覽：競賽式烘焙、淺烘焙咖啡豆、中深烘焙咖啡豆、禮盒、散裝掛耳、掛耳包、周邊、課程。
- 文章卡欄位：日期、標題、文章 URL、短摘要、圖片 URL。
- 頁面列出文章數：8 篇。
- 文章日期範圍：`2013-02-02` 到 `2021-09-18`。

## 文章或素材清單

以下是分類頁列出的 8 篇文章。為避免大量搬運來源文字，`主題摘要` 使用本知識庫自行整理的短描述。

| date | 主題摘要 | url |
| --- | --- | --- |
| 2021-09-18 | 興波雙環分水器與手沖注水模式 | https://simplekaffa.com/journal/simple-kaffa-drip-shower |
| 2021-06-30 | 咖啡豆保存與包裝細節 | https://simplekaffa.com/journal/simple-kaffa-how-to-keep-coffee-beans-fresh |
| 2020-09-29 | Simple Kaffa 手沖咖啡教學 | https://simplekaffa.com/journal/simple-kaffa-how-to-hand-brewed-coffee-tutorial |
| 2020-06-03 | 手沖架構、大參數、小參數與沖煮調整 | https://simplekaffa.com/journal/%E6%89%8B%E6%B2%96%E8%AA%BF%E6%95%B4%E6%95%99%E5%AD%B8 |
| 2020-03-27 | 掛耳包沖煮教學 | https://simplekaffa.com/journal/simple-kaffa-how-to-dripcoffee-tutorial |
| 2013-02-14 | 金杯理論與粉量對風味強弱的影響 | https://simplekaffa.com/journal/bergs-coffee-gold-cup-3 |
| 2013-02-03 | 金杯理論與萃取率對味道走向的影響 | https://simplekaffa.com/journal/bergs-coffee-gold-cup-2 |
| 2013-02-02 | 金杯理論與萃取控制圖表入門 | https://simplekaffa.com/journal/bergs-coffee-gold-cup-1 |

## 主題地圖

| 主題 | 可拆到 | RAG 用途 |
| --- | --- | --- |
| 金杯理論 | `06_沖煮`, `08_感官` | 萃取率、濃度、粉量、風味走向與味覺調整 |
| 手沖咖啡 | `06_沖煮` | 手沖流程、參數架構、沖煮調整 |
| 掛耳包沖煮 | `06_沖煮`, `16_產品知識` | 掛耳包教學、顧客 FAQ、產品使用說明 |
| 咖啡豆保存 | `05_烘焙`, `16_產品知識` | 包裝、新鮮度、保存條件 |
| 分水器 | `07_設備`, `06_沖煮` | 手沖輔助器具、注水方式、萃取穩定 |
| Simple Kaffa 品牌脈絡 | `15_案例`, `10_創業` | 世界冠軍品牌、內容行銷與產品教育案例 |

## 建議拆分方向

- `06_沖煮/`：建立金杯理論、萃取控制圖、手沖參數架構、掛耳包沖泡、粉量與風味強弱等文章。
- `07_設備/`：建立分水器、手沖輔助器具與注水控制工具條目。
- `05_烘焙/`：建立咖啡豆保存、包裝、風味衰退與新鮮度條目。
- `08_感官/`：建立萃取率與味道走向、濃淡強弱、過萃與萃取不足的感官描述。
- `11_QA/`：建立「手沖怎麼調參數」「掛耳包怎麼沖」「金杯理論是什麼」「咖啡豆怎麼保存」等長答。
- `12_FAQ/`：建立金杯理論、手沖參數、掛耳包、分水器、咖啡保存的短答。
- `16_產品知識/`：若拆掛耳包與分水器產品使用說明，需回到商品頁確認規格、售價與庫存。
- `15_案例/`：建立 Simple Kaffa 作為世界冠軍咖啡品牌與知識內容經營案例。

## 使用限制

- 此檔案只作為來源索引，不作為正式知識文章。
- 此來源是品牌內容與專家教學語彙，不是官方標準文件。
- 金杯理論、萃取率與沖煮控制圖等主題需搭配 SCA 或研究來源交叉查證。
- 商品、課程、門市、價格與庫存資訊會變動，回答使用者前必須重新查證。
- 不要直接複製文章全文；需整理為 Coffee_RAG 的文章格式並保留來源。

## 來源

- [Simple Kaffa Journal 咖啡專欄](https://simplekaffa.com/journal/category/1)，讀取日期：2026-06-30。


---
### 📄 來源檔案：`01_咖啡歷史/README.md`
---

---
title: 咖啡歷史
category: 01_咖啡歷史
type: index
tags: [coffee-history]
status: draft
updated: 2026-06-30
sources: []
---

# 咖啡歷史

## 範圍

整理咖啡從起源、傳播、商業化到現代精品咖啡文化的演變。

## 優先主題

- `001_咖啡起源.md`
- `002_咖啡如何傳到世界各地.md`
- `003_台灣咖啡史.md`
- `004_第三波咖啡.md`
- `005_精品咖啡的形成.md`

## 收錄原則

- 歷史時間線需要來源。
- 傳說、民間故事、可考資料要分開寫。
- 不確定年代需標記待查證。



---
### 📄 來源檔案：`02_產區/README.md`
---

---
title: 產區
category: 02_產區
type: index
tags: [origin]
status: draft
updated: 2026-06-30
sources: []
---

# 產區

## 範圍

整理咖啡生產國、區域、海拔、氣候、處理方式、常見風味與代表性。

## 優先主題

- `001_衣索比亞.md`
- `002_巴西.md`
- `003_哥倫比亞.md`
- `004_瓜地馬拉.md`
- `005_肯亞.md`
- `006_哥斯大黎加.md`
- `007_巴拿馬.md`
- `008_印尼.md`

## 收錄原則

- 產區風味描述要避免絕對化。
- 同一國家內不同區域差異很大時，拆成獨立文章。
- 最新產量、價格、競賽資料需查證。



---
### 📄 來源檔案：`03_品種/README.md`
---

---
title: 品種
category: 03_品種
type: index
tags: [variety]
status: draft
updated: 2026-06-30
sources: []
---

# 品種

## 範圍

整理咖啡物種、品種、栽培品系、常見命名與風味相關討論。

## 優先主題

- `001_阿拉比卡.md`
- `002_羅布斯塔.md`
- `003_藝伎.md`
- `004_波旁.md`
- `005_鐵比卡.md`
- `006_SL28.md`
- `007_卡杜拉.md`
- `008_卡杜艾.md`

## 收錄原則

- 物種、品種、品系要分清楚。
- 品種與風味的關係不能寫成單一因果。
- 若涉及基因、抗病性、產量，需來源。



---
### 📄 來源檔案：`04_處理法/README.md`
---

---
title: 處理法
category: 04_處理法
type: index
tags: [processing]
status: draft
updated: 2026-06-30
sources: []
---

# 處理法

## 範圍

整理咖啡果實採收後到生豆乾燥完成前的處理流程與風味影響。

## 優先主題

- `001_水洗處理.md`
- `002_日曬處理.md`
- `003_蜜處理.md`
- `004_厭氧發酵.md`
- `005_濕刨法.md`
- `006_二氧化碳浸漬.md`

## 收錄原則

- 流程、風味影響、風險分開寫。
- 特殊發酵法要避免過度神化。
- 不同莊園自定義名稱需標明來源。



---
### 📄 來源檔案：`05_烘焙/README.md`
---

---
title: 烘焙
category: 05_烘焙
type: index
tags: [roasting]
status: draft
updated: 2026-06-30
sources: []
---

# 烘焙

## 範圍

整理烘豆過程中的熱能控制、烘焙度、曲線、瑕疵與保存。

## 優先主題

- `001_烘焙度.md`
- `002_一爆.md`
- `003_發展時間.md`
- `004_梅納反應.md`
- `005_烘焙瑕疵.md`
- `006_咖啡豆保存.md`

## 收錄原則

- 避免只用顏色判斷烘焙度。
- 若涉及化學反應，需來源。
- 實務建議要和理論解釋分開。



---
### 📄 來源檔案：`06_沖煮/README.md`
---

---
title: 沖煮
category: 06_沖煮
type: index
tags: [brewing]
status: draft
updated: 2026-06-30
sources: []
---

# 沖煮

## 範圍

整理手沖、義式、浸泡式與其他萃取方法中的變因、配方與調整邏輯。

## 優先主題

- `001_粉水比.md`
- `002_研磨度.md`
- `003_水溫.md`
- `004_萃取率.md`
- `005_手沖基本流程.md`
- `006_義式濃縮基礎.md`
- `007_冷萃咖啡.md`

## 收錄原則

- 配方需寫清楚粉量、水量、時間、研磨、器具。
- 調整邏輯要說明原因。
- 不同器具的細節可連到 `07_設備/`。



---
### 📄 來源檔案：`07_設備/README.md`
---

---
title: 設備
category: 07_設備
type: index
tags: [equipment]
status: draft
updated: 2026-06-30
sources: []
---

# 設備

## 範圍

整理咖啡製作、量測、保存、營運會用到的器具與設備。

## 優先主題

- `001_磨豆機.md`
- `002_濾杯.md`
- `003_電子秤.md`
- `004_溫控壺.md`
- `005_義式咖啡機.md`
- `006_烘豆機.md`
- `007_TDS測量.md`

## 收錄原則

- 選購建議需分使用情境。
- 型號、價格、規格必須查證。
- 不做未經來源支持的品牌排名。



---
### 📄 來源檔案：`08_感官/README.md`
---

---
title: 感官
category: 08_感官
type: index
tags: [sensory]
status: draft
updated: 2026-06-30
sources: []
---

# 感官

## 範圍

整理咖啡品飲、杯測、風味描述、香氣、酸質、甜感、口感與訓練方式。

## 優先主題

- `001_杯測.md`
- `002_風味輪.md`
- `003_酸質.md`
- `004_甜感.md`
- `005_苦味.md`
- `006_口感.md`
- `007_香氣.md`

## 收錄原則

- 感官描述要避免絕對化。
- 主觀品飲與可訓練方法要分開。
- 若引用 SCA 或其他標準，需來源。



---
### 📄 來源檔案：`09_開店/README.md`
---

---
title: 開店
category: 09_開店
type: index
tags: [cafe-operation]
status: draft
updated: 2026-06-30
sources: []
---

# 開店

## 範圍

整理咖啡店從籌備、選址、菜單、吧台、SOP 到日常營運的實務知識。

## 優先主題

- `001_開店定位.md`
- `002_選址.md`
- `003_菜單設計.md`
- `004_吧台動線.md`
- `005_人員訓練.md`
- `006_營運SOP.md`
- `007_庫存管理.md`

## 收錄原則

- 實務建議要能轉成清單。
- 成本與法規必須查證。
- 不同店型需分開討論。



---
### 📄 來源檔案：`10_創業/README.md`
---

---
title: 創業
category: 10_創業
type: index
tags: [business]
status: draft
updated: 2026-06-30
sources: []
---

# 創業

## 範圍

整理咖啡相關創業的商業模式、品牌、財務、產品、通路與成長策略。

## 優先主題

- `001_商業模式.md`
- `002_成本結構.md`
- `003_品牌定位.md`
- `004_定價策略.md`
- `005_行銷漏斗.md`
- `006_會員經營.md`
- `007_產品線設計.md`

## 收錄原則

- 創業內容要區分假設、案例、可驗證數據。
- 財務資料必須標示來源或計算假設。
- 不給保證式建議。



---
### 📄 來源檔案：`11_QA/README.md`
---

---
title: QA
category: 11_QA
type: index
tags: [qa, customer-service]
status: draft
updated: 2026-06-30
sources: []
---

# QA

## 範圍

整理長答型問題，適合客服、教學、RAG 回答或內容改寫。

## 優先主題

- `001_新手該如何選咖啡豆.md`
- `002_咖啡為什麼會酸.md`
- `003_手沖為什麼忽濃忽淡.md`
- `004_咖啡豆要不要放冰箱.md`
- `005_義式咖啡和手沖差在哪.md`

## 收錄原則

- 先給短答，再給詳解。
- 回答要能連回知識文章。
- 不確定或情境差異大時，明確寫出條件。



---
### 📄 來源檔案：`12_FAQ/README.md`
---

---
title: FAQ
category: 12_FAQ
type: index
tags: [faq, customer-service]
status: draft
updated: 2026-06-30
sources: []
---

# FAQ

## 範圍

整理短答型常見問題，適合網站、客服、自動回覆或課程前導。

## 優先主題

- `001_咖啡豆可以保存多久.md`
- `002_手沖需要哪些器具.md`
- `003_深焙是不是比較苦.md`
- `004_咖啡因含量怎麼比較.md`
- `005_拿鐵和卡布奇諾差在哪.md`

## 收錄原則

- 每題答案短而清楚。
- 不展開長篇論述，必要時連到 QA 或文章。
- 避免過度承諾。



---
### 📄 來源檔案：`13_圖片/README.md`
---

---
title: 圖片
category: 13_圖片
type: index
tags: [image_asset]
status: draft
updated: 2026-06-30
sources: []
---

# 圖片

## 範圍

整理圖片素材的描述、授權、來源、可用場景與關聯文章。

## 優先主題

- `001_手沖流程圖片.md`
- `002_咖啡豆近照.md`
- `003_吧台工作照.md`
- `004_產區地圖.md`
- `005_杯測桌面.md`

## 收錄原則

- 必須記錄授權狀態。
- 沒有明確授權的圖片不得標記為可商用。
- 圖片描述要可供搜尋與無障礙替代文字使用。



---
### 📄 來源檔案：`14_影片/README.md`
---

---
title: 影片
category: 14_影片
type: index
tags: [video_asset]
status: draft
updated: 2026-06-30
sources: []
---

# 影片

## 範圍

整理影片素材的摘要、逐字稿、片段、授權、來源與可用場景。

## 優先主題

- `001_手沖教學影片.md`
- `002_咖啡店訪談影片.md`
- `003_烘豆過程影片.md`
- `004_杯測教學影片.md`
- `005_品牌故事影片.md`

## 收錄原則

- 需要記錄來源與授權。
- 若有逐字稿，應拆成可引用段落。
- 片段時間碼要精準。



---
### 📄 來源檔案：`15_案例/README.md`
---

---
title: 案例
category: 15_案例
type: index
tags: [case]
status: draft
updated: 2026-06-30
sources: []
---

# 案例

## 範圍

整理咖啡店、品牌、產品、活動、內容企劃、顧客故事與營運實驗。

## 優先主題

- `001_咖啡店開店案例.md`
- `002_外帶咖啡品牌案例.md`
- `003_手沖課程案例.md`
- `004_社群內容企劃案例.md`
- `005_會員經營案例.md`

## 收錄原則

- 案例要分清楚背景、問題、做法、結果。
- 未經來源確認的成效數據必須標示待查。
- 洞察要能回連到開店或創業文章。



---
### 📄 來源檔案：`16_產品知識/README.md`
---

---
title: 產品知識
category: 16_產品知識
type: index
tags: [product, green-bean, supplier, inventory]
status: draft
updated: 2026-06-30
sources: []
---

# 產品知識

## 範圍

整理咖啡產品、供應商資料、庫存頁、品項規格、產品頁連結與銷售問答。

## 優先主題

- `001_haru_coffee_生豆庫存來源.md`
- `002_生豆品項欄位說明.md`
- `003_產品諮詢回答規則.md`
- `004_生豆庫存查證流程.md`

## 收錄原則

- 庫存、價格、供貨狀態都屬於會變動的資訊，使用前必須回到來源查證。
- 來源頁沒有明確定義的符號，不自行解讀。
- 產品品名可保留中英雙語，方便搜尋與 RAG 檢索。
- 若品項同時涉及產區、處理法、品種，使用內部連結串接，不在產品頁重寫完整百科內容。



---
### 📄 來源檔案：`16_產品知識/001_haru_coffee_生豆庫存來源.md`
---

---
title: HARU COFFEE 生豆庫存來源
category: 16_產品知識
type: product_knowledge
tags: [product, green-bean, supplier, inventory, haru-coffee, needs-review]
status: review
updated: 2026-06-30
source_url: https://harucafe.com.tw/stocktw/
source_updated: 2026-06-25T15:53:57+08:00
accessed: 2026-06-30
sources:
  - type: web
    title: 生豆庫存｜咖啡生豆 | 守成咖啡HARU COFFEE
    url: https://harucafe.com.tw/stocktw/
    accessed: 2026-06-30
---

# HARU COFFEE 生豆庫存來源

## 摘要

這個來源是守成咖啡 HARU COFFEE 的生豆庫存頁，可作為產品知識、供應商品項、產區品名、處理法與包裝規格的參考。

頁面 meta 顯示修改時間為 `2026-06-25T15:53:57+08:00`。本知識庫於 `2026-06-30` 讀取頁面。

庫存資訊屬於會變動的資料。若用於銷售、採購或客服回答，必須先回到原始頁面或人工確認最新狀態。

## 可用欄位

來源頁表格欄位包含：

- `NO.`：品項編號。
- `Country`：國家或來源地。
- `Grade`：等級。
- `Item`：品名，通常包含中文與英文名稱。
- `Process`：處理法。
- `Package`：包裝規格。
- `Stock`：庫存欄位。

## 頁面觀察

本次讀取到的唯一品項數為 128 筆。

來源頁使用 `x` 與空白呈現庫存欄位，但頁面截取內容未明確定義符號意義。因此知識庫不得自行把 `x` 解讀為有貨或缺貨。

本次讀取到的品項來源國或來源地包含 21 種：Ethiopia、Panama、Brasil、Kenya、Costa Rica、Guatemala、El Salvador、Colombia、Indonesia、Uganda、Yemen、Tanzania、Nicaragua、Ecuador、India、Austria、Jamaica、Hawaii、Timor、Japan、England。

本次讀取到的處理法欄位包含：Washed、Natural、Honey、Semi Washed、Anaerobic Natural、Anaerobic Honey、Other，以及空白欄位。

## 代表品項

以下只作為來源結構樣例，不代表完整庫存，也不代表目前可供貨。

| 編號 | Country | Grade | Item | Process | Package | Stock |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Ethiopia | G1 | 衣索比亞 耶加雪夫 哈洛巴 G1 水洗 / Ethiopia Yirgacheffe Halo Bariti G1 Washed | Washed | 30kg(Grainpro bag) | x |
| 10 | Ethiopia | G1 | 衣索比亞 藝妓村 蓋里區 伊魯森林 水洗-綠標 / Ethiopia Gesha Village Gaylee Illubabor Forest Washed-SINGLE TERROIR | Washed | 30kg(Vaccum) | x |
| 23 | Kenya | AA TOP | 肯亞 奇恩杜 AA TOP / Kenya Kiandu AA TOP | Washed | 30kg(Vaccum) |  |
| 36 | Yemen |  | 葉門 哈拉茲：迦瑪小農 蜜處理 / Yemen Haraz：Jarma Honey | Honey | 10kg(Vaccum) | x |
| 45 | Panama | SHB | 蕾莉妲莊園 “紅玉谷” 卡杜依 水洗 / Finca Lerida “Ruby Ridge” Catuai Washed | Washed | 22.6kg(Vaccum) |  |
| 51 | Panama | SHB | 悅境莊園 藝妓 蜜處理 / Finca Las Delicias Geisha Honey | Honey | 15kg(Vaccum) | x |
| 73 | Costa Rica | SHB | 拉斯拉哈斯莊園 薇拉羅伯斯 黑鑽 日曬 / Finca Las Lajas Villalobos Black Diamond Natural | Natural | 30kg(Vaccum) | x |
| 85 | Guatemala | SHB | 拉米尼塔 安堤瓜 花神 PB / La Minita Antiqua La Flor PB | Washed | 30kg(Grainpro bag) | x |
| 101 | Colombia | Supremo | 哥倫比亞 薇拉 Supremo / Colombia Huila Supremo Sc 17/18 | Washed | 35kg(Grainpro bag) |  |
| 117 | Indonesia | G1-TP | 印尼 P.W.N 黃金曼特寧 半水洗 三次手選 / Indonesia P.W.N Golden Mandheling Semi Washed TP | Semi Washed | 30kg(Grainpro bag) | x |
| 125 | Austria |  | ISI 不鏽鋼奶油發泡槍 0.5L / ISI Cream Profi Whip Stainless Steel |  | 6/Box |  |
| 128 | England |  | 鍍銀寬口杯測匙 / Silver Plated Cupping Spoon |  | MOQ: 1 |  |

## 產品知識整理規則

- 若要建立單一品項文章，使用 `16_產品知識` 的產品模板。
- 品名保留中文與英文，方便搜尋。
- `Country` 可連到 `02_產區/`，但不要在產品文章內重寫完整產區百科。
- `Process` 可連到 `04_處理法/`，但不要在產品文章內重寫完整處理法百科。
- `Package` 可作為採購或倉儲資訊，但使用前需回源確認。
- `Stock` 不可直接拿來回答有貨或缺貨，除非先確認來源頁符號定義與最新狀態。

## 後續任務

- 建立 `002_生豆品項欄位說明.md`，定義 Country、Grade、Item、Process、Package、Stock 的使用方式。
- 建立 `003_產品諮詢回答規則.md`，規範客服如何回答產品與庫存問題。
- 從代表品項中挑 10 筆建立單一產品 Markdown。
- 將 Country 對應到 `02_產區/` 的產區文章。
- 將 Process 對應到 `04_處理法/` 的處理法文章。

## 來源

- [生豆庫存｜咖啡生豆 | 守成咖啡HARU COFFEE](https://harucafe.com.tw/stocktw/)，讀取日期：2026-06-30，頁面 meta 修改時間：2026-06-25T15:53:57+08:00。

