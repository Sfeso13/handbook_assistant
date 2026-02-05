import json
from ollama import embeddings
import faiss
import numpy as np


def embed(chunks, model="nomic-embed-text-v2-moe"):
    texts = [c["content"] for c in chunks]
    
    vectors = []
    
    for text in texts:
        res = embeddings(
            model=model,
            prompt=text
        )
        vectors.append(res["embedding"])

    embeddings_np = np.array(vectors, dtype="float32")
    dim = embeddings_np.shape[1]

    index = faiss.IndexFlatIP(dim)
    index.add(embeddings_np)

    faiss.write_index(index, "data/index/handbook.faiss")

    with open("data/index/metadata.json", "w", encoding="utf-8") as f:
        json.dump(
            {
                "embed_model": model,
                "dimension": dim,
                "chunks": chunks
            },
            f,
            ensure_ascii=False,
            indent=2
        )
