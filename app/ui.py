import gradio as gr
from .text_pipeline import analyze_text
from .audio_pipeline import analyze_audio

with gr.Blocks(theme=gr.themes.Soft(primary_hue="violet", neutral_hue="slate")) as demo:

    gr.Markdown("# 🧠 Psychologist Assistant")

    # -------- TEXT SECTION --------
    gr.Markdown("## ✍️ Text Analysis")

    textbox = gr.Textbox(
        placeholder="Paste session text here...",
        lines=5,
        show_label=False
    )

    analyze_btn = gr.Button("Analyze Text", variant="primary")

    text_output = gr.JSON(label="Structured Analysis")

    analyze_btn.click(
        fn=analyze_text,
        inputs=textbox,
        outputs=text_output
    )

    # -------- AUDIO SECTION --------
    gr.Markdown("## 🎙 Audio Analysis")

    audio_input = gr.Audio(type="filepath", label="Upload WAV")
    audio_btn = gr.Button("Analyze Audio")

    audio_output = gr.JSON(label="Structured Analysis")

    audio_btn.click(
        fn=analyze_audio,
        inputs=audio_input,
        outputs=audio_output
    )

    # -------- DISCLAIMER --------
    gr.Markdown(
        "⚠️ This AI is not a medical professional. Results are probabilistic."
    )