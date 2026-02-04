from ollama import chat

def trim_history(history, model):
    
    system = """
    You are an expert at summarizing conversations.
    Preserve all important context and facts.
    """

    messages = [{"role": "system", "content": system}]
    messages.extend(history)

    messages.append({
        "role": "user",
        "content": "Summarize the conversation above."
    })

    response = chat(model=model, messages=messages)
    summary = response["message"]["content"]

    return [{
        "role": "assistant",
        "content": summary
    }]

