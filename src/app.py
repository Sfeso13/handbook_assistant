import  json
from    scripts.retrieval import retrieve
from    scripts.embedding import embed


chunks = []
with open("data/chunked/handbook_chunked.jsonl", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line:
            chunks.append(json.loads(line))

model = embed(chunks)

retrieved = retrieve("can i smoke?", model)

for chunk in retrieved:
    print(f"path : {chunk['path']}")
