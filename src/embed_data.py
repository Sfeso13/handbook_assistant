from scripts.embedding import embed
import json

def main():
    path = "data/chunked/handbook_chunked.jsonl"
    chunks = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines
                chunk = json.loads(line)
                chunks.append(chunk)
    embed(chunks)

if __name__ == "__main__"
    main()
