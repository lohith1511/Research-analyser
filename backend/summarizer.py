from transformers import pipeline

_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        _summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    return _summarizer


MAX_CHUNK_WORDS = 400


def chunk_text(text, chunk_size=MAX_CHUNK_WORDS):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        if len(chunk.strip()) > 50:  # skip tiny chunks
            yield chunk


def generate_summary(text: str) -> str:
    summarizer = get_summarizer()

    summaries = []

    for chunk in chunk_text(text):
        try:
            result = summarizer(
                chunk,
                max_length=120,
                min_length=30,
                do_sample=False
            )
            summaries.append(result[0]["summary_text"])
        except Exception as e:
            print("Skipping chunk due to error:", e)

    if not summaries:
        return "Could not generate summary — document too short or invalid."

    # Final merge
    try:
        final = summarizer(
            " ".join(summaries),
            max_length=180,
            min_length=50,
            do_sample=False
        )
        return final[0]["summary_text"]
    except:
        return " ".join(summaries)