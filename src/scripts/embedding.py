import json
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


def embed(chunks):
    texts = [c["content"] for c in chunks]

    model = SentenceTransformer("all-MiniLM-L6-v2")

    embeddings = model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            normalize_embeddings=True
            )

    dim = embeddings.shape[1]

    index = faiss.IndexFlatIP(dim)
    index.add(np.array(embeddings))

    faiss.write_index(index, "data/index/handbook.faiss")

    with open("data/index/metadata.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    
