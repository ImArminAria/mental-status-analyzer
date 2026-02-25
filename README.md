# 🧠 Psychologist Assistant
AI-Based Clinical Conversation Processing System

---

## 📌 Overview

Psychologist Assistant is an AI-powered support system designed to process and analyze segments of psychotherapy sessions.

The system allows professionals to upload therapist–patient conversation segments in text or audio format and receive structured analytical insights using natural language processing models.

This tool supports clinical workflow and does not replace professional judgment.

---

## 🎙 Supported Input Types

- **Text Input**
  - Therapy session transcripts
  - Written clinical notes

- **Audio Input**
  - Uploaded WAV session segments
  - Automatic speech-to-text transcription
  - NLP-based semantic analysis

---

## ⚙️ Processing Pipeline

1. Audio (if provided) is transcribed using a speech recognition model.
2. The transcript is analyzed using a transformer-based classifier.
3. Psychological indicators are extracted.
4. Structured JSON output is generated for review.

---

## 🏗 Architecture

- Speech-to-Text Module (ASR)
- Transformer-based Classification (BERT)
- LLM-based Structured Analysis
- Gradio User Interface

The architecture separates transcription, classification, and reasoning layers to ensure modularity and scalability.

---

## 🛠 Tech Stack

- Python  
- PyTorch  
- HuggingFace Transformers  
- OpenAI API  
- Gradio  
- Librosa  

---

## 📂 Project Structure

```
psychologist-assistant/
│
├── app/
│   ├── config.py
│   ├── models.py
│   ├── text_pipeline.py
│   ├── audio_pipeline.py
│   ├── openai_client.py
│   └── ui.py
│
├── prompts/
│   └── system_prompt.txt
│
├── assets/
│   ├── ui_text.png
│   ├── ui_audio.png
│   └── english_test.png
│
├── run.py
├── requirements.txt
└── README.md
```

---

## 🚀 Setup

```bash
git clone <repository-url>
cd psychologist-assistant
pip install -r requirements.txt
python run.py
```

If required, create a `.env` file:

```
OPENAI_API_KEY=your_key_here
HF_TOKEN=your_token_here
```

---

## 📊 Output

The system generates structured JSON output including:

- Emotional state indicators
- Risk signals
- Cognitive patterns
- Behavioral markers

This output is intended for professional review and structured documentation.

---

## ⚠️ Disclaimer

This project is intended for research and demonstration purposes only.

It does not provide medical diagnosis and must not be used as a substitute for professional psychiatric or psychological evaluation.