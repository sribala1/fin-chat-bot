# rag_pipeline.py

from llama_index.core import VectorStoreIndex, Document, Settings
from llama_index.llms.cohere import Cohere
from llama_index.embeddings.cohere import CohereEmbedding
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()
api_key = os.getenv("CO_API_KEY")

def load_excel_to_documents(filepath):
    df = pd.read_excel(filepath)
    documents = []
    for _, row in df.iterrows():
        text = (
            f"Company: {row['company']}, Year: {row['year']}\n"
            f"Revenue: {row['total_revenue']}, COGS: {row['cogs']}, "
            f"Operating Expenses: {row['operating_expenses']}, Net Income: {row['net_income']}\n"
            f"Cash from Ops: {row['cash_from_ops']}, "
            f"Investing: {row['cash_from_investing']}, Financing: {row['cash_from_financing']}"
        )
        documents.append(Document(text=text))
    return documents

def build_index_from_excel(filepath):
    if not api_key:
        raise ValueError("Missing CO_API_KEY. Check your .env file.")
    
    llm = Cohere(model="command-r", api_key=api_key)
    embed_model = CohereEmbedding(api_key=api_key)

    Settings.llm = llm
    Settings.embed_model = embed_model

    documents = load_excel_to_documents(filepath)
    return VectorStoreIndex.from_documents(documents)

def query_index(index, question):
    return index.as_query_engine().query(question)
