import streamlit as st
import requests

# Set the base URL for your Pathway RAG API
BASE_URL = "http://localhost:8080"

st.title("Pathway RAG Application with Gemini")

# Sidebar for configuration
st.sidebar.header("Configuration")
api_key = st.sidebar.text_input("Gemini API Key", type="password")

# Main content area
tab1, tab2 = st.tabs(["Ask Question", "List Documents"])

with tab1:
    st.header("Ask a Question")
    question = st.text_input("Enter your question and press Enter:")

    if question:  # This will trigger when Enter is pressed
        payload = {
            "prompt": question,
        }
        if api_key:
            payload["gemini_api_key"] = api_key
        
        response = requests.post(f"{BASE_URL}/v1/pw_ai_answer", json=payload)
        if response.status_code == 200:
            st.subheader("Answer:")
            st.write(response.text)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

with tab2:
    st.header("List Documents")
    if st.button("Fetch Documents"):
        response = requests.post(f"{BASE_URL}/v1/pw_list_documents")
        if response.status_code == 200:
            try:
                documents = response.json()
                for doc in documents:
                    st.subheader(doc.get("path", "Unnamed Document"))
                    for key, value in doc.items():
                        if key != "path":
                            st.write(f"{key.capitalize()}: {value}")
                    st.write("---")
            except requests.exceptions.JSONDecodeError:
                st.warning("Response is not in JSON format. Raw response:")
                st.text(response.text)
        else:
            st.error(f"Error: {response.status_code} - {response.text}")

# Display statistics
st.sidebar.header("Statistics")
if st.sidebar.button("Fetch Statistics"):
    response = requests.post(f"{BASE_URL}/v1/statistics")
    if response.status_code == 200:
        try:
            stats = response.json()
            st.sidebar.subheader("System Statistics")
            if stats:
                for key, value in stats.items():
                    st.sidebar.write(f"{key.replace('_', ' ').capitalize()}: {value}")
            else:
                st.sidebar.write("No statistics available.")
        except requests.exceptions.JSONDecodeError:
            st.sidebar.warning("Response is not in JSON format. Raw response:")
            st.sidebar.text(response.text)
    else:
        st.sidebar.error(f"Error fetching statistics: {response.status_code} - {response.text}")
