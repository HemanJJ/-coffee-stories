#!/usr/bin/env python3
"""Search YouTube topics and export a sheet-ready CSV.

This script uses the official YouTube Data API v3 instead of scraping
search pages. It is meant to help build a reusable topic library for
story research, especially around gentle human themes like companionship,
returning home, forgiveness, and new beginnings.
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import random
import re
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen


YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"
OLLAMA_URL = "http://127.0.0.1:11434/api/generate"
DEFAULT_QUERY_FILE = Path(__file__).with_name("topic_queries.txt")
DEFAULT_ENV_FILE = Path(__file__).resolve().parents[1] / ".env"
VIDEO_ID_PATTERN = re.compile(r"^[A-Za-z0-9_-]{11}$")

INTENT_QUERY_TERMS = {
    "object": ["家書", "老照片", "舊物", "錄音", "日記", "遺物"],
    "family": ["父親", "母親", "外公", "外婆", "家庭", "家人"],
    "home": ["回家", "故鄉", "離家", "返鄉"],
    "care": ["陪伴", "等待", "守候", "守望", "在場", "照顧者", "陪病", "長照"],
    "restart": ["重新開始", "中年", "轉職", "人生下半場"],
    "dialect": ["方言", "台語", "客語", "潮汕話", "家族記憶"],
}

POSITIVE_TERMS = {
    "訪談": 3,
    "專訪": 3,
    "人物故事": 4,
    "生命故事": 4,
    "小人物": 3,
    "紀錄": 3,
    "紀實": 3,
    "紀錄片": 4,
    "微紀錄片": 4,
    "調查報告": 3,
    "陪伴": 2,
    "等待": 2,
    "守候": 2,
    "守望": 2,
    "在場": 2,
    "回家": 2,
    "重新開始": 3,
    "重啟": 2,
    "告白": 1,
    "一個人": 2,
    "外公": 2,
    "父親": 2,
    "母親": 2,
    "家屬": 2,
    "告別": 2,
    "記憶": 2,
    "失去": 2,
    "想念": 2,
    "回憶": 2,
    "家書": 3,
    "家书": 3,
    "書信": 3,
    "书信": 3,
    "信件": 3,
    "老照片": 3,
    "舊照片": 3,
    "旧照片": 3,
    "照片": 2,
    "錄音": 3,
    "录音": 3,
    "日記": 2,
    "日记": 2,
    "老物件": 3,
    "舊物": 3,
    "旧物": 3,
    "遺物": 3,
    "遗物": 3,
    "方言": 2,
    "台語": 2,
    "台语": 2,
    "客語": 2,
    "客语": 2,
    "潮汕話": 2,
    "潮汕话": 2,
    "相遇": 1,
    "成長": 1,
}

NEGATIVE_TERMS = {
    "shorts": -5,
    "short": -3,
    "lyric": -8,
    "lyrics": -8,
    "歌詞": -8,
    "歌词": -8,
    "動態歌詞": -8,
    "动态歌词": -8,
    "歌曲": -7,
    "原創歌曲": -8,
    "原创歌曲": -8,
    "翻唱": -6,
    "cover": -6,
    "看哭": -4,
    "催淚": -3,
    "爆哭": -4,
    "哭慘": -4,
    "潸然淚下": -4,
    "必看": -2,
    "精彩片段": -3,
    "reaction": -3,
    "懶人包": -2,
    "八卦": -4,
    "直播": -3,
    "live": -3,
    "新聞": -4,
    "新聞台": -5,
    "大現場": -5,
    "政論": -5,
    "政治人物": -6,
    "選舉": -5,
    "政治": -5,
    "毛澤東": -8,
    "毛泽东": -8,
    "佛教": -7,
    "法師": -7,
    "法师": -7,
    "和尚": -7,
    "僧人": -7,
    "佛陀": -7,
    "禪修": -6,
    "禅修": -6,
    "寺廟": -6,
    "寺庙": -6,
    "講經": -6,
    "讲经": -6,
    "成果": -3,
    "成果紀錄": -4,
    "精華版": -3,
    "完整版": -1,
    "品牌重塑": -5,
    "品牌": -3,
    "集團": -3,
    "同仁": -2,
    "企業": -3,
    "課程": -4,
    "课程": -4,
    "畢業生訪談": -5,
    "毕业生访谈": -5,
    "原力生命故事": -6,
    "原力創造": -6,
    "原力创造": -6,
    "論壇": -2,
    "宣傳": -4,
    "mv": -5,
    "主題曲": -5,
    "純享版": -5,
    "纯享版": -5,
    "片段": -4,
    "合唱": -3,
    "配樂": -4,
    "配乐": -4,
    "風華合伙人": -5,
    "风华合伙人": -5,
    "主持人": -4,
    "節目": -4,
    "节目": -4,
    "藝人": -6,
    "艺人": -6,
    "明星": -6,
    "女星": -6,
    "男星": -6,
    "演員": -5,
    "演员": -5,
    "歌手": -5,
    "偶像": -5,
    "曾寶儀": -8,
    "曾宝仪": -8,
    "張頌文": -8,
    "张颂文": -8,
    "狂飆": -8,
    "狂飙": -8,
    "娛樂人物": -6,
    "娱乐人物": -6,
    "告別式": -5,
    "告别式": -5,
    "告別典禮": -6,
    "告别典礼": -6,
    "追思": -5,
    "紀念影片": -4,
    "生命影片": -5,
    "紀錄片頭": -5,
    "纪录片头": -5,
    "apple daily": -6,
    "蘋果日報": -6,
    "苹果日报": -6,
    "果籽": -5,
    "飲食男女": -5,
    "饮食男女": -5,
    "原刊日期": -5,
    "ep": -4,
    "cut": -5,
    "霸总": -6,
    "霸總": -6,
    "女主": -5,
    "原创歌曲": -6,
    "原創歌曲": -6,
    "vlog": -5,
    "釣魚": -8,
    "釣查": -8,
    "飛釣": -8,
    "小物釣": -8,
    "flyfishing": -8,
    "fishing": -8,
    "生態釣查": -8,
    "原生魚": -7,
    "該怎麼辦": -5,
    "跟蹤": -6,
    "生活技巧": -5,
    "服貿": -6,
    "柯文哲": -6,
    "賴清德": -6,
    "民進黨": -6,
    "國民黨": -6,
    "外星人": -8,
    "靈異": -8,
    "灵异": -8,
    "靈魂": -7,
    "灵魂": -7,
    "測驗": -7,
    "测验": -7,
    "業力": -7,
    "业力": -7,
    "療癒": -4,
    "疗愈": -4,
    "羅斯威爾": -8,
    "罗斯威尔": -8,
    "濫賭": -8,
    "滥赌": -8,
    "賭鬼": -8,
    "赌鬼": -8,
    "老王說": -6,
    "活俠傳": -8,
    "活侠传": -8,
}

SEARCH_EXCLUDE_TERMS = [
    "shorts",
    "short",
    "直播",
    "live",
    "新聞",
    "新聞台",
    "政論",
    "政治人物",
    "選舉",
    "服貿",
    "柯文哲",
    "賴清德",
    "民進黨",
    "國民黨",
    "毛澤東",
    "毛泽东",
    "佛教",
    "法師",
    "法师",
    "和尚",
    "僧人",
    "佛陀",
    "禪修",
    "禅修",
    "寺廟",
    "寺庙",
    "MV",
    "主題曲",
    "纯享版",
    "純享版",
    "主持人",
    "節目",
    "节目",
    "藝人",
    "艺人",
    "明星",
    "女星",
    "男星",
    "演員",
    "演员",
    "曾寶儀",
    "曾宝仪",
    "張頌文",
    "张颂文",
    "狂飆",
    "狂飙",
    "歌手",
    "偶像",
]

NEGATIVE_CHANNEL_TERMS = {
    "新聞": -5,
    "新聞台": -6,
    "直播": -4,
    "娛樂": -3,
    "娛樂台": -5,
    "综艺": -5,
    "綜藝": -5,
    "佛教": -7,
    "法師": -7,
    "法师": -7,
    "寺": -4,
    "亮生活": -8,
    "bright side": -8,
    "玩飛釣": -8,
    "釣": -6,
}

PRIVATE_MEMORIAL_TERMS = [
    "告別式",
    "告别式",
    "告別典禮",
    "告别典礼",
    "追思",
    "生命影片",
    "紀念影片",
    "紀錄片頭",
    "纪录片头",
    "訃聞",
    "讣闻",
]

MEDIA_NOISE_TERMS = [
    "apple daily",
    "蘋果日報",
    "苹果日报",
    "果籽",
    "飲食男女",
    "饮食男女",
    "原刊日期",
    "ep",
    "cut",
    "霸总",
    "霸總",
    "女主",
    "lyric",
    "lyrics",
    "歌詞",
    "歌词",
    "動態歌詞",
    "动态歌词",
    "歌曲",
    "原创歌曲",
    "原創歌曲",
    "翻唱",
    "cover",
    "vlog",
    "釣魚",
    "釣查",
    "飛釣",
    "小物釣",
    "flyfishing",
    "fishing",
    "生態釣查",
    "原生魚",
    "該怎麼辦",
    "跟蹤",
    "生活技巧",
]

ENTERTAINMENT_TERMS = [
    "藝人",
    "艺人",
    "明星",
    "女星",
    "男星",
    "演員",
    "演员",
    "歌手",
    "偶像",
    "主持人",
    "節目",
    "节目",
    "綜藝",
    "综艺",
    "影集",
    "劇集",
    "剧集",
    "角色",
    "遊戲",
    "游戏",
    "動畫",
    "动画",
    "動漫",
    "动漫",
]


@dataclass
class TopicRow:
    rank: int
    query: str
    video_id: str
    title: str
    channel: str
    published_at: str
    duration_seconds: int
    duration_label: str
    view_count: int
    comment_count: int
    url: str
    score: int
    score_reasons: str
    source_type: str
    availability: str
    transcript_status: str
    auto_suggestion: str
    manual_status: str
    manual_note: str
    notes: str
    top_comment_excerpt: str
    description: str


def read_env_file(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def extract_json_object(text: str) -> str:
    cleaned = (text or "").strip()
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


def get_default_api_key() -> str:
    env_key = os.environ.get("YOUTUBE_API_KEY", "").strip()
    if env_key:
        return env_key
    return read_env_file(DEFAULT_ENV_FILE).get("YOUTUBE_API_KEY", "").strip()


def get_default_ollama_model() -> str:
    env_model = os.environ.get("OLLAMA_MODEL", "").strip()
    if env_model:
        return env_model
    return read_env_file(DEFAULT_ENV_FILE).get("OLLAMA_MODEL", "qwen2.5:7b").strip()


def ai_expand_hook_queries(hook: str, model: str, max_queries: int) -> tuple[list[str], str]:
    hook = hook.strip()
    if not hook:
        return [], ""

    max_queries = max(1, min(max_queries, 10))
    prompt = f"""
你是「咖啡時光廊」的 YouTube 題材搜尋策略師。

使用者今天給的 hook 是：「{hook}」。

請不要只是把 hook 塞進搜尋框。你要先理解它背後的故事意圖，再產生適合 YouTube 搜尋的查詢詞。

咖啡時光廊要找的是：
- 小人物、小故事、真實人生
- 家人、陪伴、等待、守候、回家、告別、老照片、舊物、書信、記憶
- 訪談、口述故事、紀錄片、微紀錄片、生命故事
- 有字幕或可整理成文字的內容

請避免：
- 歌曲、MV、歌詞、演唱、翻唱
- 新聞、政治人物、宗教講道、靈異、測驗、娛樂名人、劇集片段、vlog
- 太空泛的心靈雞湯詞

請產生 {max_queries} 個繁體中文 YouTube 搜尋 query。

重要：query 不是文案標題，不要寫成詩、散文或節目名稱。
query 必須像真人會在 YouTube 搜尋框輸入的詞組。

好的 query 範例：
- 高溫 工作 紀錄片
- 酷暑 獨居老人 訪談
- 熱天 外送員 生活紀錄
- 停電 夏天 家人 故事
- 長照 陪伴 夏天 紀錄片
- 中暑 家人 照顧 訪談

壞的 query 範例：
- 夏日炎炎守候家人
- 老照片中的熱浪人生
- 口述故事：熱死人的一天
- 在酷暑中守護

每個 query 以 3 到 6 個詞為宜。
每個 query 至少包含一個「真實內容類型詞」：訪談、紀錄片、微紀錄片、生活紀錄、口述故事、真實故事。
每個 query 至少包含一個「具體生活場景詞」：老人、外送員、工人、照顧者、家人、停電、長照、醫院、街友、獨居。
如果 hook 是「陪伴」，每個 query 還必須包含至少一個關係核心詞：陪伴、照顧、守候、陪病、長照、家人陪伴、照顧者。
不要只用「回家」「故事」「訪談」這種泛詞代表陪伴。
不要使用冒號、句號、破折號或完整句子。

只輸出 JSON，不要解釋：
{{
  "intent_note": "一句話說明你如何理解這個 hook",
  "queries": ["查詢一", "查詢二"]
}}
"""

    payload = json.dumps(
        {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "format": "json",
            "options": {
                "temperature": 0.55,
                "num_ctx": 4096,
                "num_predict": 900,
            },
        }
    ).encode("utf-8")

    try:
        request = Request(
            OLLAMA_URL,
            data=payload,
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(request, timeout=180) as response:
            raw_response = json.loads(response.read().decode("utf-8"))
    except Exception as exc:
        print(f"AI hook expansion unavailable, falling back to static queries: {exc}")
        return [], ""

    try:
        data = json.loads(extract_json_object(raw_response.get("response", "")))
    except json.JSONDecodeError as exc:
        print(f"AI hook expansion returned invalid JSON, falling back: {exc}")
        return [], ""

    queries: list[str] = []
    seen: set[str] = set()
    for raw_query in data.get("queries", []):
        query = re.sub(r"\s+", " ", str(raw_query)).strip()
        query = re.sub(r"[。．.!！?？:：;；,，、]+", " ", query)
        query = re.sub(r"\s+", " ", query).strip()
        if not query or query in seen:
            continue
        queries.append(query)
        seen.add(query)
        if len(queries) >= max_queries:
            break

    if queries:
        note = str(data.get("intent_note", "")).strip()
        if note:
            print(f"AI hook intent: {note}")
        print("AI-generated YouTube queries:")
        for query in queries:
            print(f"- {query}")

    return queries, str(data.get("intent_note", "")).strip()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search YouTube topics and export a Google-Sheet-ready CSV."
    )
    parser.add_argument(
        "--api-key",
        default=get_default_api_key(),
        help="YouTube Data API key. Defaults to YOUTUBE_API_KEY env var or .env.",
    )
    parser.add_argument(
        "--query",
        action="append",
        default=[],
        help="Single search query. Repeat this flag to add more queries.",
    )
    parser.add_argument(
        "--query-file",
        type=Path,
        default=DEFAULT_QUERY_FILE,
        help="UTF-8 text file with one query per line.",
    )
    parser.add_argument(
        "--hook",
        default="",
        help="Today's story direction hook, e.g. 老照片, 一封信, 等待.",
    )
    parser.add_argument(
        "--ai-expand-hook",
        action="store_true",
        help="Use local Ollama to turn --hook into intent-aware YouTube queries.",
    )
    parser.add_argument(
        "--ollama-model",
        default=get_default_ollama_model(),
        help="Local Ollama model for --ai-expand-hook. Default: OLLAMA_MODEL or qwen2.5:7b.",
    )
    parser.add_argument(
        "--max-ai-queries",
        type=int,
        default=6,
        help="Maximum AI-generated queries when --ai-expand-hook is enabled.",
    )
    parser.add_argument(
        "--intent",
        choices=sorted(INTENT_QUERY_TERMS),
        default="",
        help="Focus query set for today: object, family, home, care, restart, dialect.",
    )
    parser.add_argument(
        "--sample-queries",
        type=int,
        default=0,
        help="Randomly sample N queries after intent/hook expansion. Saves quota.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=0,
        help="Seed for --sample-queries. Default 0 means use today's date.",
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=10,
        help="Results per query to request from YouTube search.list (1-50).",
    )
    parser.add_argument(
        "--region-code",
        default="TW",
        help="ISO 3166-1 alpha-2 region code. Default: TW",
    )
    parser.add_argument(
        "--language",
        default="zh-Hant",
        help="Search relevance language. Default: zh-Hant",
    )
    parser.add_argument(
        "--order",
        choices=["relevance", "date", "viewCount"],
        default="relevance",
        help="YouTube search ordering.",
    )
    parser.add_argument(
        "--min-score",
        type=int,
        default=0,
        help="Only write rows at or above this score.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("youtube_topic_candidates.csv"),
        help="CSV output path.",
    )
    parser.add_argument(
        "--shortlist-output",
        type=Path,
        default=Path("youtube_topic_shortlist.csv"),
        help="Shortlist CSV output path.",
    )
    parser.add_argument(
        "--plan-output",
        type=Path,
        default=Path("topic_plan.md"),
        help="Markdown output path for hook interpretation and search strategy.",
    )
    parser.add_argument(
        "--report-output",
        type=Path,
        default=Path("topic_report.md"),
        help="Markdown output path for today's topic selection report.",
    )
    parser.add_argument(
        "--shortlist-min-score",
        type=int,
        default=15,
        help="Minimum score for shortlist CSV.",
    )
    parser.add_argument(
        "--max-per-channel",
        type=int,
        default=1,
        help="Maximum rows to keep per channel after scoring. Default: 1",
    )
    parser.add_argument(
        "--allow-unusable",
        action="store_true",
        help="Keep videos that are private, unlisted, live, or not embeddable.",
    )
    parser.add_argument(
        "--story-only",
        action="store_true",
        help="Keep only rows classified as story-fit after scoring.",
    )
    parser.add_argument(
        "--require-transcript",
        action="store_true",
        help="Keep only videos with a fetchable YouTube transcript/caption.",
    )
    parser.add_argument(
        "--sleep",
        type=float,
        default=0.15,
        help="Small pause between API calls.",
    )
    return parser.parse_args()


def read_queries(args: argparse.Namespace) -> list[str]:
    queries, _ = read_queries_with_plan(args)
    return queries


def read_queries_with_plan(args: argparse.Namespace) -> tuple[list[str], dict[str, str]]:
    queries: list[str] = []
    seen: set[str] = set()
    plan = {
        "hook": args.hook.strip(),
        "intent_note": "",
        "query_source": "static",
    }

    if args.hook and args.ai_expand_hook:
        query_count = args.sample_queries or args.max_ai_queries
        ai_queries, intent_note = ai_expand_hook_queries(
            args.hook,
            args.ollama_model,
            query_count,
        )
        if ai_queries:
            plan["intent_note"] = intent_note
            plan["query_source"] = "ai"
            return ai_queries, plan

    for query in args.query:
        normalized = query.strip()
        if normalized and normalized not in seen:
            queries.append(normalized)
            seen.add(normalized)

    if args.query_file.exists():
        for raw_line in args.query_file.read_text(encoding="utf-8").splitlines():
            normalized = raw_line.strip()
            if not normalized or normalized.startswith("#") or normalized in seen:
                continue
            queries.append(normalized)
            seen.add(normalized)

    if args.intent:
        intent_terms = INTENT_QUERY_TERMS[args.intent]
        queries = [
            query
            for query in queries
            if any(term in query for term in intent_terms)
        ]

    if args.hook:
        hook = args.hook.strip()
        queries = [f"{query} {hook}" for query in queries]

    if args.sample_queries and len(queries) > args.sample_queries:
        seed = args.seed or int(time.strftime("%Y%m%d"))
        sampler = random.Random(seed)
        queries = sampler.sample(queries, args.sample_queries)

    return queries, plan


def fetch_json(endpoint: str, params: dict[str, str | int]) -> dict:
    url = f"{YOUTUBE_API_BASE}/{endpoint}?{urlencode(params)}"
    try:
        with urlopen(url) as response:
            return json.loads(response.read().decode("utf-8"))
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"YouTube API HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise RuntimeError(f"Network error while calling YouTube API: {exc}") from exc


def search_videos(
    *,
    api_key: str,
    query: str,
    max_results: int,
    region_code: str,
    language: str,
    order: str,
) -> list[dict]:
    query_with_exclusions = " ".join(
        [query] + [f"-{term}" for term in SEARCH_EXCLUDE_TERMS]
    )
    payload = fetch_json(
        "search",
        {
            "key": api_key,
            "part": "snippet",
            "q": query_with_exclusions,
            "type": "video",
            "maxResults": max_results,
            "regionCode": region_code,
            "relevanceLanguage": language,
            "safeSearch": "strict",
            "videoEmbeddable": "true",
            "videoDuration": "medium",
            "order": order,
        },
    )
    return payload.get("items", [])


def fetch_video_details(api_key: str, video_ids: Iterable[str]) -> dict[str, dict]:
    video_ids = [
        video_id.strip()
        for video_id in video_ids
        if video_id and VIDEO_ID_PATTERN.fullmatch(video_id.strip())
    ]
    if not video_ids:
        return {}

    params = {
        "key": api_key,
        "part": "snippet,contentDetails,statistics,status",
        "id": ",".join(video_ids),
    }

    try:
        payload = fetch_json("videos", params)
        return {item["id"]: item for item in payload.get("items", [])}
    except RuntimeError:
        detail_map: dict[str, dict] = {}
        for video_id in video_ids:
            try:
                payload = fetch_json(
                    "videos",
                    {
                        "key": api_key,
                        "part": "snippet,contentDetails,statistics,status",
                        "id": video_id,
                    },
                )
            except RuntimeError:
                continue

            items = payload.get("items", [])
            if items:
                detail_map[video_id] = items[0]
        return detail_map


def fetch_top_comment_excerpt(api_key: str, video_id: str) -> str:
    try:
        payload = fetch_json(
            "commentThreads",
            {
                "key": api_key,
                "part": "snippet",
                "videoId": video_id,
                "maxResults": 1,
                "order": "relevance",
                "textFormat": "plainText",
            },
        )
    except RuntimeError:
        return ""

    items = payload.get("items", [])
    if not items:
        return ""

    snippet = (
        items[0]
        .get("snippet", {})
        .get("topLevelComment", {})
        .get("snippet", {})
    )
    text = normalize_description(snippet.get("textDisplay") or "")
    return text[:140]


def video_availability(detail: dict) -> tuple[bool, str]:
    if not detail:
        return False, "missing-details"

    snippet = detail.get("snippet", {})
    status = detail.get("status", {})

    privacy_status = status.get("privacyStatus", "")
    embeddable = status.get("embeddable")
    upload_status = status.get("uploadStatus", "")
    live_content = snippet.get("liveBroadcastContent", "")

    if upload_status and upload_status != "processed":
        return False, f"upload:{upload_status}"
    if privacy_status != "public":
        return False, f"privacy:{privacy_status or 'unknown'}"
    if embeddable is False:
        return False, "not-embeddable"
    if live_content in {"live", "upcoming"}:
        return False, f"live:{live_content}"

    return True, "usable"


def transcript_availability(video_id: str) -> tuple[bool, str]:
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
    except ImportError:
        return False, "transcript:tool-missing"

    try:
        YouTubeTranscriptApi().list(video_id)
    except Exception as exc:  # The package exposes several version-specific errors.
        return False, f"transcript:{exc.__class__.__name__}"

    return True, "transcript:available"


def parse_iso8601_duration(value: str) -> int:
    match = re.fullmatch(
        r"PT(?:(?P<hours>\d+)H)?(?:(?P<minutes>\d+)M)?(?:(?P<seconds>\d+)S)?",
        value,
    )
    if not match:
        return 0
    hours = int(match.group("hours") or 0)
    minutes = int(match.group("minutes") or 0)
    seconds = int(match.group("seconds") or 0)
    return hours * 3600 + minutes * 60 + seconds


def format_duration_label(total_seconds: int) -> str:
    if total_seconds <= 0:
        return ""
    minutes, seconds = divmod(total_seconds, 60)
    hours, minutes = divmod(minutes, 60)
    if hours:
        return f"{hours:d}:{minutes:02d}:{seconds:02d}"
    return f"{minutes:d}:{seconds:02d}"


def summarize_notes(duration_seconds: int, title_blob: str) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    lowered = title_blob.lower()

    for term, weight in POSITIVE_TERMS.items():
        if term.lower() in lowered:
            score += weight
            reasons.append(f"+{weight} {term}")

    for term, weight in NEGATIVE_TERMS.items():
        if term in lowered:
            score += weight
            reasons.append(f"{weight} {term}")

    if 480 <= duration_seconds <= 2400:
        score += 3
        reasons.append("+3 片長適中")
    elif 240 <= duration_seconds < 480:
        score += 2
        reasons.append("+2 可快速消化")
    elif 0 < duration_seconds < 180:
        score -= 3
        reasons.append("-3 太短")
    elif duration_seconds > 3600:
        score -= 1
        reasons.append("-1 偏長")

    return score, reasons


def score_query_match(query: str, metadata_blob: str, source_type: str) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    metadata = metadata_blob.lower()
    query_terms = [term.strip().lower() for term in query.split() if term.strip()]

    matched_terms = [term for term in query_terms if term in metadata]
    matched_count = len(matched_terms)

    if matched_count >= 3:
        score += 3
        reasons.append("+3 查詢貼合")
    elif matched_count == 2:
        score += 2
        reasons.append("+2 查詢貼合")
    elif matched_count == 1:
        score += 1
        reasons.append("+1 查詢略貼")
    else:
        if source_type == "general":
            score -= 8
            reasons.append("-8 與查詢不貼")
        else:
            score -= 4
            reasons.append("-4 與查詢偏離")

    return score, reasons


def score_channel(channel: str) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    lowered = channel.lower()

    for term, weight in NEGATIVE_CHANNEL_TERMS.items():
        if term.lower() in lowered:
            score += weight
            reasons.append(f"{weight} 頻道:{term}")

    return score, reasons


def classify_source_type(title_blob: str, channel: str) -> str:
    lowered = " ".join([title_blob, channel]).lower()

    if any(term in lowered for term in ["新聞", "新聞台", "live", "直播", "政論"]):
        return "news-risk"
    if any(term in lowered for term in ENTERTAINMENT_TERMS):
        return "entertainment"
    if any(term in lowered for term in PRIVATE_MEMORIAL_TERMS):
        return "private-memorial"
    if any(term in lowered for term in MEDIA_NOISE_TERMS):
        return "media-noise"
    if any(term in lowered for term in ["佛教", "法師", "法师", "和尚", "僧人", "佛陀", "禪修", "禅修", "寺廟", "寺庙"]):
        return "religion"
    if any(term in lowered for term in ["毛澤東", "毛泽东", "總統", "总统", "市長", "市长", "立委", "議員", "议员", "部長", "部长"]):
        return "politics"
    if any(
        term in lowered
        for term in [
            "mv",
            "music video",
            "主題曲",
            "主题曲",
            "纯享版",
            "純享版",
            "片段",
            "合唱",
            "配樂",
            "配乐",
            "lyric",
            "lyrics",
            "歌詞",
            "歌词",
            "動態歌詞",
            "动态歌词",
            "歌曲",
            "原創歌曲",
            "原创歌曲",
            "翻唱",
            "cover",
        ]
    ):
        return "music-fragment"
    if any(term in lowered for term in ["品牌", "品牌重塑", "集團", "企業", "同仁"]):
        return "brand"
    if any(term in lowered for term in ["課程", "课程", "畢業生訪談", "毕业生访谈", "原力生命故事", "原力創造", "原力创造"]):
        return "brand"
    if any(term in lowered for term in ["成果", "成果紀錄", "精華版", "基金會", "協會", "社區", "計畫"]):
        return "institutional"
    if any(
        term in lowered
        for term in ["回家", "陪伴", "等待", "守候", "守望", "在場", "父親", "母親", "外公", "家屬", "告別", "記憶", "人物故事", "生命故事"]
    ):
        return "story-fit"
    return "general"


def normalize_description(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:280]


def suggest_status(score: int, source_type: str) -> str:
    if source_type in {"news-risk", "politics", "religion", "entertainment", "brand", "music-fragment", "private-memorial", "media-noise"}:
        return "排除"
    if source_type == "general" and score < 18:
        return "排除"
    if source_type == "institutional":
        return "觀察" if score >= 18 else "排除"
    if source_type == "story-fit":
        if score >= 20:
            return "保留"
        if score >= 16:
            return "觀察"
        return "排除"
    if score >= 20:
        return "保留"
    if score >= 16:
        return "觀察"
    return "排除"


def score_fame(view_count: int, title_blob: str, channel: str) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []
    lowered = " ".join([title_blob, channel]).lower()

    if any(term in lowered for term in ["曾寶儀", "曾宝仪", "張頌文", "张颂文", "狂飆", "狂飙"]):
        score -= 10
        reasons.append("-10 明確名人排除")
    elif any(term in lowered for term in ["天王", "影帝", "明星", "女星", "男星", "藝人", "艺人", "總統", "总统", "市長", "市长", "主演", "角色"]):
        score -= 4
        reasons.append("-4 太有名")

    if view_count >= 2_000_000:
        score -= 4
        reasons.append("-4 過熱")
    elif view_count >= 500_000:
        score -= 2
        reasons.append("-2 偏熱門")
    elif 100 <= view_count <= 50_000:
        score += 2
        reasons.append("+2 小人物帶")
    elif 50_001 <= view_count <= 200_000:
        score += 1
        reasons.append("+1 中小眾")

    return score, reasons


def score_engagement(view_count: int, comment_count: int) -> tuple[int, list[str]]:
    score = 0
    reasons: list[str] = []

    if comment_count == 0:
        if view_count >= 10_000:
            score -= 6
            reasons.append("-6 有觀看但無心聲")
        elif view_count >= 1_000:
            score -= 5
            reasons.append("-5 有觀看但幾乎無回應")
        elif view_count >= 100:
            score -= 4
            reasons.append("-4 無留言")
        elif view_count >= 20:
            score -= 6
            reasons.append("-6 太冷又無留言")
        else:
            score -= 8
            reasons.append("-8 幾乎沒被觀眾驗證")
        return score, reasons

    if view_count < 100 and comment_count <= 1:
        score -= 2
        reasons.append("-2 觀眾驗證仍薄")

    if comment_count >= 100:
        score += 3
        reasons.append("+3 留言明顯")
    elif comment_count >= 20:
        score += 2
        reasons.append("+2 有留言")
    elif comment_count >= 5:
        score += 1
        reasons.append("+1 有少量留言")

    if view_count > 0:
        comments_per_thousand = (comment_count * 1000) / view_count
        if comments_per_thousand >= 5:
            score += 2
            reasons.append("+2 心得互動高")
        elif comments_per_thousand >= 2:
            score += 1
            reasons.append("+1 有互動")
        elif view_count >= 5_000 and comments_per_thousand < 0.5:
            score -= 2
            reasons.append("-2 互動偏低")

    return score, reasons


def build_rows(
    query: str,
    search_items: list[dict],
    detail_map: dict[str, dict],
    allow_unusable: bool,
    story_only: bool,
    require_transcript: bool,
) -> list[TopicRow]:
    rows: list[TopicRow] = []

    for item in search_items:
        video_id = item.get("id", {}).get("videoId", "")
        if not video_id:
            continue

        detail = detail_map.get(video_id, {})
        usable, availability = video_availability(detail)
        if not usable and not allow_unusable:
            continue

        snippet = detail.get("snippet", item.get("snippet", {}))
        statistics = detail.get("statistics", {})
        content_details = detail.get("contentDetails", {})

        title = (snippet.get("title") or "").strip()
        channel = (snippet.get("channelTitle") or "").strip()
        description = normalize_description(snippet.get("description") or "")
        published_at = (snippet.get("publishedAt") or "").strip()
        view_count = int(statistics.get("viewCount", 0) or 0)
        comment_count = int(statistics.get("commentCount", 0) or 0)
        duration_seconds = parse_iso8601_duration(content_details.get("duration", ""))
        duration_label = format_duration_label(duration_seconds)

        metadata_blob = " ".join([title, channel, description])
        score, reasons = summarize_notes(duration_seconds, metadata_blob)
        channel_score, channel_reasons = score_channel(channel)
        score += channel_score
        reasons.extend(channel_reasons)
        source_type = classify_source_type(metadata_blob, channel)

        if story_only and source_type != "story-fit":
            continue

        if source_type == "story-fit":
            score += 2
            reasons.append("+2 故事貼合")
        elif source_type == "music-fragment":
            score -= 5
            reasons.append("-5 音樂或片段")
        elif source_type == "institutional":
            score -= 2
            reasons.append("-2 機構成果片")
        elif source_type == "brand":
            score -= 4
            reasons.append("-4 品牌內容")
        elif source_type == "news-risk":
            score -= 6
            reasons.append("-6 新聞風險")
        elif source_type == "entertainment":
            score -= 7
            reasons.append("-7 娛樂人物排除")
        elif source_type == "private-memorial":
            score -= 8
            reasons.append("-8 私人追思片")
        elif source_type == "media-noise":
            score -= 7
            reasons.append("-7 媒體或劇情雜訊")
        elif source_type == "religion":
            score -= 8
            reasons.append("-8 佛教排除")
        elif source_type == "politics":
            score -= 8
            reasons.append("-8 政治排除")

        query_match_score, query_match_reasons = score_query_match(
            query, metadata_blob, source_type
        )
        score += query_match_score
        reasons.extend(query_match_reasons)

        fame_score, fame_reasons = score_fame(view_count, title, channel)
        score += fame_score
        reasons.extend(fame_reasons)
        engagement_score, engagement_reasons = score_engagement(
            view_count, comment_count
        )
        score += engagement_score
        reasons.extend(engagement_reasons)

        if view_count < 100:
            reasons.append("0 冷門待人工判讀")

        if not title:
            score -= 2
            reasons.append("-2 缺少標題")

        transcript_status = "not-checked"
        if require_transcript:
            has_transcript, transcript_status = transcript_availability(video_id)
            if not has_transcript:
                continue

        rows.append(
            TopicRow(
                rank=0,
                query=query,
                video_id=video_id,
                title=title,
                channel=channel,
                published_at=published_at,
                duration_seconds=duration_seconds,
                duration_label=duration_label,
                view_count=view_count,
                comment_count=comment_count,
                url=f"https://www.youtube.com/watch?v={video_id}",
                score=score,
                score_reasons=" | ".join(reasons),
                source_type=source_type,
                availability=availability,
                transcript_status=transcript_status,
                auto_suggestion=suggest_status(score, source_type),
                manual_status="",
                manual_note="",
                notes="待人工複查",
                top_comment_excerpt="",
                description=description,
            )
        )

    return rows


def sort_rows(rows: list[TopicRow]) -> list[TopicRow]:
    def engagement_priority(row: TopicRow) -> float:
        if row.view_count <= 0:
            return 0.0
        return row.comment_count / row.view_count

    sorted_rows = sorted(
        rows,
        key=lambda row: (
            -row.score,
            -(1 if row.comment_count > 0 else 0),
            -engagement_priority(row),
            -row.comment_count,
            -row.view_count,
            row.duration_seconds,
            row.title.lower(),
        ),
    )
    for index, row in enumerate(sorted_rows, start=1):
        row.rank = index
    return sorted_rows


def deduplicate_rows(rows: list[TopicRow]) -> list[TopicRow]:
    best_by_video: dict[str, TopicRow] = {}

    for row in rows:
        existing = best_by_video.get(row.video_id)
        if existing is None:
            best_by_video[row.video_id] = row
            continue

        if (
            row.score,
            row.comment_count,
            row.view_count,
        ) > (
            existing.score,
            existing.comment_count,
            existing.view_count,
        ):
            best_by_video[row.video_id] = row

    return list(best_by_video.values())


def limit_rows_per_channel(rows: list[TopicRow], max_per_channel: int) -> list[TopicRow]:
    if max_per_channel <= 0:
        return rows

    kept: list[TopicRow] = []
    counts: dict[str, int] = {}

    for row in rows:
        channel_key = row.channel.strip().lower()
        if counts.get(channel_key, 0) >= max_per_channel:
            continue
        counts[channel_key] = counts.get(channel_key, 0) + 1
        kept.append(row)

    return kept


def write_csv(path: Path, rows: list[TopicRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "query",
                "rank",
                "score",
                "score_reasons",
                "source_type",
                "availability",
                "transcript_status",
                "auto_suggestion",
                "manual_status",
                "manual_note",
                "title",
                "channel",
                "published_at",
                "duration_label",
                "view_count",
                "comment_count",
                "url",
                "notes",
                "top_comment_excerpt",
                "description",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "query": row.query,
                    "rank": row.rank,
                    "score": row.score,
                    "score_reasons": row.score_reasons,
                    "source_type": row.source_type,
                    "availability": row.availability,
                    "transcript_status": row.transcript_status,
                    "auto_suggestion": row.auto_suggestion,
                    "manual_status": row.manual_status,
                    "manual_note": row.manual_note,
                    "title": row.title,
                    "channel": row.channel,
                    "published_at": row.published_at,
                    "duration_label": row.duration_label,
                    "view_count": row.view_count,
                    "comment_count": row.comment_count,
                    "url": row.url,
                    "notes": row.notes,
                    "top_comment_excerpt": row.top_comment_excerpt,
                    "description": row.description,
                }
            )


def is_shortlist_candidate(row: TopicRow) -> bool:
    if row.auto_suggestion == "排除":
        return False
    if row.source_type in {"media-noise", "news-risk", "politics", "religion", "entertainment", "brand", "music-fragment"}:
        return False
    return True


def write_shortlist(path: Path, rows: list[TopicRow], min_score: int) -> tuple[int, bool]:
    clean_rows = [row for row in rows if is_shortlist_candidate(row)]
    shortlisted = [row for row in clean_rows if row.score >= min_score]
    used_fallback = False
    if not shortlisted and clean_rows:
        shortlisted = clean_rows[: min(5, len(clean_rows))]
        used_fallback = True
    write_csv(path, shortlisted)
    return len(shortlisted), used_fallback


def write_topic_plan(path: Path, plan: dict[str, str], queries: list[str], args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    hook = plan.get("hook") or "(no hook)"
    intent_note = plan.get("intent_note") or "未使用 AI 解讀，改用靜態 query。"
    query_source = plan.get("query_source", "static")
    lines = [
        f"# 今日 Hook：{hook}",
        "",
        "## AI 對 Hook 的理解",
        "",
        intent_note,
        "",
        "## 搜尋策略",
        "",
        f"- query source: {query_source}",
        f"- story only: {args.story_only}",
        f"- require transcript: {args.require_transcript}",
        f"- allow unusable: {args.allow_unusable}",
        "",
        "## YouTube 搜尋 Query",
        "",
    ]
    lines.extend(f"- {query}" for query in queries)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_topic_report(path: Path, rows: list[TopicRow], plan: dict[str, str], args: argparse.Namespace) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    hook = plan.get("hook") or "(no hook)"
    lines = [
        f"# 今日選題報告：{hook}",
        "",
        "## 結論",
        "",
    ]

    if not rows:
        lines.extend(
            [
                "這輪沒有找到符合條件的候選。",
                "",
                "## 建議下一步",
                "",
                "- 保留同一個 hook，但把「需要有字幕/文字可抓？」改成 `n` 再跑一次。",
                "- 保留同一個 hook，但讓下一輪 query 更像 YouTube 搜尋詞，例如「高溫 工作 紀錄片」「酷暑 獨居老人 訪談」。",
                "- 或把 hook 補成更具體的生活場景，例如「停電的夏天」「烈日下工作的人」「高溫裡的老人陪伴」。",
                "- 如果仍然 0 筆，代表 YouTube 當下可用素材不足，不代表 hook 不好。",
            ]
        )
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        return

    lines.extend(
        [
            f"找到 {len(rows)} 筆候選。先看前 3 筆，不要一次看完整 CSV。",
            "",
            "## 建議先看",
            "",
        ]
    )
    for row in rows[:3]:
        lines.extend(
            [
                f"### {row.rank}. {row.title}",
                "",
                f"- 分數：{row.score}",
                f"- 類型：{row.source_type}",
                f"- 點閱 / 留言：{row.view_count} / {row.comment_count}",
                f"- 可用性：{row.availability}",
                f"- 字幕：{row.transcript_status}",
                f"- URL：{row.url}",
                f"- 為什麼：{row.score_reasons}",
                "",
            ]
        )

    risky = [row for row in rows if row.auto_suggestion == "排除"]
    if risky:
        lines.extend(["## 排除或小心", ""])
        for row in risky[:5]:
            lines.append(f"- {row.title}：{row.source_type}，{row.score_reasons}")

    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def print_summary(rows: list[TopicRow], output: Path) -> None:
    print(f"Wrote {len(rows)} rows to {output}")
    for row in rows[:8]:
        print(
            f"{row.rank:>2}. [score={row.score:>2}] [{row.source_type}] "
            f"{row.query} :: {row.title} "
            f"({row.duration_label or 'n/a'}, {row.view_count} views, "
            f"{row.comment_count} comments)"
        )


def validate_api_key(api_key: str) -> None:
    if api_key:
        return
    raise SystemExit(
        "Missing YouTube API key. Set YOUTUBE_API_KEY or pass --api-key."
    )


def main() -> int:
    args = parse_args()
    validate_api_key(args.api_key)

    queries, plan = read_queries_with_plan(args)
    if not queries:
        raise SystemExit("No queries found. Pass --query or create topic_queries.txt.")
    write_topic_plan(args.plan_output, plan, queries, args)

    all_rows: list[TopicRow] = []

    for query in queries:
        search_items = search_videos(
            api_key=args.api_key,
            query=query,
            max_results=max(1, min(args.max_results, 50)),
            region_code=args.region_code,
            language=args.language,
            order=args.order,
        )
        video_ids = [item.get("id", {}).get("videoId", "") for item in search_items]
        details = fetch_video_details(args.api_key, video_ids)
        rows = build_rows(
            query,
            search_items,
            details,
            args.allow_unusable,
            args.story_only,
            args.require_transcript,
        )
        all_rows.extend(rows)
        time.sleep(max(args.sleep, 0))

    filtered_rows = [row for row in all_rows if row.score >= args.min_score]
    filtered_rows = deduplicate_rows(filtered_rows)
    sorted_rows = sort_rows(filtered_rows)
    sorted_rows = limit_rows_per_channel(sorted_rows, args.max_per_channel)
    sorted_rows = sort_rows(sorted_rows)
    if not sorted_rows:
        write_topic_report(args.report_output, [], plan, args)
        print(
            "Wrote 0 rows. Existing CSV files were kept. "
            f"Review {args.plan_output} and {args.report_output} for next steps."
        )
        return 0

    for row in sorted_rows:
        if row.score < args.shortlist_min_score or row.comment_count <= 0:
            continue
        row.top_comment_excerpt = fetch_top_comment_excerpt(args.api_key, row.video_id)
        time.sleep(max(args.sleep, 0))
    write_csv(args.output, sorted_rows)
    shortlist_count, used_fallback = write_shortlist(
        args.shortlist_output, sorted_rows, args.shortlist_min_score
    )
    write_topic_report(args.report_output, sorted_rows, plan, args)
    print_summary(sorted_rows, args.output)
    if used_fallback:
        print(
            f"No rows reached shortlist score {args.shortlist_min_score}. "
            f"Wrote top {shortlist_count} review rows to {args.shortlist_output}."
        )
    else:
        print(
            f"Shortlist ({args.shortlist_min_score}+) written to "
            f"{args.shortlist_output}"
        )
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit("Interrupted.")
