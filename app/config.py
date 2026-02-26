import os
import torch


MODEL_NAME = "mental/mental-bert-base-uncased"
ASR_MODEL = "openai/whisper-base"
SUMMARIZER_MODEL = os.getenv(
    "SUMMARIZER_MODEL",
    "sshleifer/distilbart-cnn-12-6"
)


HF_TOKEN = os.getenv("HF_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


USE_MOCK_GPT = os.getenv("USE_MOCK_GPT", "true").lower() == "true"
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")