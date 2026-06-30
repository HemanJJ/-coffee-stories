---
name: coffee-knowledge-system
description: Maintain and expand a professional Markdown coffee knowledge base. Use when ingesting coffee URLs, building Coffee_RAG source catalogs, creating coffee articles/QA/FAQ, designing evidence tiers, or turning industry news, brewing science, sensory research, education resources, product pages, and coffee business material into structured RAG-ready Markdown.
---

# Coffee Knowledge System

## Core Workflow

1. Read `Coffee_RAG/AGENTS.md`, `_source_policy.md`, `_taxonomy.md`, `_style_guide.md`, `_queue.md`, and `_index.md` before changing the knowledge base.
2. For each new URL, create or update a `00_來源資料/NNN_來源名稱.md` source catalog first. Do not skip directly to a final article unless the source is already cataloged.
3. Record title, URL, accessed date, published/modified dates when available, source type, usable metadata, topic map, limitations, and suggested target folders.
4. Convert sources into domain articles only after source context is clear. Keep one article per topic.
5. Update `_index.md` for new files and `_queue.md` for follow-up work.
6. Validate local Markdown links and scan the changed keywords before finishing.

## Evidence Tiers

Use the strongest available source and label uncertainty.

| Tier | Source type | Typical use |
| --- | --- | --- |
| A | Official organizations, research bodies, standards, peer-reviewed papers | Definitions, standards, protocols, scientific claims |
| B | Professional trade media and expert publications | Industry trends, equipment/news context, business developments |
| C | Coffee schools, roasters, brands, product pages, blogs | Practical education, product vocabulary, examples, local market language |
| D | Forums, social posts, unverified summaries | Only as leads or customer-language examples |

Rules:

- Prefer Tier A for brewing science, sensory standards, value assessment, health, safety, and grading systems.
- Use Tier B for current market movement, cafe culture, and industry news; re-check dates before answering.
- Use Tier C for teaching language, product examples, and operational details; do not treat prices, stock, claims, or recommendations as stable.
- Avoid Tier D unless the task specifically asks for community sentiment.

Read `references/authority-sources.md` when selecting authoritative coffee sources or building a reading plan.

## Classification

Map every source into one or more folders:

- `01_咖啡歷史`: history, culture, origin stories, institutional context.
- `02_產區`: country, region, farm, estate, terroir, altitude, climate.
- `03_品種`: species, cultivar, variety, mutation, bean type.
- `04_處理法`: washed, natural, honey, wet-hulled, anaerobic, fermentation.
- `05_烘焙`: roast level, roast curves, defects, freshness, storage.
- `06_沖煮`: recipes, extraction, water, grinder, espresso, filter, immersion.
- `07_設備`: brewers, grinders, espresso machines, roasters, measurement tools.
- `08_感官`: cupping, flavor wheel, lexicon, acidity, sweetness, body, aftertaste.
- `09_開店`: cafe operations, menu, layout, staffing, SOP.
- `10_創業`: business model, cost, branding, market, finance.
- `11_QA`: long-form answers.
- `12_FAQ`: short answers.
- `15_案例`: farms, brands, cafes, competitions, supply-chain cases.
- `16_產品知識`: product pages, inventory, SKUs, sales questions.

## Writing Rules

- Use Traditional Chinese by default.
- Summarize and restructure; do not copy full articles.
- Keep volatile data out of stable articles unless dated and sourced.
- For science claims, separate "source says" from "Coffee_RAG inference".
- For product or brand material, write "可作為產品語彙/案例參考" unless independently verified.
- For recommendations that affect spending, re-check current source pages.
- Keep sources in frontmatter and a human-readable `## 來源` section.

## Validation

Before finishing:

- Run the local Markdown link check.
- Run `rg` for the new source name, slug, and main topic.
- Check `git status --short Coffee_RAG`.
- Mention any failed fetches, timeouts, or unverified claims in the final response.
