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
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import urlopen


YOUTUBE_API_BASE = "https://www.googleapis.com/youtube/v3"
DEFAULT_QUERY_FILE = Path(__file__).with_name("topic_queries.txt")

POSITIVE_TERMS = {
    "訪談": 3,
    "專訪": 3,
    "人物故事": 4,
    "生命故事": 4,
    "紀錄": 3,
    "紀實": 3,
    "紀錄片": 4,
    "微紀錄片": 4,
    "調查報告": 3,
    "陪伴": 2,
    "回家": 2,
    "重新開始": 3,
    "重啟": 2,
    "告白": 1,
}

NEGATIVE_TERMS = {
    "shorts": -5,
    "short": -3,
    "看哭": -4,
    "催淚": -3,
    "爆哭": -4,
    "必看": -2,
    "精彩片段": -3,
    "reaction": -3,
    "懶人包": -2,
    "八卦": -4,
}


@dataclass
class TopicRow:
    query: str
    video_id: str
    title: str
    channel: str
    published_at: str
    duration_seconds: int
    duration_label: str
    view_count: int
    url: str
    score: int
    score_reasons: str
    notes: str
    description: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Search YouTube topics and export a Google-Sheet-ready CSV."
    )
    parser.add_argument(
        "--api-key",
        default=os.environ.get("YOUTUBE_API_KEY", "").strip(),
        help="YouTube Data API key. Defaults to YOUTUBE_API_KEY env var.",
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
        "--sleep",
        type=float,
        default=0.15,
        help="Small pause between API calls.",
    )
    return parser.parse_args()


def read_queries(args: argparse.Namespace) -> list[str]:
    queries: list[str] = []
    seen: set[str] = set()

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

    return queries


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
    payload = fetch_json(
        "search",
        {
            "key": api_key,
            "part": "snippet",
            "q": query,
            "type": "video",
            "maxResults": max_results,
            "regionCode": region_code,
            "relevanceLanguage": language,
            "safeSearch": "strict",
            "videoEmbeddable": "true",
            "order": order,
        },
    )
    return payload.get("items", [])


def fetch_video_details(api_key: str, video_ids: Iterable[str]) -> dict[str, dict]:
    video_ids = [video_id for video_id in video_ids if video_id]
    if not video_ids:
        return {}

    payload = fetch_json(
        "videos",
        {
            "key": api_key,
            "part": "snippet,contentDetails,statistics",
            "id": ",".join(video_ids),
        },
    )
    return {item["id"]: item for item in payload.get("items", [])}


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


def normalize_description(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:280]


def build_rows(
    query: str,
    search_items: list[dict],
    detail_map: dict[str, dict],
) -> list[TopicRow]:
    rows: list[TopicRow] = []

    for item in search_items:
        video_id = item.get("id", {}).get("videoId", "")
        if not video_id:
            continue

        detail = detail_map.get(video_id, {})
        snippet = detail.get("snippet", item.get("snippet", {}))
        statistics = detail.get("statistics", {})
        content_details = detail.get("contentDetails", {})

        title = (snippet.get("title") or "").strip()
        channel = (snippet.get("channelTitle") or "").strip()
        description = normalize_description(snippet.get("description") or "")
        published_at = (snippet.get("publishedAt") or "").strip()
        view_count = int(statistics.get("viewCount", 0) or 0)
        duration_seconds = parse_iso8601_duration(content_details.get("duration", ""))
        duration_label = format_duration_label(duration_seconds)

        score_blob = " ".join([query, title, channel, description])
        score, reasons = summarize_notes(duration_seconds, score_blob)

        if view_count >= 100000:
            score += 2
            reasons.append("+2 高觀看驗證")
        elif 10000 <= view_count < 100000:
            score += 1
            reasons.append("+1 中等熱度")
        elif view_count < 300:
            reasons.append("0 冷門待人工判讀")

        rows.append(
            TopicRow(
                query=query,
                video_id=video_id,
                title=title,
                channel=channel,
                published_at=published_at,
                duration_seconds=duration_seconds,
                duration_label=duration_label,
                view_count=view_count,
                url=f"https://www.youtube.com/watch?v={video_id}",
                score=score,
                score_reasons=" | ".join(reasons),
                notes="待人工複查",
                description=description,
            )
        )

    return rows


def sort_rows(rows: list[TopicRow]) -> list[TopicRow]:
    return sorted(
        rows,
        key=lambda row: (
            -row.score,
            -row.view_count,
            row.duration_seconds,
            row.title.lower(),
        ),
    )


def write_csv(path: Path, rows: list[TopicRow]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "query",
                "score",
                "score_reasons",
                "title",
                "channel",
                "published_at",
                "duration_label",
                "view_count",
                "url",
                "notes",
                "description",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow(
                {
                    "query": row.query,
                    "score": row.score,
                    "score_reasons": row.score_reasons,
                    "title": row.title,
                    "channel": row.channel,
                    "published_at": row.published_at,
                    "duration_label": row.duration_label,
                    "view_count": row.view_count,
                    "url": row.url,
                    "notes": row.notes,
                    "description": row.description,
                }
            )


def print_summary(rows: list[TopicRow], output: Path) -> None:
    print(f"Wrote {len(rows)} rows to {output}")
    for row in rows[:8]:
        print(
            f"- [{row.score:>2}] {row.query} :: {row.title} "
            f"({row.duration_label or 'n/a'}, {row.view_count} views)"
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

    queries = read_queries(args)
    if not queries:
        raise SystemExit("No queries found. Pass --query or create topic_queries.txt.")

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
        rows = build_rows(query, search_items, details)
        all_rows.extend(rows)
        time.sleep(max(args.sleep, 0))

    filtered_rows = [row for row in all_rows if row.score >= args.min_score]
    sorted_rows = sort_rows(filtered_rows)
    write_csv(args.output, sorted_rows)
    print_summary(sorted_rows, args.output)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        raise SystemExit("Interrupted.")
