# 🩺 Medical Assistant AI — Retrieval-Augmented Medical Question Answering System

A production-ready **Medical AI Assistant** built using **FastAPI, LangChain, Pinecone, Gemini Embeddings, and Groq LLM** that enables users to upload medical documents and interact with them through natural language conversations.

Instead of relying solely on an LLM's pre-trained knowledge, the system implements **Retrieval-Augmented Generation (RAG)** to retrieve relevant information from uploaded medical literature and generate accurate, context-aware responses with source references.

---

## 🚀 Overview

Medical professionals, students, and researchers often need to extract specific information from lengthy medical documents.

This project solves that challenge by combining:

* Semantic Search
* Vector Databases
* Large Language Models
* Retrieval-Augmented Generation (RAG)

Users can upload medical PDFs and ask questions in plain English. The assistant retrieves the most relevant document chunks and generates answers grounded in the uploaded content.

---

## ✨ Features

### 📄 Intelligent Document Processing

* Upload single or multiple medical PDFs
* Automatic document parsing and preprocessing
* Recursive text chunking for optimized retrieval

### 🔍 Semantic Search

* Gemini Embedding Model for vector generation
* Meaning-based retrieval instead of keyword matching
* Highly relevant context extraction

### 🧠 Retrieval-Augmented Generation (RAG)

* Context-aware answer generation
* Reduced hallucinations
* Responses grounded in uploaded medical documents

### ⚡ FastAPI Backend

* RESTful API architecture
* High-performance asynchronous endpoints
* Easy integration with frontend applications

### ☁️ Vector Database Integration

* Pinecone-powered vector storage
* Scalable similarity search
* Fast retrieval of relevant chunks

### 📚 Source Attribution

* Returns document sources used for answering
* Improved transparency and trustworthiness

### 🛡️ Production-Oriented Design

* Modular codebase
* Centralized logging
* Global exception handling
* Environment-based configuration

---

## 🏗️ System Architecture

```text
                  ┌──────────────────┐
                  │  Medical PDFs    │
                  └─────────┬────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Document Processing │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │    Text Chunking    │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Gemini Embeddings   │
                 └─────────┬───────────┘
                           │
                           ▼
                 ┌─────────────────────┐
                 │ Pinecone Vector DB  │
                 └─────────┬───────────┘


     User Question
            │
            ▼
 ┌─────────────────────────────┐
 │ Similarity Search Retrieval │
 └──────────────┬──────────────┘
                │
                ▼
 ┌─────────────────────────────┐
 │ Context Construction (RAG)  │
 └──────────────┬──────────────┘
                │
                ▼
 ┌─────────────────────────────┐
 │   Groq GPT-OSS-120B LLM     │
 └──────────────┬──────────────┘
                │
                ▼
        Context-Aware Answer
```

---

## 🛠️ Technology Stack

| Layer           | Technology           |
| --------------- | -------------------- |
| Backend API     | FastAPI              |
| LLM             | Groq GPT-OSS-120B    |
| Embeddings      | Gemini Embedding-001 |
| Vector Database | Pinecone             |
| Orchestration   | LangChain            |
| Server          | Uvicorn              |
| Language        | Python               |

---

## 📂 Project Structure

```bash
medical-assistant-ai/
│
├── backend/
│   │
│   ├── main.py
│   ├── logger.py
│   │
│   ├── middleware/
│   │   └── exception_handlers.py
│   │
│   ├── routes/
│   │   ├── upload_pdfs.py
│   │   └── ask_question.py
│   │
│   ├── services/
│   │   ├── pdf_handler.py
│   │   ├── vectorstore.py
│   │   ├── query_handler.py
│   │   └── llm.py
│   │
│   ├── uploaded_docs/
│   │
│   └── requirements.txt
│
├── client/
│   │
│   ├── app.py
│   ├── config.py
│   │
│   ├── components/
│   │   ├── upload_section.py
│   │   ├── chat_section.py
│   │   └── sidebar.py
│   │
│   ├── utils/
│   │   └── api_client.py
│   │
│   └── requirements.txt
│
├── .env
├── .gitignore
├── README.md
└── LICENSE
---

## 🎯 Key Engineering Highlights

✅ End-to-End RAG Pipeline

✅ Semantic Retrieval using Vector Embeddings

✅ Production-Ready FastAPI Architecture

✅ Scalable Pinecone Vector Storage

✅ Source-Grounded AI Responses

✅ Modular and Maintainable Codebase

✅ Logging & Exception Management

✅ REST API Integration Support

---

## 🔮 Future Improvements

* Multi-turn Conversational Memory
* User Authentication & Authorization
* Docker & Kubernetes Deployment
* Medical Citation Highlighting
* Document Versioning
* Multi-User Knowledge Bases
* Frontend Dashboard (React/Next.js)
* Streaming Responses

---

## 👨‍💻 Author

### Atin Choudhary
