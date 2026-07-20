# Internal Knowledge Assistant
### AI-Powered Retrieval System for 1337 Coding School

> **Project Type:** Retrieval-Augmented Generation (RAG)
>
> **Role:** Sole Developer
>
> **Status:** Completed Prototype

---

# Overview

This project was developed to solve a common problem faced by students at 1337 Coding School.

The school relies heavily on self-learning, with students expected to navigate a large collection of documentation, internal rules, project specifications, and operational guidelines independently. Although the information already existed, finding the right answer often meant manually searching through lengthy documents.

The goal of this project was to build an AI-powered knowledge assistant capable of answering questions directly from the school's documentation while avoiding hallucinations and remaining strictly within the scope of the available knowledge.

Rather than relying on the language model's general knowledge, every answer is generated from relevant sections of the official documentation.

---

# Business Problem

Students regularly needed answers to questions such as:

- What are the evaluation rules for this project?
- How many peer evaluations are required?
- What happens if I miss a deadline?
- What are the campus regulations?
- How does a specific project work?

Although the answers existed in the handbook, finding them often required searching through dozens of pages of documentation.

This resulted in:

- Time spent searching documentation
- Repeated questions between students
- Inconsistent answers
- Difficulty locating specific information

---

# Project Goals

The assistant was designed to:

- Provide instant answers from official documentation
- Eliminate unnecessary searching
- Reduce incorrect or inconsistent answers
- Restrict responses to verified information
- Operate entirely on a local machine

---

# Solution

The system indexes the school's documentation into a searchable knowledge base.

When a question is asked, it:

1. Understands the user's query.
2. Searches the documentation for relevant information.
3. Retrieves the most relevant sections.
4. Uses those sections as context to generate the answer.

Because every response is grounded in retrieved documentation, the assistant avoids relying on the model's memory or external knowledge.

---

# System Architecture

```
User Question

↓

Query Analysis

↓

Semantic Search

↓

Retrieve Relevant Documentation

↓

Language Model

↓

Grounded Response
```

---

# Key Design Decisions

## Built Without Large RAG Frameworks

One design decision I intentionally made was implementing the retrieval pipeline myself rather than relying on frameworks such as LangChain or LlamaIndex.

This provided much finer control over:

- document preprocessing
- chunking strategy
- embedding generation
- retrieval behavior
- prompt construction
- context management

Building the pipeline from scratch also made the system easier to understand, debug, and optimize.

---

## Structured Document Processing

Instead of treating the handbook as plain text, the system preserves the document hierarchy during processing.

Sections are split according to headings before being converted into searchable chunks.

This improves retrieval accuracy while maintaining the context of each section.

---

## Local-First Architecture

The assistant was designed to operate entirely locally.

Benefits include:

- No external document uploads
- Improved privacy
- Lower operating costs
- Offline operation
- Full control over the models

---

# Technologies

The project combines several AI components:

- Dense vector embeddings for semantic understanding
- FAISS for similarity search
- Local language models through Ollama
- Custom document processing pipeline
- Structured markdown chunking

---

# Workflow

```
Documentation

↓

Preprocessing

↓

Hierarchical Chunking

↓

Embedding Generation

↓

Vector Index

──────────────────────

User Question

↓

Embedding

↓

Similarity Search

↓

Top Matching Chunks

↓

Language Model

↓

Final Answer
```

---

# Outcome

The completed system allows students to retrieve accurate information from the school's documentation within seconds instead of manually searching through large documents.

More importantly, the assistant answers using retrieved evidence rather than relying on the language model's general knowledge, producing more reliable and verifiable responses.

---

# Lessons Learned

This project reinforced an important principle of AI system design:

The quality of a retrieval system depends less on the language model itself and more on how information is prepared, retrieved, and presented to the model.

By implementing the retrieval pipeline from scratch, I gained complete control over every stage of the system while producing a modular architecture that can easily be adapted to other knowledge bases.
