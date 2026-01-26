

def build_prompt(query, chunks):
    context = "\n\n".join(
        f"[{i+1}] {chunk['content']}"
        for i, chunk in enumerate(chunks)
    )

    prompt = f"""
                You are an assistant answering questions using the provided handbook excerpts.
Answer strictly based on the context below.
If the answer is not in the context, say "I don't know".

Context:
{context}

Question:
{query}

Answer:
"""
    return prompt.strip()

