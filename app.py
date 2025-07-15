# app.py

import streamlit as st
from rag_pipeline import build_index_from_excel, query_index
import os

st.set_page_config(page_title="💰 Financial Chatbot", layout="centered")
st.title("💬 AI-Powered Financial Chatbot")
st.markdown("Upload your Excel file and ask questions!")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
index = None

if uploaded_file:
    with open("data/temp_uploaded.xlsx", "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🔄 Building the index..."):
        index = build_index_from_excel("data/temp_uploaded.xlsx")
        st.success("✅ Index built!")

if index:
    query = st.text_input("Ask a question:")
    if query:
        with st.spinner("Thinking..."):
            answer = query_index(index, query)
            st.markdown(f"**Answer:** {answer}")
