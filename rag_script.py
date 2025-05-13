import fitz  # PyMuPDF
import requests

# STEP 1: Add your API key here
API_KEY = "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"  # Replace with your actual API key

# STEP 2: PDF Text Extraction
def extract_text_from_pdf(file_path):
    doc = fitz.open(file_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# STEP 3: Split text into chunks for context
def split_text(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

# STEP 4: Ask question using Perplexity API
def ask_with_context(question, context_docs):
    context_str = "\n\n".join(context_docs)
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "sonar-pro",
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
        return f"Error: {response.status_code} - {response.text}"

# STEP 5: Main function to run everything
if __name__ == "__main__":
    # File path to your PDF
    pdf_file = "google_health_impact (1).pdf"  # Replace with your PDF file name

    # Extract and split text
    print("Extracting text from PDF...")
    pdf_text = extract_text_from_pdf(pdf_file)
    context_docs = split_text(pdf_text)

    # Ask a question
    question = "Which organisations working in health meet future health needs. make a list of them"
    print(f"\nAsking: {question}\n")
    answer = ask_with_context(question, context_docs)

    print("\nAnswer:\n", answer)
