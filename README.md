# 💬 Fin Chat Bot

An interactive, AI-powered chatbot that allows users to ask financial questions using plain English and receive intelligent, real-time responses based on uploaded Excel documents.

Built as part of a simulation project at BCG’s GenAI consulting team, this chatbot extracts and interprets key insights from financial data (10-K and 10-Q) using Retrieval-Augmented Generation (RAG).

---

## 🚀 Demo Use Case

> 🧾 Upload an Excel file of financial data and ask:  
> _"What was Tesla’s net income in 2023?"_

The chatbot will analyze the file and return a plain English answer instantly.

---

## 🛠️ Tech Stack

- **🧠 LLM:** [Cohere](https://cohere.com) (via API)
- **📚 RAG:** [LlamaIndex](https://www.llamaindex.ai/)
- **📊 Frontend UI:** Streamlit
- **📂 Input Format:** Excel (.xlsx or .csv)

---

## ✨ Key Features

- 🔍 **Financial Insight Extraction** from 10-K and 10-Q reports  
- 🤖 **Cohere-Powered LLM Chatbot** with natural language understanding  
- 📈 **Upload & Query Excel Sheets** with financial data  
- 📬 **Instant Q&A Responses** from structured document context  
- 📦 **Streamlit Frontend** for clean user interaction

---
## 🧪 How to Run the Project Locally

> Make sure you have **Python 3.8+** and **pip** installed.

### 1. Clone the repository

```bash
git clone https://github.com/your-username/fin-chat-bot.git
cd fin-chat-bot
