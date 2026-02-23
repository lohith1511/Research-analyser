from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil

from pdf_utils import extract_text_from_pdf
from summarizer import generate_summary
from keyword_extractor import extract_keywords
from embeddings import get_embedding_model
from vector_store import index_text_chunks, load_faiss_index
from qa_engine import answer_question

app = FastAPI(title="AI Research Assistant API")

# Setup CORS for Frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("uploads", exist_ok=True)

class QuestionRequest(BaseModel):
    question: str

CURRENT_DOCUMENT_TEXT = ""

@app.post("/upload-paper")
async def upload_paper(file: UploadFile = File(...)):
    global CURRENT_DOCUMENT_TEXT
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    file_path = f"uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        
    try:
        text = extract_text_from_pdf(file_path)
        if not text.strip():
            raise HTTPException(status_code=400, detail="Could not extract text from the PDF.")
            
        CURRENT_DOCUMENT_TEXT = text
        keywords = extract_keywords(text)
        index_text_chunks(text)
        
        return {
            "message": "Paper uploaded and processed successfully!",
            "filename": file.filename,
            "keywords": keywords
        }
    except Exception as e:
        import traceback
        print("ERROR TRACEBACK:")
        print(traceback.format_exc())
        raise HTTPException(status_code=500, detail=str(e))
@app.post("/summarize")
async def summarize_paper():
    global CURRENT_DOCUMENT_TEXT
    if not CURRENT_DOCUMENT_TEXT:
        raise HTTPException(status_code=400, detail="No document uploaded yet.")
    try:
        summary = generate_summary(CURRENT_DOCUMENT_TEXT)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ask-question")
async def ask_question(request: QuestionRequest):
    global CURRENT_DOCUMENT_TEXT
    if not CURRENT_DOCUMENT_TEXT:
        raise HTTPException(status_code=400, detail="No document uploaded yet.")
    try:
        answer = answer_question(request.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/keywords")
async def get_keywords():
    global CURRENT_DOCUMENT_TEXT
    if not CURRENT_DOCUMENT_TEXT:
        return {"keywords": []}
    keywords = extract_keywords(CURRENT_DOCUMENT_TEXT)
    return {"keywords": keywords}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=9090, reload=True)
