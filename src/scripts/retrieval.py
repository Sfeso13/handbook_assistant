import faiss
import json

def retrieve(query, model, k=5):
    index = faiss.read_index("data/index/handbook.faiss")
    with open("data/index/metadata.json", encoding="utf-8") as f:
        chunks = json.load(f)

    query_emb = model.encode([query], normalize_embeddings=True)
    D, I = index.search(query_emb, k)

    retrieved_chunks = [chunks[i] for i in I[0]]

    return retrieved_chunks


