import gradio as gr
from .text_pipeline import analyze_text
from .audio_pipeline import analyze_audio


def text_handler(text, enable_summary):
    return analyze_text(text, enable_summarization=enable_summary)


def audio_handler(audio_file, enable_summary):
    return analyze_audio(audio_file, enable_summarization=enable_summary)


with gr.Blocks(
    theme=gr.themes.Soft(primary_hue="violet", neutral_hue="slate")
) as demo:

    gr.Markdown("# 🧠 Psychologist Assistant")

    enable_summary = gr.Checkbox(
        label="Enable cost-reduction summarization",
        value=True
    )


    gr.Markdown("## ✍️ Text Analysis")

    textbox = gr.Textbox(
        placeholder="Paste session text here...",
        lines=8,
        show_label=False
    )

    analyze_btn = gr.Button("Analyze Text", variant="primary")

    text_output = gr.JSON(label="Structured Analysis")

    analyze_btn.click(
        fn=text_handler,
        inputs=[textbox, enable_summary],
        outputs=text_output
    )


    gr.Markdown("## 🎙 Audio Analysis")

    audio_input = gr.Audio(
        type="filepath",
        label="Upload WAV file"
    )

    audio_btn = gr.Button("Analyze Audio")

    audio_output = gr.JSON(label="Structured Analysis")

    audio_btn.click(
        fn=audio_handler,
        inputs=[audio_input, enable_summary],
        outputs=audio_output
    )

    gr.Markdown(
        "⚠️ This AI system is not a medical professional. "
        "Results are probabilistic and for professional review only."
    )


if __name__ == "__main__":
    demo.launch()