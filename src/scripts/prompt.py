def build_prompt(query, system, chunks=[], history=""):
    context = ""
    if chunks:
        context = "\n\n".join(
            f"[{i+1}] {chunk['content']}"
            for i, chunk in enumerate(chunks)
        )
    
    user_message = f"{context}\n\nQuestion:\n{query}"
    
    messages = [{"role": "system", "content": system}]

    if history:
        for msg in history:
            messages.append({"role": msg["role"], "content": msg["content"]})

    messages.append({"role": "user", "content": user_message})

    return messages

