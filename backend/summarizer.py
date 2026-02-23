from transformers import pipeline

summarizer_pipeline = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
def generate_summary(text: str, max_length: int = 250, min_length: int = 50) -> str:
    """Generates a summary using HuggingFace Transformers."""
    input_text = text[:3000] # Adjust if needed
    summary = summarizer_pipeline(input_text, max_length=max_length, min_length=min_length, do_sample=False)
    return summary[0]['summary_text']
