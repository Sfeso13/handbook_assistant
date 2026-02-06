import re
from pathlib import Path
from scripts.token_length import calculate_tokens
import json

def split_large_paragraph(text, max_tokens):
    words = text.split()
    chunks = []
    start = 0

    max_words = int(max_tokens / 1.3)

    while start < len(words):
        end = min(start + max_words, len(words))
        chunks.append(" ".join(words[start:end]))
        start += max_words

    return chunks

def split_section_text(
    text: str,
    max_tokens=400,
    overlap_paragraphs=1,
):
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    chunks = []

    current = []
    current_tokens = 0

    for p in paragraphs:
        p_tokens = calculate_tokens(p)

        # Paragraph alone is too big → fallback later
        if p_tokens > max_tokens:
            if current:
                chunks.append("\n\n".join(current))
                current = []
                current_tokens = 0
            chunks.extend(split_large_paragraph(p, max_tokens))
            continue

        if current_tokens + p_tokens <= max_tokens:
            current.append(p)
            current_tokens += p_tokens
        else:
            chunks.append("\n\n".join(current))
            current = current[-overlap_paragraphs:] + [p]
            current_tokens = calculate_tokens("\n\n".join(current))

    if current:
        chunks.append("\n\n".join(current))

    return chunks

def chunk_markdown(input_path: Path, output_path: Path):

    md = input_path.read_text(encoding="utf-8")

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
        # process previous h2 content
            if current["h2"] and current["content"]:
                full_text = "\n".join(current["content"]).strip()
                sub_chunks = split_section_text(full_text)
                for sub in sub_chunks:
                    chunks.append({
                        "path": [current["h1"], current["h2"]],
                        "content": sub
                        })
            current["h2"] = h2.group(1)
            current["content"] = []
            continue

        current["content"].append(line)

    # last h2 chunk
    if current["h2"] and current["content"]:
        full_text = "\n".join(current["content"]).strip()
        sub_chunks = split_section_text(full_text)
        for sub in sub_chunks:
            chunks.append({
                "path": [current["h1"], current["h2"]],
                "content": sub
                })
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(json.dumps(chunk, ensure_ascii=False) + "\n")

    return chunks


