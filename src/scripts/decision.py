from scripts.embedding import embed
import numpy as np
from ollama import embeddings
from ollama import chat

def normalize(v):
    return v / np.linalg.norm(v)

def cosine(a, b):
    return np.dot(a, b)


def llm_decide(query):
    system = f"""You classify user intent. The system you are working on is created to answer queries about official handbook rules and policies as well as the life in a coding school called '1337'.

If the question requires factual information about the school, official handbook rules or policies, output:
RETRIEVAL

Otherwise output:
CHAT
"""

    print("\nLLM DECISION\n")
    messages = [{"role": "system", "content": system}]
    messages.append({"role": "user", "content": query})
    response = chat(
            model="qwen3:2b-rag",
            messages=messages
            )
    return response.message.content


def route_query(query, model):
    """
    Decide wether the query needs retrieval or not.
    """

    retrieval_intent = normalize(
            embeddings(
                model=model,
                prompt="Questions about 1337 coding school, official rules, policies, procedures, requirements or overall enquiries about the life in 1337 campus"
            )["embedding"])
    chat_intent = normalize(
            embeddings(
                model=model,
                prompt="Greetings, Casual conversation, explanations, summaries, or general discussion"
            )["embedding"])

    query_embed = normalize(
            embeddings(
                model=model,
                prompt=query
            )["embedding"])

    s_retrieve = cosine(query_embed, retrieval_intent)
    s_chat = cosine(query_embed, chat_intent)

    margin = abs(s_retrieve - s_chat)
    print("\nmargin : ", margin, "\n")

    if margin > 0.15:
        decision = "retrieval" if s_retrieve > s_chat else "chat"
    else:
        decision = llm_decide(query)

    return decision

