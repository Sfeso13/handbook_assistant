import re
from pathlib import Path
import json

def chunk_markdown(md: str):
    chunks = []

    current = {
        "h1": None,
        "h2": None,
        "content": []
    }

    for line in md.splitlines():
        h1 = re.match(r'^# (.+)', line)
        h2 = re.match(r'^## (.+)', line)

        if h1:
            current["h1"] = h1.group(1)
            continue

        if h2:
            # save previous chunk
            if current["h2"] and current["content"]:
                chunks.append({
                    "path": [current["h1"], current["h2"]],
                    "content": "\n".join(current["content"]).strip()
                })

            current["h2"] = h2.group(1)
            current["content"] = []
            continue

        current["content"].append(line)

    # last chunk
    if current["h2"] and current["content"]:
        chunks.append({
            "path": [current["h1"], current["h2"]],
            "content": "\n".join(current["content"]).strip()
        })

    return chunks


INPUT = Path("data/cleaned/handbook_clean.md")
OUTPUT = Path("data/chunked/handbook_chunked.jsonl")

text = INPUT.read_text(encoding="utf-8")

chunks = chunk_markdown(text)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)

with OUTPUT.open("w", encoding="utf-8") as f:
    for chunk in chunks:
        f.write(json.dumps(chunk, ensure_ascii=False) + "\n")
