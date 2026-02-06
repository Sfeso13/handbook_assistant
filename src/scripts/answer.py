from ollama import chat

def generate(prompt, model="mistral", stream=False):
    return chat(
            model=model,
            messages=prompt,
            stream=stream
            )
