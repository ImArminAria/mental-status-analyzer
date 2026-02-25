import os
import torch

MODEL_NAME = "mental/mental-bert-base-uncased"
ASR_MODEL = "openai/whisper-base"

HF_TOKEN = os.getenv("HF_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")