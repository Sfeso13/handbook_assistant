from transformers import AutoTokenizer

def calculate_tokens(prompt):
    prompt = str(prompt)
   # tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen3-4B-Instruct-2507")
   # tokens = tokenizer.encode(prompt)
    return len(prompt.split()) * 1.3
