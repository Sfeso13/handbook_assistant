from scripts.trim_history import trim_history
from scripts.token_length import calculate_tokens

def update_history(history, query, response, MAX_MEMORY_TOKENS=300, model="qwen3:4b-instruct-2507-q4_K_M"):

    mem = history
    
    mem.append({"role": "user", "content": query})
    mem.append({"role": "assistant", "content": response})
    
    if calculate_tokens(mem) >= MAX_MEMORY_TOKENS:
        mem = trim_history(mem, model)

    return mem
