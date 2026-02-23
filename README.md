# Research Paper Summarization for Multi-Disciplinary Knowledge Discovery

An advanced, placement-ready AI Research Assistant system that allows users to upload PDF research papers, extracts text and concepts, generates intelligent summaries, and provides an interactive chatbot to ask real-time questions about the paper using Semantic Search.

## Folder Structure

```
AI_Research_Assistant/
├── backend/
│   ├── main.py                # FastAPI entry point
│   ├── summarizer.py          # HuggingFace summary generator
│   ├── pdf_utils.py           # Extracts text from incoming PDFs
│   ├── keyword_extractor.py   # Spacy keyword extraction
│   ├── embeddings.py          # SentenceTransformers for embeddings
│   ├── vector_store.py        # FAISS database operations
│   ├── qa_engine.py           # Open-ended QA generation
│   ├── requirements.txt       # Python dependencies
│   └── uploads/               # Directory where uploaded PDFs are stored
└── frontend/
    ├── package.json           # Frontend dependency manifest
    ├── vite.config.js         # Vite configuration
    ├── index.html             # HTML entry point
    └── src/
        ├── main.jsx           # React DOM rendering
        ├── App.jsx            # Main Hub Screen layout
        ├── styles.css         # Modern AI UI premium dark theme
        └── components/        # Isolated modular React UI components
            ├── Navbar.jsx
            ├── Upload.jsx
            ├── Summary.jsx
            ├── Chatbot.jsx
            └── Loader.jsx
```

## How to run the Backend

The backend is powered by **FastAPI** and uses **HuggingFace**, **FAISS**, **SentenceTransformers**, and **SpaCy**.

1. Open a terminal and navigate to the backend folder:
   ```bash
   cd AI_Research_Assistant/backend
   ```
2. Create and activate a Virtual Environment (Optional but recommended):
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the development server (This will expose APIs on `localhost:9090`):
   ```bash
   python main.py
   ```
   *(Wait a bit on first upload/summarize for models to hit the cache).*

## How to run the Frontend

The frontend is an ultra-fast **React + Vite** app with dynamic glassmorphic styles.

1. Open a new terminal and navigate to the frontend folder:
   ```bash
   cd AI_Research_Assistant/frontend
   ```
2. Install dependencies (you can use npm/yarn):
   ```bash
   npm install
   ```
3. Start the dev server:
   ```bash
   npm run dev
   ```
4. Open your browser as instructed by Vite!

## How to connect both

They are pre-configured to automatically connect out-of-the-box! 
- The React Frontend automatically routes its HTTP POST requests directly to `http://localhost:9090/...` using the `axios` library inside components like `Upload.jsx`, `Chatbot.jsx`, and `Summary.jsx`.
- The FastAPI Backend has CORS enabled wide-open `allow_origins=["*"]` to ensure the frontend development port interacts smoothly without blocks.
"# Research-analyser" 
