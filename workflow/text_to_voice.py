import asyncio
import time
from pathlib import Path

from module_4_voice import generate_voice_with_fallback


WORKFLOW_DIR = Path(__file__).resolve().parent
REPO_ROOT = WORKFLOW_DIR.parent


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


async def main() -> int:
    print("=========================================")
    print("文字轉語音 Text to Voice")
    print("=========================================")

    source = input("請輸入 .txt 路徑；或直接 Enter 改用貼上文字: ").strip()
    if source:
        source_path = Path(source).expanduser()
        if not source_path.exists():
            print(f"找不到檔案：{source_path}")
            return 1
        text = source_path.read_text(encoding="utf-8").strip()
    else:
        text = input_multiline_text("請貼上要轉語音的文案。")

    if not text:
        print("沒有文字，已取消。")
        return 1

    voice_type = choose_voice()
    audio_dir = REPO_ROOT / "assets" / "audio"
    audio_dir.mkdir(parents=True, exist_ok=True)
    audio_path = audio_dir / f"text_voice_{int(time.time())}.mp3"

    print("\n正在產生 MP3...")
    audio_ok, actual_voice_type, audio_error = await generate_voice_with_fallback(
        text,
        str(audio_path),
        voice_type,
    )
    if not audio_ok:
        print(f"語音生成失敗：{audio_error}")
        return 1
    if actual_voice_type != voice_type:
        print("男聲配音失敗，已自動改用女聲完成。")
    print(f"完成：{audio_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(asyncio.run(main()))
