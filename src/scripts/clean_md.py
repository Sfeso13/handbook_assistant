import re
from pathlib import Path

def normalize_headers(md: str) -> str:
    out = []

    for raw_line in md.splitlines():
        line = raw_line.rstrip()

        header = re.match(r'^(#+)\s+(.*)', line)

        if header:
            hashes, title = header.groups()

            # Numeric main section
            if re.match(r'\*\*\d+\.\s+|\d+\.\s+', title):
                out.append(f"## {title}")

            # Alphabetic subsection
            elif re.match(r'\*\*[a-zA-Z]\.\s+|[a-zA-Z]\.\s+', title):
                out.append(f"### {title}")

            else:
                out.append(line)

        else:
            # Non-header numeric lines
            if re.match(r'^\d+\.\s+', line):
                out.append(f"## {line}")
            elif re.match(r'^[a-zA-Z]\.\s+', line):
                out.append(f"### {line}")
            else:
                out.append(line)

    return "\n".join(out)


INPUT = Path("data/processed/handbook.md")
OUTPUT = Path("data/cleaned/handbook_clean.md")

text = INPUT.read_text(encoding="utf-8")

# Remove page numbers
text = re.sub(
    r'\n*!?\[\]\(_page_\d+_Picture_\d+\.jpeg\)\n*',
    '\n',
    text
)
# Collapse excessive newlines
text = re.sub(r"\n{3,}", "\n\n", text)

# Normalize spacing
text = text.strip() + "\n"

# Normalize normalize headers
text = normalize_headers(text)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(text, encoding="utf-8")
