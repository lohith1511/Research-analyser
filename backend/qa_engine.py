from vector_store import get_relevant_chunks
from transformers import pipeline

qa_pipeline = None


def get_qa_pipeline():
    global qa_pipeline
    if qa_pipeline is None:
        qa_pipeline = pipeline(
            "question-answering",
            model="distilbert-base-cased-distilled-squad"
        )
    return qa_pipeline


def answer_question(question: str) -> str:
    try:
        relevant_chunks = get_relevant_chunks(question, top_k=3)

        if not relevant_chunks:
            return "I don't have enough context to answer this question."

        # Merge context safely
        context = " ".join(relevant_chunks)

        # Limit context length to avoid tokenizer crash
        context = context[:1500]

        qa = get_qa_pipeline()

        result = qa(question=question, context=context)

        answer = result.get("answer", "").strip()
        print("QUESTION:", question)
        print("CHUNKS:", relevant_chunks)

        if not answer:
            return "I couldn't find a clear answer in the document."

        return answer

    except Exception as e:
        import traceback
        print("\n===== QA ERROR TRACEBACK =====")
        print(traceback.format_exc())
        print("===== END ERROR =====\n")
        return "Sorry, I couldn't process your question."