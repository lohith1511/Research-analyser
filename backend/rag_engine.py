from transformers import pipeline
from vector_store import get_relevant_chunks

generator = None


def get_generator():
    global generator
    if generator is None:
        generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base"
        )
    return generator


def generate_answer(question: str):
    try:
        # Retrieve context
        chunks = get_relevant_chunks(question, top_k=5)

        if not chunks:
            return "I couldn't find relevant information in the document."

        context = " ".join(chunks)[:1200]

        prompt = f"""
You are an academic research assistant.

Using ONLY the context below, answer the question clearly in 2–3 sentences.
If the answer is not in the context, say you don't know.

Context:
{context}

Question: {question}

Answer:
"""

        gen = get_generator()

        output = gen(
            prompt,
            max_new_tokens=150,
            temperature=0.2,
            do_sample=False
        )

        answer = output[0]["generated_text"].strip()

        # Clean possible prefix
        if "Answer:" in answer:
            answer = answer.split("Answer:")[-1].strip()

        return answer

    except Exception as e:
        print("RAG ERROR:", e)
        return "Sorry, I couldn't generate an answer."