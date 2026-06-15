from google import genai
import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def read_env_file(path):
    values = {}
    if not path.exists():
        return values

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def get_gemini_api_key():
    env_file_key = read_env_file(REPO_ROOT / ".env").get("GEMINI_API_KEY", "").strip()
    if env_file_key:
        return env_file_key, ".env"

    shell_key = os.environ.get("GEMINI_API_KEY", "").strip()
    if shell_key:
        return shell_key, "shell env"

    return "", "missing"

try:
    api_key, source = get_gemini_api_key()
    if not api_key:
        raise RuntimeError("Missing GEMINI_API_KEY. Add it to .env or export it.")

    print(f"GEMINI_API_KEY source={source}, length={len(api_key)}")

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='say hi'
    )
    print("SUCCESS", response.text)
except Exception as e:
    print("FAILED", str(e))
