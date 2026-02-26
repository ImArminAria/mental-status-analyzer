from transformers import pipeline
from functools import lru_cache
from .config import SUMMARIZER_MODEL


@lru_cache()
def load_summarizer():
    return pipeline(
        "summarization",
        model=SUMMARIZER_MODEL,
        device=-1
    )


def summarize_text(
    text: str,
    max_length: int = 250,
    min_length: int = 80,
    threshold_words: int = 180
):

    if not text:
        return text

    if len(text.split()) < threshold_words:
        return text

    summarizer = load_summarizer()

    summary = summarizer(
        text,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return summary[0]["summary_text"]