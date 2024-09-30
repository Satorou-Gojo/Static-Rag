# Static-Rag
Pathway RAG Application Using Streamlit UI
This project showcases how to build a Retrieval-Augmented Generation (RAG) application with Pathway and Streamlit, incorporating the Gemini API for NLP tasks.

Table of Contents
Overview
Key Features
Workflow
Pathway Tools
LLM Integration
Requirements
Installation Guide
Configuration Setup
Running the Application
Locally
Using Docker
Application Usage
Adding Your Own Data
Querying and Searching Documents
Question Answering (With or Without RAG)
Summarization
API Endpoints
Customization Options
Overview
This app blends the real-time document indexing and retrieval strengths of Pathway with the simplicity of Streamlit's UI. By leveraging the Gemini API for NLP tasks such as question-answering and summarization, the application delivers an always-up-to-date knowledge base for your LLM without requiring separate ETL processes.

Key Features
Query static documents in a local directory using RAG or without it.
Search through indexed documents with custom filters.
Display a list of all indexed documents and related metadata.
Summarize multiple text inputs simultaneously.
Workflow
Pathway connectors capture data from various sources (like local files, Google Drive, and SharePoint) with low-latency change detection. The unstructured library parses and divides binary objects into chunks, which are then embedded using the Gemini API.

The embeddings are indexed with Pathway's machine learning tools, allowing users to query the index through HTTP requests to specified endpoints.

Pathway Tools
Custom Prompts & UDFs: Pathway allows users to define prompts and stream operations using the @pw.udf decorator.
RAG Components: Pathway's toolkit includes a vector store and web server, enabling the complete setup for a RAG app.
Connectors: Seamless integration with various data sources.
LLM Integration
The app uses the Gemini API to:

Generate embeddings for document chunks.
Answer questions based on the retrieved context.
Summarize text inputs.
Different models within the Gemini API can be configured, providing flexibility in performance and cost management.

Requirements
Python 3.7 or newer
Pathway
Streamlit
Access to Gemini API
Installation Guide
Clone the repository:

bash
Copy code
git clone https://github.com/nrk-necro/pathway-rag-streamlit.git
cd pathway-rag-streamlit
Install the dependencies:

bash
Copy code
pip install -r requirements.txt
Configuration Setup
LLM Model
Configure the Gemini model in the config.yaml file:

yaml
Copy code
llm_config:
  model: "gemini/gemini-pro"
API Key
Store your Gemini API key in a .env file:

bash
Copy code
GEMINI_API_KEY=your_api_key_here
Running the Application
Using Docker
Build the Docker image:

bash
Copy code
docker build -t pathway-rag-streamlit .
Run the container:

bash
Copy code
docker run -v $(pwd)/data:/app/data -p 8000:8000 -p 8501:8501 pathway-rag-streamlit
Running Locally
To run locally, execute the following in a terminal:

bash
Copy code
streamlit run streamlit_app.py
Navigate to the Streamlit URL (usually http://localhost:8501) in your browser.

Application Usage
The Streamlit interface offers four key features:

Ask a Question: Submit questions, with or without using RAG and filters.
List Documents: Browse all indexed documents along with their metadata.
Summarize Texts: Input multiple texts for summary generation.
Adding Your Own Data
You can replace the default document, "Zombie Survival Guide - Complete Protection from the Living Dead.pdf", with your own files by adding them to the data folder.

Querying and Searching Documents
To list all indexed inputs with metadata, use this command:

bash
Copy code
curl -X POST 'http://localhost:8000/v1/pw_list_documents' -H 'accept: */*' -H 'Content-Type: application/json'
To search within your indexed documents:

bash
Copy code
curl -X POST 'http://localhost:8000/v1/retrieve' -H 'accept: */*' -H 'Content-Type: application/json' -d '{
  "query": "Your search query here",
  "k": 5
}'
Question Answering (With and Without RAG)
For asking questions using RAG:

bash
Copy code
curl -X POST 'http://localhost:8000/v1/pw_ai_answer' -H 'accept: */*' -H 'Content-Type: application/json' -d '{
  "prompt": "Your question here",
  "filters": "contains(path, `docx`)"
}'
Summarization
To summarize a list of texts:

bash
Copy code
curl -X POST 'http://localhost:8000/v1/pw_ai_summary' -H 'accept: */*' -H 'Content-Type: application/json' -d '{
  "text_list": [
    "Text 1 to summarize",
    "Text 2 to summarize"
  ]
}'
API Endpoints
/v1/pw_ai_answer: Question answering.
/v1/pw_list_documents: Lists all indexed documents (metadata).
/v1/pw_ai_summary: Text summarization.
Customization Options
To modify the application:

Edit the app.py file for backend logic or to introduce new features.
Adjust the streamlit_app.py file to update the user interface or introduce new functionalities.
Tweak the config.yaml file to change data sources, model configurations, or other settings.
