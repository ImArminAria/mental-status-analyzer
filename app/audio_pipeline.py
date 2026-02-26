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

    return transcription.strip()


def analyze_audio(audio_file, enable_summarization: bool = True):

    transcript = transcribe_audio(audio_file)

    if transcript is None or not transcript.strip():
        return {"error": "No valid audio transcription produced."}

    analysis = analyze_text(
        transcript,
        enable_summarization=enable_summarization
    )

    return {
        "transcript": transcript,
        "analysis": analysis
    }