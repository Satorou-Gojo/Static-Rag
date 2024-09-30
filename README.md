# Pathway RAG Application with Streamlit UI

This project demonstrates how to create a Retrieval-Augmented Generation (RAG) application using [Pathway](https://github.com/pathwaycom/pathway) and [Streamlit](https://streamlit.io/), integrated with the Gemini API for natural language processing tasks.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Pathway Tooling](#pathway-tooling)
- [LLM Functionality](#llm-functionality)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
  - [LLM Model](#llm-model)
  - [API Key Configuration](#api-key-configuration)
- [How to Run](#how-to-run)
  - [Running Locally](#running-locally)
  - [Running with Docker](#running-with-docker)
- [Using the Application](#using-the-application)
  - [Adding your own data](#adding-your-own-data)
  - [Querying Documents](#querying-documents)
  - [Listing Inputs](#listing-inputs)
  - [Searching Documents](#searching-documents)
  - [Asking Questions (With and Without RAG)](#asking-questions-with-and-without-rag)
  - [Summarization](#summarization)
- [API Endpoints](#api-endpoints)
- [Customization](#customization)

## Overview

This app blends the real-time document indexing and retrieval strengths of Pathway with the simplicity of Streamlit's UI. By leveraging the Gemini API for NLP tasks such as question-answering and summarization, the application delivers an always-up-to-date knowledge base for your LLM without requiring separate ETL processes.

## Key Features

-Query static documents in a local directory using RAG or without it.
-Search through indexed documents with custom filters.
-Display a list of all indexed documents and related metadata.
-Summarize multiple text inputs simultaneously.

## WorkFlow

Pathway connectors capture data from your local folder(data). The unstructured library parses and divides binary objects into chunks, which are then embedded using the Gemini API.

The embeddings are indexed with Pathway's machine learning tools, allowing users to query the index through HTTP requests to specified endpoints.

## Pathway Tooling

- **Prompts and Helpers**: Pathway enables custom prompt definitions and user-defined functions (UDFs) with the `@pw.udf` decorator for streaming data operations.
- **RAG Components**: Pathway offers tools like a vector store and web server (via REST connector) to build a complete RAG solution.
- **Connectors**: A range of connectors are available for seamless integration of different data sources.

## LLM Functionality

The application uses the Gemini API to:
- Generate embeddings for document chunks
- Answer questions based on retrieved context
- Summarize text inputs

The LLM model can be configured within the Gemini API, providing flexibility between performance and cost.

## Prerequisites

```yaml
- Python 3.7+
- Pathway
- Streamlit
- Access to Gemini API
## Installation

1. Clone this repository:
   ```
   git clone https://github.com/nrk-necro/pathway-rag-streamlit.git
   cd pathway-rag-streamlit
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Configuration

### LLM Model

You can configure the Gemini model in the `config.yaml` file:

```yaml
llm_config:
  model: "gemini/gemini-pro"
```


### API Key Configuration

Store your Gemini API key in a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

## How to Run

### Running with Docker

1. Build the Docker image:
   ```
   docker build -t pathway-rag-streamlit .
   ```

2. Run the container:
   ```
   docker run -v $(pwd)/data:/app/data -p 8000:8000 -p 8501:8501 pathway-rag-streamlit
   ```


### Running Locally


1. In a separate terminal, run the Streamlit app:
   ```
   streamlit run streamlit_app.py
   ```

2. Open a web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).


## Using the Application

The Streamlit interface provides four main tabs:

1. **Ask Question**: Enter a question and optionally use RAG with filters.
2. **List Documents**: View all indexed documents and their metadata.
3. **Summarize Texts**: Input multiple texts and get a summary.

## Adding your own data
Currently, the RAG application uses the book 'Zombie Survival Guide - Complete Protection from the Living Dead.pdf'. Howeever, you can add your own data in the data folder.

## Querying Documents

### Listing Inputs

To get a list of available inputs and associated metadata:

```bash
curl -X 'POST' 'http://localhost:8000/v1/pw_list_documents' -H 'accept: */*' -H 'Content-Type: application/json'
```

### Searching Documents

To search within your documents:

```bash
curl -X 'POST' \
  'http://localhost:8000/v1/retrieve' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "Your search query here",
  "k": 5
}'
```

### Asking Questions (With and Without RAG)

To ask a question using RAG:

```bash
curl -X 'POST' \
  'http://localhost:8000/v1/pw_ai_answer' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "prompt": "Your question here",
  "filters": "contains(path, `docx`)"
}'
```

### Summarization

To summarize a list of texts:

```bash
curl -X 'POST' \
  'http://localhost:8000/v1/pw_ai_summary' \
  -H 'accept: */*' \
  -H 'Content-Type: application/json' \
  -d '{
  "text_list": [
    "Text 1 to summarize",
    "Text 2 to summarize"
  ]
}'
```

## API Endpoints

- `/v1/pw_ai_answer`: For question answering
- `/v1/pw_list_documents`: To list all indexed documents (not included in this project)
- `/v1/pw_ai_summary`: For text summarization

## Customization

To customize the application:

1. Modify the `app.py` file to change the backend logic or add new features.
2. Update the `streamlit_app.py` file to alter the user interface or add new functionalities.
3. Adjust the `config.yaml` file to change data sources, model configurations, or other settings.

