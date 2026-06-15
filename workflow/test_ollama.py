from pathlib import Path

from module_2_story import generate_story


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


model = read_env_file(REPO_ROOT / ".env").get("OLLAMA_MODEL", "qwen2.5:7b")
sample = "一位老人每天傍晚坐在巷口，看著回家的孩子。他不多說話，只把燈打開，等家人回來。"

print(f"OLLAMA_MODEL={model}")
story = generate_story(sample, model)
if story:
    print("SUCCESS", story.get("title", ""))
else:
    print("FAILED")
