import asyncio
import subprocess
import sys
import time
import unicodedata
from pathlib import Path

WORKFLOW_DIR = Path(__file__).resolve().parent
REPO_ROOT = WORKFLOW_DIR.parent
MAX_TTS_CHARS = 1800

if str(WORKFLOW_DIR) not in sys.path:
    sys.path.insert(0, str(WORKFLOW_DIR))

from module_4_voice import generate_voice_with_fallback


def input_multiline_text(prompt: str) -> str:
    print(prompt)
    print("貼上後另起一行輸入 END 結束。")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        marker = line.strip().upper()
        if marker == "END" or marker.startswith("END ") or line.strip() == "結束":
            break
        lines.append(line)
    return "\n".join(lines).strip()


def clean_text(text: str) -> str:
    cleaned = []
    for char in text:
        if char in {"\n", "\r", "\t"}:
            cleaned.append(char)
            continue
        if unicodedata.category(char).startswith("C"):
            continue
        cleaned.append(char)
    return "".join(cleaned).strip()


def choose_source() -> str:
    print("請選擇文字來源：")
    print("1. 讀 Mac 剪貼簿 clip（推薦，先把全文複製好）")
    print("2. 讀 .txt 檔案路徑")
    print("3. 手動貼上文字（短文才建議）")
    while True:
        try:
            choice = input("請選擇 [預設 1]: ").strip()
        except EOFError:
            return "clip"
        if choice in {"", "1", "clip", "剪貼簿"}:
            return "clip"
        if choice in {"2", "txt", "file", "檔案"}:
            return "file"
        if choice in {"3", "paste", "貼上"}:
            return "paste"
        print("請輸入 1、2 或 3。")


def choose_voice() -> str:
    while True:
        try:
            choice = input("請選擇聲音 (1: 溫暖女聲-曉臻, 2: 沉穩男聲-雲哲) [預設 1]: ").strip()
        except EOFError:
            return "female"
        if choice in {"", "1"}:
            print("👉 已選擇：溫暖女聲")
            return "female"
        if choice == "2":
            print("👉 已選擇：沉穩男聲")
            return "male"
        print("請輸入 1 或 2。")


def read_clipboard() -> str:
    result = subprocess.run(["pbpaste"], capture_output=True, text=True, check=False)
    return result.stdout.strip()


def split_text_for_tts(text: str, max_chars: int = MAX_TTS_CHARS) -> list[str]:
    paragraphs = [part.strip() for part in text.splitlines() if part.strip()]
    chunks: list[str] = []
    current = ""

    for paragraph in paragraphs:
        if len(paragraph) > max_chars:
            if current:
                chunks.append(current.strip())
                current = ""
            for start in range(0, len(paragraph), max_chars):
                chunks.append(paragraph[start : start + max_chars].strip())
            continue

        candidate = f"{current}\n{paragraph}".strip() if current else paragraph
        if len(candidate) <= max_chars:
            current = candidate
        else:
            chunks.append(current.strip())
            current = paragraph

    if current:
        chunks.append(current.strip())
    return [chunk for chunk in chunks if chunk]


def merge_mp3_files(part_paths: list[Path], output_path: Path) -> None:
    with output_path.open("wb") as output:
        for part_path in part_paths:
            with part_path.open("rb") as part:
                output.write(part.read())


async def main() -> int:
    print("=========================================")
    print("文字轉語音 Text to Voice")
    print("=========================================")

    source_mode = choose_source()
    if source_mode == "clip":
        text = read_clipboard()
        print(f"已讀取剪貼簿：{len(text)} 字")
    elif source_mode == "file":
        source = input("請輸入 .txt 檔案路徑: ").strip()
        source_path = Path(source).expanduser()
        if not source_path.exists():
            print(f"找不到檔案：{source_path}")
            return 1
        text = source_path.read_text(encoding="utf-8").strip()
    else:
        text = input_multiline_text("請貼上要轉語音的文案。")

    text = clean_text(text)
    if not text:
        print("沒有文字，已取消。")
        return 1

    voice_type = choose_voice()
    audio_dir = REPO_ROOT / "assets" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    audio_path = audio_dir / f"text_voice_{int(time.time())}.mp3"
    chunks = split_text_for_tts(text)

    print(f"\n文字長度：{len(text)} 字，將分成 {len(chunks)} 段產生 MP3。")
    part_paths: list[Path] = []
    actual_voice_types = set()
    for index, chunk in enumerate(chunks, start=1):
        part_path = audio_path.with_name(f"{audio_path.stem}_part{index:02d}.mp3")
        print(f"正在產生第 {index}/{len(chunks)} 段...")
        audio_ok, actual_voice_type, audio_error = await generate_voice_with_fallback(
            chunk,
            str(part_path),
            voice_type,
        )
        if not audio_ok:
            print(f"語音生成失敗：{audio_error}")
            return 1
        actual_voice_types.add(actual_voice_type)
        part_paths.append(part_path)

    if len(part_paths) == 1:
        part_paths[0].replace(audio_path)
    else:
        merge_mp3_files(part_paths, audio_path)
        for part_path in part_paths:
            part_path.unlink(missing_ok=True)

    if voice_type not in actual_voice_types:
        print("男聲配音失敗，已自動改用女聲完成。")
    print(f"完成：{audio_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
