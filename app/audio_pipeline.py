import torch
import librosa
from .models import processor, whisper_model
from .config import DEVICE
from .text_pipeline import analyze_text

def transcribe_audio(audio_file):

    if audio_file is None:
        return None

    audio, sr = librosa.load(audio_file, sr=16000)

    inputs = processor(
        audio,
        sampling_rate=16000,
        return_tensors="pt"
    ).to(DEVICE)

    with torch.no_grad():
        predicted_ids = whisper_model.generate(inputs["input_features"])

    transcription = processor.batch_decode(
        predicted_ids,
        skip_special_tokens=True
    )[0]

    return transcription

def analyze_audio(audio_file):

    text = transcribe_audio(audio_file)

    if text is None:
        return "No audio file provided."

    return analyze_text(text)