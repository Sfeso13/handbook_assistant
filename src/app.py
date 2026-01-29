import  json
from    scripts.retrieval import retrieve
from    sentence_transformers import SentenceTransformer
from    scripts.prompt import build_prompt
from    scripts.llm import generate

import time, psutil, os

# Track your process
#pid = os.getpid()
#proc = psutil.Process(pid)
#
#def log_resources(prefix=""):
#    mem = proc.memory_info().rss / 1e9  # in GB
#    cpu = proc.cpu_percent(interval=None)
#    print(f"{prefix} CPU: {cpu:.1f}% | RAM: {mem:.2f}GB")
#
# Example query list

queries = [
    "I am already working at a company in casablanca, can I still join 1337 and get the benifits?",
]

model = SentenceTransformer("all-MiniLM-L6-v2")

for q in queries:
    # Step 1: retrieve relevant chunks
    chunks = retrieve(q, model, k=5)
    for chunk in chunks:
        print(chunk["path"])

    # Step 2: build prompt
    prompt = build_prompt(q, chunks)

    # Step 3: log memory before generation
    log_resources(f"Before query '{q}'")

    # Step 4: measure generation time
    start = time.time()
    answer = generate(prompt)
    end = time.time()

    # Step 5: log memory and time after generation
    log_resources(f"After query '{q}'")
    print(f"Query: {q}")
    print(f"Time taken: {end-start:.2f} sec")
    print(f"Answer: {answer}")
    print("-"*50)



