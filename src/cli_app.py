import  json
from    chat_retrieve import retrieve_prompt, chat_prompt
from    scripts.decision import route_query
from    scripts.memory import update_history
#from    scripts.llm import generate
from    scripts.answer import generate
from    scripts.token_length import calculate_tokens
import  time

def main():
    
    embed_model = "nomic-embed-text-v2-moe"
    history = []

    while True:
        user_input = input(">> ").strip()
        if user_input.lower() in {"exit", "quit", "stop"}:
            break
        
        if route_query(user_input, embed_model).lower() == "retrieval":
            prompt = retrieve_prompt(user_input, embed_model, history)
        else:
            prompt = chat_prompt(user_input, history)


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
