# 🤖handbook_assistant

A Retrieval-Augmented Generation (RAG) system designed for efficiently querying a structured handbook.

**what to expect next**:
- Expanding "Knowledge base" to include 42-related informations and overall general facts and rules any 42/1337 student need to be aware of.
- Web app UI for ease of use with intra account login.
- Possibility of choosing your own **embedding** and **LLM** models.
---

## 📋 Table of Contents
- [About](#-about)
- [Features](#-features)
- [System Architecture](#-system-architecture)
- [Project Structure](#-project-structure)
- [Setup](#-setup)
- [Usage](#-usage)

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Film%20Projector.png" alt="Film Projector" width="25" height="25" /> About

**handbook_assistant** is a local Retrieval-Augmented Generation (RAG) system built to answer questions related to 1337 coding school using its official handbook and internal documentation.
The system combines:
- Structured document chunking
- Dense vector embeddings
- Semantic search with FAISS
- Local LLM inference via Ollama

It is designed to only answer questions related to 1337, while rejecting unrelated queries or instructions.

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Control%20Knobs.png" alt="Control Knobs" width="25" height="25" /> Features
- ✅ Hierarchical markdown chunking (H1 / H2 aware)
- ✅ Token-aware chunk splitting for embeddings
- ✅ Local embeddings using nomic-embed-text
- ✅ Vector search with FAISS
- ✅ Query routing (retrieval vs chat)
- ✅ Ollama-based local LLM inference
- ✅ Strict scope enforcement (1337-only answers)
- ✅ Modular and extensible design

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Alien%20Monster.png" alt="Alien Monster" width="25" height="25" /> System Architecture

```
User Query
    │
    ▼
Query Router (Embedding Similarity / LLM fallback)
    ├── Chat → Generic LLM (scope-limited)
    └── Retrieval
          ├── Embed query
          ├── FAISS similarity search
          ├── Retrieve top-k chunks
          └── LLM answers using retrieved context

```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Card%20File%20Box.png" alt="Card File Box" width="25" height="25" /> Project Structure

<details>
   <summary>Click to expand</summary>

```
.
├── data/
│   ├── cleaned/
│   │   └── handbook_clean.md
│   ├── chunked/
│   │   └── handbook_chunked.jsonl
│   ├── index/
│   │   ├── handbook.faiss
│   │   └── metadata.json
│   ├── processed/
│   │   ├── images/
│   │   └── handbook.md
│   └── raw/
│       └── handbook.pdf
├── src/
│   ├── chat_retrieve.py
│   ├── cli_app.py
│   ├── prep_data.py
│   └── scripts/
│       ├── chunker.py
│       ├── answer.py
│       ├── clean_md.py
│       ├── memory.py
│       ├── pdf_to_md.py
│       ├── prompt.py
│       ├── trim_history.py
│       ├── embedding.py
│       ├── retrieval.py
│       ├── decision.py
│       └── token_length.py
├── README.md
└── requirements.txt
  
```
</details>

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Gear.png" alt="Gear" width="25" height="25" /> Setup

1. **Clone the repository**
```bash
git clone https://github.com/Sfeso13/handbook_assistant.git
cd handbook_assistant
```
2. **Create and activate a virtual environment**
```bash
python3 -m venv venv
source venv/bin/activate
```
3. **Install dependencies**
```bash
pip install -r requirements.txt
```

Make sure [ollama](https://ollama.com/download) is installed and running locally.

4. **Pull required models**
```bash
ollama pull qwen3:4b-instruct-2507-q4_K_M
ollama pull sanruss/qwen3-2b-rag
ollama pull nomic-embed-text-v2-moe
```

---

## <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Objects/Abacus.png" alt="Abacus" width="25" height="25" /> Usage
1. **Start the assistant**
```bash
python3 src/cli_app.py
```
2. **Query to your heart contents**
