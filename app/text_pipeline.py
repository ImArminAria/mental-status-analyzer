import torch
from .models import tokenizer, text_model
from .config import DEVICE
from .openai_client import analyze_with_gpt
from .summarizer import summarize_text


labels = ["Anxiety", "Depression", "Normal", "Suicidal"]


def analyze_text(text, enable_summarization: bool = True):

    if not text or not text.strip():
        return {"error": "Please enter text."}

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = text_model(**inputs)
        pred = outputs.logits.argmax(-1).item()

    bert_label = labels[pred]


    if enable_summarization:
        processed_text = summarize_text(text)
    else:
        processed_text = text

  
    gpt_result = analyze_with_gpt(processed_text)

    return {
        "bert_prediction": bert_label,
        "summarization_enabled": enable_summarization,
        "original_word_count": len(text.split()),
        "processed_word_count": len(processed_text.split()),
        "gpt_analysis": gpt_result
    }