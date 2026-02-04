import  json
from    scripts.memory import update_history
from    scripts.retrieval import retrieve
from    sentence_transformers import SentenceTransformer
from    scripts.prompt import build_prompt
#from    scripts.llm import generate
from    scripts.answer import generate
from    scripts.token_length import calculate_tokens
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

        prompt = build_prompt(
                query=user_input,
                chunks=retrieved_chunks,
                history=history
                )
        
        print("\nprompt so far  : \n", prompt)
        print("tokens used : ", calculate_tokens(prompt), "\n")
        
        start = time.time()
        response = generate(prompt, model="qwen3:4b-instruct-2507-q4_K_M")
        end = time.time()
        answer = response.message.content
        
        print("\nAssistant : \n", answer, "\n")
        print(f"Time taken: {end-start:.2f} sec")
        
        history = update_history(history, user_input, answer)

        print("\nhistory : ")
        for msg in history:
            print(f"{msg['role']} : {msg['content']}")


if __name__ == "__main__":
    main()
