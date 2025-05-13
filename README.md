📄 PDF Chat WebApp — RAG with Perplexity API
This is a lightweight Retrieval-Augmented Generation (RAG) web application that lets users upload a PDF document and ask natural language questions about its content. It uses the Perplexity API for generation and PyMuPDF for PDF parsing.

Built with ❤️ using Python + Gradio.

🔧 Features
📁 Upload any PDF (contracts, policies, reports, etc.)

🧠 Ask natural language questions (e.g., "What are the refund terms?")

🤖 Uses Perplexity’s sonar-small-online model to answer from context

🖥️ Clean web interface via Gradio

🚀 Demo
<p align="center"> <img src="https://i.imgur.com/7mJy3NK.png" alt="Demo UI" width="600"/> </p>
📦 Installation
Clone the repository (or just save the script):

bash
Copy
Edit
git clone https://github.com/yourusername/pdf-chat-perplexity.git
cd pdf-chat-perplexity
Install dependencies:

bash
Copy
Edit
pip install gradio pymupdf requests
Add your Perplexity API Key:
Edit the script and replace:

python
Copy
Edit
API_KEY = "YOUR_PERPLEXITY_API_KEY"
▶️ Running the App
bash
Copy
Edit
python rag_webapp.py
Then open the local server in your browser (typically http://127.0.0.1:7860).

📁 Project Structure
bash
Copy
Edit
.
├── rag_webapp.py       # Main Gradio app
├── sample.pdf          # (Optional) Example PDF for testing
├── README.md           # You're reading this!
⚙️ Configuration
Model: By default, uses "sonar-small-online"

You can switch to other models supported by Perplexity (e.g., LLaMA 3, Claude, GPT) by updating:

python
Copy
Edit
payload["model"] = "desired-model-id"
📚 See available models: Perplexity API Docs

📌 Limitations
Only the first 10 chunks (~5,000 tokens) of the PDF are sent to stay within model context limits

Very large PDFs may be partially processed unless paging is added

Requires a valid Perplexity API key (visit perplexity.ai)

🛡️ License
MIT License

🙌 Acknowledgments
Perplexity API

Gradio

PyMuPDF

