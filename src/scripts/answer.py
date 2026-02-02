from ollama import chat

def generate(prompt, model="mistral"):
    response = chat(
            model=model,
            messages=[{'role': 'user', 'content': prompt}],
            think=False
            )
    return response
