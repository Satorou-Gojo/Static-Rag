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

This application combines the power of Pathway's real-time document indexing and retrieval capabilities with a user-friendly Streamlit interface. It uses the Gemini API for natural language processing tasks such as question answering and text summarization, providing an always up-to-date knowledge base for your LLM without the need for separate ETL processes.

## Features

- Ask questions with or without RAG from static documents in the local directory (Retrieval-Augmented Generation)
- Search indexed documents with customizable filters
- List all indexed documents with metadata
- Summarize multiple texts

## How It Works

The pipeline leverages Pathway connectors to read data from various sources (local drive, Google Drive, SharePoint) with low-latency change detection. Binary objects are parsed using the [unstructured](https://unstructured.io/) library and split into chunks. The Gemini API is used to embed these chunks.

Embeddings are indexed using Pathway's machine learning library. Users can query the index through HTTP requests made to the provided endpoints.

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

