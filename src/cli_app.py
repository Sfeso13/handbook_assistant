import  json
from    scripts.retrieval import retrieve
from    sentence_transformers import SentenceTransformer
from    scripts.prompt import build_prompt
#from    scripts.llm import generate
from    scripts.answer import generate
from    scripts.token_length import calculate_tokens
from    scripts.trim_history import trim_history
import  time

MAX_TOKENS = 200

def main():
    
    model = SentenceTransformer("all-MiniLM-L6-v2")
    history = []

    while True:
        user_input = input(">> ").strip()
        if user_input.lower() in {"exit", "quit", "stop"}:
            break
        
        retrieved_chunks = retrieve(user_input, model)
        print("\nContext provided : \n")
        for chunk in retrieved_chunks:
            print(chunk["path"])

        if calculate_tokens(history) >= MAX_TOKENS:
            history = trim_history(history, model="qwen3:4b-instruct-2507-q4_K_M")

        prompt = build_prompt(
                query=user_input,
                chunks=retrieved_chunks,
                history=history
                )
        
        print("\nhistory : ")
        for role, content in history:
            print("role: ", role)
            print("content :",content)

        print("\nprompt so far  : \n", prompt)
        print("tokens used : ", calculate_tokens(prompt), "\n")
        
        start = time.time()
        response = generate(prompt, model="qwen3:4b-instruct-2507-q4_K_M")
        end = time.time()
        answer = response.message.content
        
        print("\nAssistant : \n", answer, "\n")
        print(f"Time taken: {end-start:.2f} sec")
        
        history.append(("user", user_input))
        history.append(("assistant", answer))


if __name__ == "__main__":
    main()
