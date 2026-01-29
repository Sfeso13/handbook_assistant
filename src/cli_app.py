import  json
from    scripts.retrieval import retrieve
from    sentence_transformers import SentenceTransformer
from    scripts.prompt import build_prompt
from    scripts.llm import generate
import time

def main():
    
    model = SentenceTransformer("all-MiniLM-L6-v2")
    history = []

    while True:
        user_input = input(">>").strip()
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

        start = time.time()
        response = generate(prompt)
        end = time.time()
        
        print("\nAssistant : \n", response, "\n")
        print(f"Time taken: {end-start:.2f} sec")
        
        history.append(("user", user_input))
        history.append(("assistant", response))


if __name__ == "__main__":
    main()
