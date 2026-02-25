import torch
import json
from .models import tokenizer, text_model
from .config import DEVICE
from .openai_client import analyze_with_gpt

labels = ["Anxiety", "Depression", "Normal", "Suicidal"]

def analyze_text(text):

    if not text or not text.strip():
        return "Please enter text."

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

    gpt_result = analyze_with_gpt(text)

    return f"""🧠 MENTAL STATE:

BERT: {labels[pred]}

GPT:
{json.dumps(gpt_result, indent=2, ensure_ascii=False)}
"""