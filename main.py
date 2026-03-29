import os

from dotenv import load_dotenv
import gradio as gr
import ollama
from pypdf import PdfReader

load_dotenv(override=True)

OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "gemma3:4b")
OLLAMA_HOST = os.getenv("OLLAMA_HOST", "http://127.0.0.1:11434")
_ollama = ollama.Client(host=OLLAMA_HOST)
reader = PdfReader("bhagavad-gita-in-english-source-file.pdf")
gita = ""
for page in reader.pages:
    text = page.extract_text()
    if text:
        gita += text

system_prompt = f"""You are a careful reader and guide for the Bhagavad Gita. Users ask questions about its meaning, themes, characters, and teachings.

Ground every answer in the English source text below. When responding:
- Explain what the text says; paraphrase clearly when it helps understanding.
- When the source names a chapter, speaker, or idea, stay consistent with that wording unless you are clearly summarizing.
- If the provided text does not contain enough information to answer, say so plainly instead of inventing verses, chapter numbers, or details.
- Use a respectful, clear tone appropriate for philosophical and spiritual discussion.

## Bhagavad Gita (English source text)

{gita}
"""

def chat(message, history):
    # history is prior turns only (role/content dicts); message is the new user input (Gradio ChatInterface).
    prior = [{"role": m["role"], "content": m["content"]} for m in history if m.get("content")]
    messages = [{"role": "system", "content": system_prompt}] + prior + [
        {"role": "user", "content": message}
    ]
    response = _ollama.chat(model=OLLAMA_MODEL, messages=messages)
    return response["message"]["content"]


if __name__ == "__main__":
    demo = gr.ChatInterface(
        fn=chat,
        title="Bhagavad Gita Q&A",
        description="Ask about the text, then follow up with clarifications or deeper questions. Each reply uses the full conversation so far.",
        examples=[
            "What is the Bhagavad Gita mainly about?",
            "What does Krishna tell Arjuna about duty?",
        ],
    )
    demo.launch()