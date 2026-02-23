from vector_store import get_relevant_chunks
from transformers import pipeline

qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(question: str) -> str:
    """Answers a question based on retrieved document chunks."""
    relevant_chunks = get_relevant_chunks(question, top_k=3)
    
    if not relevant_chunks:
        return "I don't have enough context to answer this question."
        
    context = " ".join(relevant_chunks)
    
    result = qa_pipeline(question=question, context=context)
    return result['answer']
