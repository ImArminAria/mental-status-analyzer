import gradio as gr
from .text_pipeline import analyze_text
from .audio_pipeline import analyze_audio

with gr.Blocks(theme=gr.themes.Soft(primary_hue="violet", neutral_hue="slate")) as demo:

    gr.Markdown("# 🧠 Mental Status Analyzer")

    textbox = gr.Textbox(
        placeholder="Type text here...",
        lines=4,
        show_label=False
    )

    analyze_btn = gr.Button("Analyze Text", variant="primary")
    text_output = gr.Markdown()
    analyze_btn.click(analyze_text, textbox, text_output)

    gr.Markdown("## 🎙 Upload WAV File")

    audio_input = gr.Audio(type="filepath", label="Upload WAV")
    audio_btn = gr.Button("Analyze Audio")
    audio_output = gr.Markdown()

    audio_btn.click(analyze_audio, audio_input, audio_output)

    gr.Markdown(
        "⚠️ This AI is not a medical professional. Results are probabilistic."
    )