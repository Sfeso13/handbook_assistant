import  json
from scripts.retrieval import retrieve
import  argparse
from    chat_retrieve import retrieve_prompt, chat_prompt
from    scripts.decision import route_query
from    scripts.memory import update_history
from    scripts.answer import generate
from    scripts.token_length import calculate_tokens
import  time
from rich.console import Console
from rich.spinner import Spinner
from rich.live import Live

def debug_print(console, debug, title, content):
    if not debug:
        return
    
    console.rule(f"[bold red]Debug : {title}")
    console.print(content)
    console.rule()

def main(console, debug=False):
    
    embed_model = "nomic-embed-text-v2-moe"
    history = []

    while True:
    
        user_input = input(">> ").strip()
        if user_input.lower() in {"exit", "quit", "stop"}:
            break
        
        start = time.time()
        with console.status("[bold cyan]Deciding..."):
            route = route_query(user_input, embed_model)
        
        if route.lower() == "retrieval":
            with console.status("[bold cyan]Retrieving context..."):
                retrieved_chunks = retrieve(user_input, embed_model)
                #debug
                debug_print(console, debug, "Retrieved chunks", retrieved_chunks)

                prompt = retrieve_prompt(user_input, history, retrieved_chunks=retrieved_chunks)
            
            console.print("[bold cyan]Context Retrieved!")
        else:
            prompt = chat_prompt(user_input, history)
        ##debug 
        debug_print(console, debug, "Constructed prompt", prompt)

        response_stream = generate(prompt, model="qwen3:4b-instruct-2507-q4_K_M", stream=True)
        with console.status("[bold green]Generating answer..."):
            first_chunk = next(response_stream)
        first_token = first_chunk["message"]["content"]
        answer = first_token
        
        console.print("[bold green]Assistant:[/bold green] ", end="")
        console.print(first_token, end="", soft_wrap=True)
        
        for chunk in response_stream:
            token = chunk["message"]["content"]
            answer += token
            console.print(token, end="", soft_wrap=True)
        
        console.print()
        end = time.time()
        console.print(f"[bold cyan]Generated in : {end - start:.2f} seconds", end="")
        console.print(f"", end="\n")
        
        with console.status("[bold green]Updating conversation history..."):
            history = update_history(history, user_input, answer)

        ##debug
        if debug:
            for msg in history:
                debug_print(console, debug, "Conversation history",  f"{msg['role']} : {msg['content']}")

def parse_args():
    parser = argparse.ArgumentParser(
        prog="assist-me",
        description="RAG CLI assistant"
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable debug output (prompts, context, history)"
    )
    return parser.parse_args()

if __name__ == "__main__":
    try:
        console = Console()
        args = parse_args()
        main(console, debug=args.debug)
    except KeyboardInterrupt:
        console.print("\n[dim]See ya![/dim]")
