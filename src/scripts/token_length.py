from transformers import AutoTokenizer

def calculate_tokens(prompt):
    tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.2")
    tokens = tokenizer.encode(prompt)
    return len(tokens)
