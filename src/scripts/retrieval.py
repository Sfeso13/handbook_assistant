import faiss
from ollama import embeddings
import numpy as np
import json

def retrieve(query, model, k=5):
    index = faiss.read_index("data/index/handbook.faiss")
    with open("data/index/metadata.json", encoding="utf-8") as f:
        meta = json.load(f)
        chunks = meta["chunks"]
    
    res = embeddings(
        model=model,
        prompt="search_query: " + query
    )
    
    query_vec = np.array([res["embedding"]], dtype="float32")
    D, I = index.search(query_vec, k)

    retrieved_chunks = []
    for score, idx in zip(D[0], I[0]):
        chunk = chunks[idx].copy()
        chunk["score"] = float(score)
        retrieved_chunks.append(chunk)
    
    return retrieved_chunks


