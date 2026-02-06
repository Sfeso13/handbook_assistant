from scripts.embedding import embed
from scripts.chunker import chunk_markdown
from pathlib import Path
import json

def main():
    input_path = Path("data/cleaned/handbook_clean.md")
    output_path = Path("data/chunked/handbook_chunked.jsonl")

    print("####### STARTED CHUNKING #############")
    chunks = chunk_markdown(input_path, output_path)
    print("####### FINISHED CHUNKING #############")

    #with open(output_path, "r", encoding="utf-8") as f:
    #    for line in f:
    #        line = line.strip()
    #        if line:  # skip empty lines
    #            chunk = json.loads(line)
    #            chunks.append(chunk)
    
    print("####### STARTED EMBEDING #############")
    embed(chunks)
    print("####### FINISHED EMBEDING #############")

if __name__ == "__main__":
    main()
