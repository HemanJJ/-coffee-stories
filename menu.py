#!/usr/bin/env python3
"""Small command menu for coffee-stories tools."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent

def workflow_python() -> str:
    venv_python = ROOT / "workflow" / "venv" / "bin" / "python"
    if venv_python.exists():
        return str(venv_python)
    return sys.executable


COMMANDS = {
    "1": {
        "name": "yt-find",
        "title": "YouTube 題材搜尋",
        "command": [],
    },
    "2": {
        "name": "story-make-single",
        "title": "單口說故事：正式上架用",
        "command": [
            workflow_python(),
            str(ROOT / "workflow" / "main.py"),
            "--mode",
            "single",
        ],
    },
    "3": {
        "name": "story-make-dialogue",
        "title": "男女對話試聽：像 NotebookLM，用來聽題材",
        "command": [
            workflow_python(),
            str(ROOT / "workflow" / "main.py"),
            "--mode",
            "dialogue",
        ],
    },
    "4": {
        "name": "text-to-voice",
        "title": "現成文案轉 MP3",
        "command": [
            workflow_python(),
            str(ROOT / "workflow" / "text_to_voice.py"),
        ],
    },
}


def prompt_with_default(label: str, default: str) -> str:
    value = input(f"{label} [{default}]: ").strip()
    return value or default


def ask_yes_no(label: str, default: bool = True) -> bool:
    suffix = "Y/n" if default else "y/N"
    value = input(f"{label} [{suffix}]: ").strip().lower()
    if not value:
        return default
    return value in {"y", "yes", "1", "true", "是", "好"}


def infer_intent(hook: str) -> str:
    if any(term in hook for term in ["父", "母", "阿嬤", "阿公", "外公", "外婆", "家人"]):
        return "family"
    if any(term in hook for term in ["回家", "故鄉", "离家", "離家", "返鄉"]):
        return "home"
    if any(term in hook for term in ["陪伴", "等待", "守候", "守望", "在場", "照顧", "照顾", "陪病", "長照"]):
        return "care"
    if any(term in hook for term in ["重新", "中年", "轉職", "人生下半場"]):
        return "restart"
    if any(term in hook for term in ["台語", "客語", "潮汕", "方言"]):
        return "dialect"
    return "object"


def build_yt_find_command(interactive: bool) -> list[str]:
    hook = "一封信"
    sample_queries = "5"
    strict_usable = True
    story_only = True
    require_transcript = True

    if interactive:
        print("\n先給一個方向 hook，AI 會先展開成幾組 YouTube 搜尋策略。")
        hook = prompt_with_default("今天的 hook，例如 一封信 / 回家 / 阿嬤 / 等待", hook)
        strict_usable = ask_yes_no("只要可用影片？", strict_usable)
        story_only = ask_yes_no("只要故事型，排除歌曲/MV/劇集/vlog？", story_only)
        require_transcript = ask_yes_no("需要有字幕/文字可抓？", require_transcript)

    command = [
        workflow_python(),
        str(ROOT / "tools" / "search_youtube_topics.py"),
        "--intent",
        infer_intent(hook),
        "--hook",
        hook,
        "--ai-expand-hook",
        "--sample-queries",
        sample_queries,
        "--output",
        "youtube_topic_candidates.csv",
        "--shortlist-output",
        "shortlist.csv",
        "--plan-output",
        "topic_plan.md",
        "--report-output",
        "topic_report.md",
    ]
    if not strict_usable:
        command.append("--allow-unusable")
    if story_only:
        command.append("--story-only")
    if require_transcript:
        command.append("--require-transcript")
    return command


def print_menu() -> None:
    print("=========================================")
    print("咖啡時光廊 Python Menu")
    print("=========================================")
    for key, item in COMMANDS.items():
        print(f"{key}. {item['name']} - {item['title']}")
    print("q. quit")


def run_choice(choice: str, interactive: bool = False) -> int:
    item = COMMANDS.get(choice)
    if not item:
        print("沒有這個選項。")
        return 1

    print(f"\nRunning: {item['name']}\n")
    if item["name"] == "yt-find":
        command = build_yt_find_command(interactive)
    else:
        command = item["command"]
    return subprocess.call(command, cwd=ROOT)


def main() -> int:
    if len(sys.argv) > 1:
        requested = sys.argv[1]
        if requested == "story-make":
            requested = "story-make-single"
        for key, item in COMMANDS.items():
            if requested in {key, item["name"]}:
                return run_choice(key, interactive=False)
        print(f"未知指令: {requested}")
        print("可用指令: yt-find, story-make-single, story-make-dialogue, text-to-voice")
        return 1

    print_menu()
    choice = input("請選擇: ").strip()
    if choice.lower() in {"q", "quit", "exit"}:
        return 0
    return run_choice(choice, interactive=True)


if __name__ == "__main__":
    raise SystemExit(main())
