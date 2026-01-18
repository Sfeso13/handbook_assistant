from transformers import AutoTokenizer


tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")

def approx_token_count(text: str) -> int:
    return len(tokenizer.encode(text))

MAX_TOKENS = 700
oversized = [ c for c in text if approx_token_count(c['content']) > MAX_TOKENS]

for chunk in oversized:
    print(f"Path : {chunk['path']}\ncontent : {chunk['content']}\n\n")
