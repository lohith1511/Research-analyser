import spacy
from collections import Counter
from spacy.cli import download
import threading

nlp_model = None
lock = threading.Lock()

def get_nlp():
    global nlp_model
    with lock:
        if nlp_model is None:
            try:
                nlp_model = spacy.load("en_core_web_sm")
            except OSError:
                from spacy.cli import download
                download("en_core_web_sm")
                nlp_model = spacy.load("en_core_web_sm")
    return nlp_model

def extract_keywords(text: str, top_n: int = 10):
    """Extracts top keywords using SpaCy."""
    nlp = get_nlp()
    doc = nlp(text[:10000])  # limit text length for speed
    
    keywords = [
        token.text.lower()
        for token in doc
        if token.pos_ in ["NOUN", "PROPN"]
        and not token.is_stop
        and token.is_alpha
    ]

    most_common = Counter(keywords).most_common(top_n)
    return [word for word, count in most_common]