import gradio as gr
from transformers import pipeline

# Load a text generation pipeline from Hugging Face
generator = pipeline("text-generation", model="gpt2")

def generate_idea(topic):
    prompt = f"Create an innovative AI startup idea related to: {topic}."
    result = generator(prompt, max_length=60, num_return_sequences=1)
    return result[0]['generated_text']

# Gradio UI
iface = gr.Interface(
    fn=generate_idea,
    inputs=gr.Textbox(placeholder="e.g. healthcare, education, finance..."),
    outputs="text",
    title="💡 AI Startup Idea Generator",
    description="Enter a domain and get a fresh AI-based startup idea!"
)

if __name__ == "__main__":
    iface.launch()
