from transformers import pipeline

# Load once
summarizer_pipeline = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-12-6"
)

MAX_CHUNK_WORDS = 700  # safe size


def chunk_text(text, chunk_size=MAX_CHUNK_WORDS):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])


def generate_summary(text: str) -> str:
    summaries = []

    for chunk in chunk_text(text):
        result = summarizer_pipeline(
            chunk,
            max_length=150,
            min_length=40,
            do_sample=False
        )
        summaries.append(result[0]['summary_text'])

    # Final summary pass for coherence
    final_summary = summarizer_pipeline(
        " ".join(summaries),
        max_length=200,
        min_length=60,
        do_sample=False
    )

    return final_summary[0]['summary_text']