import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    WhisperProcessor,
    WhisperForConditionalGeneration
)
from .config import MODEL_NAME, ASR_MODEL, HF_TOKEN, DEVICE

# Text Model
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, token=HF_TOKEN)
text_model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, token=HF_TOKEN)
text_model.to(DEVICE)
text_model.eval()

# Whisper
processor = WhisperProcessor.from_pretrained(ASR_MODEL)
whisper_model = WhisperForConditionalGeneration.from_pretrained(ASR_MODEL)
whisper_model.to(DEVICE)
whisper_model.eval()