import fitz  # PyMuPDF
import gradio as gr
import requests

# Replace with your actual Perplexity API key
API_KEY = "your pplx api key"

# Extract text from uploaded PDF
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Split into chunks for long context
def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# Send context + query to Perplexity API
def ask_question(pdf_file, question):
    if not pdf_file:
        return "Please upload a PDF first."
    if not question.strip():
        return "Please enter a question."

    pdf_text = extract_text_from_pdf(pdf_file)
    context_chunks = split_text(pdf_text)
    context_str = "\n\n".join(context_chunks[:10])  # send only top 10 chunks to stay within token limits

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "sonar-small-online",  # use another model if you prefer
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant that answers questions based on the provided documents."
            },
            {
                "role": "user",
                "content": f"Here are some documents:\n\n{context_str}\n\nQuestion: {question}"
            }
        ]
    }

    response = requests.post("https://api.perplexity.ai/chat/completions", headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"❌ API Error {response.status_code}: {response.text}"

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("# 📄 Chat with Your PDF using Perplexity API")
    pdf_input = gr.File(label="Upload a PDF", file_types=[".pdf"])
    question_input = gr.Textbox(label="Ask a question about the document", placeholder="e.g. What is the refund policy?")
    answer_output = gr.Textbox(label="Answer")

    ask_btn = gr.Button("Ask")
    ask_btn.click(ask_question, inputs=[pdf_input, question_input], outputs=answer_output)

demo.launch()
