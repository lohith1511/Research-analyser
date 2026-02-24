# 🔬 Research Analyser — AI Research Paper Assistant

An advanced AI-powered research assistant that enables users to upload research papers (PDF), extract meaningful concepts, generate high-quality summaries, and interact through a semantic search chatbot using **Retrieval Augmented Generation (RAG)**.

Designed as a placement-ready full-stack AI project demonstrating modern NLP pipelines, vector search, and semantic QA architecture.

---

## 🚀 Features

- 📄 Upload research papers in PDF format
- 🧠 Automatic text extraction and preprocessing
- 🔍 Keyword and concept extraction
- ✨ Abstractive summarization using Transformers
- ⚡ Semantic search with FAISS vector database
- 🤖 Retrieval Augmented Generation (RAG) pipeline
- 💬 Context-aware chatbot Q&A
- 🎨 Modern React UI

---

## 🛠 Tech Stack

### Backend
- FastAPI
- HuggingFace Transformers
- SentenceTransformers
- FAISS
- SpaCy
- Python

### Frontend
- React + Vite
- Axios
- CSS

---

## 📂 Project Structure

```
AI_Research_Assistant/
│
├── backend/
│   ├── __pycache__/
│   ├── uploads/
│   ├── venv/
│   ├── embeddings.py          # Generate sentence embeddings
│   ├── keyword_extractor.py   # Extract keywords using SpaCy
│   ├── main.py                # FastAPI entry point
│   ├── pdf_utils.py           # PDF text extraction
│   ├── qa_engine.py           # Question answering pipeline
│   ├── rag_engine.py          # Retrieval Augmented Generation logic
│   ├── summarizer.py          # Text summarization model
│   ├── vector_store.py        # FAISS vector operations
│   ├── requirements.txt       # Backend dependencies
│
├── frontend/
│   ├── node_modules/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot.jsx
│   │   │   ├── Loader.jsx
│   │   │   ├── Navbar.jsx
│   │   │   ├── Summary.jsx
│   │   │   ├── Upload.jsx
│   │   │
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   ├── styles.css
│   │
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   ├── vite.config.js
```

---

## 🧩 System Architecture

1️⃣ User uploads PDF  
2️⃣ Backend extracts text  
3️⃣ Keywords extracted using SpaCy  
4️⃣ Embeddings generated via SentenceTransformers  
5️⃣ Stored in FAISS vector database  
6️⃣ Summarizer generates concise overview  
7️⃣ RAG engine retrieves relevant chunks  
8️⃣ QA engine generates contextual answers  

---

## ⚙️ Backend Setup

Navigate to backend directory:

```bash
cd AI_Research_Assistant/backend
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

**Windows**
```bash
venv\Scripts\activate
```

**Mac/Linux**
```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run server:

```bash
python main.py
```

Backend runs at:

```
http://localhost:9090
```

---

## 🎨 Frontend Setup

Navigate to frontend directory:

```bash
cd AI_Research_Assistant/frontend
```

Install dependencies:

```bash
npm install
```

Run development server:

```bash
npm run dev
```

Open the URL shown in terminal.

---

## 🔗 API Integration

Frontend communicates with backend using Axios requests to:

```
http://localhost:9090
```

CORS is enabled to allow seamless communication.

---

## 🧠 Core Modules Explained

### 📄 pdf_utils.py
Handles PDF parsing and text extraction.

### 🔍 keyword_extractor.py
Extracts important keywords using SpaCy NLP pipeline.

### 🧬 embeddings.py
Generates vector embeddings using SentenceTransformers.

### 📦 vector_store.py
Stores and retrieves vectors using FAISS similarity search.

### ✨ summarizer.py
Generates abstractive summaries using HuggingFace models.

### 🔗 rag_engine.py
Implements Retrieval Augmented Generation by combining vector retrieval with context injection.

### 🤖 qa_engine.py
Generates context-aware answers using retrieved document chunks.

### 🚀 main.py
Defines API endpoints for upload, summarize, and chat.

---

## 📡 API Endpoints

| Method | Endpoint | Description |
|--------|---------|------------|
| POST | `/upload` | Upload PDF |
| GET | `/summary` | Generate summary |
| POST | `/chat` | Ask question |

---

## 💡 Use Cases

- Academic literature review
- Research paper understanding
- Knowledge discovery
- Semantic document search
- AI research assistant

---

## 🔮 Future Enhancements

- Multi-document knowledge base
- User authentication
- Cloud deployment (Docker + AWS)
- Streaming LLM responses
- Citation extraction
- PDF highlighting
- Conversation memory

---

## 🎓 Learning Outcomes

- Built end-to-end RAG pipeline
- Implemented vector search with FAISS
- Integrated Transformer models
- Designed scalable FastAPI backend
- Developed modern React frontend
- Implemented semantic search chatbot

---

## 👨‍💻 Author

AI Research Assistant Project  

---

## 📜 License

MIT License

---

⭐ If you found this project useful, consider giving it a star!