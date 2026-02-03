from ollama import chat

def generate(prompt, model="mistral"):
    response = chat(
            model=model,
            messages=prompt
            )
    return response
