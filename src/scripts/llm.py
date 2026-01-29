import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def generate(prompt, model="mistral"):
    payload = {
            "model": model,
            "prompt": prompt,
            "stream": False,
            "temperature": 0.0
            }
    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"]
