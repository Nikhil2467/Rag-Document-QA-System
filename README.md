# 📄 RAG-Based Document Question Answering System

## 🔍 Overview
This project is a full-stack NLP application that enables users to upload PDF documents and ask questions based on their content. The system uses a Retrieval-Augmented Generation (RAG) approach to extract relevant information and generate accurate answers.

It is designed to work efficiently even in low-resource environments by using lightweight models such as TinyLLaMA.

---

## 🎯 Objective
To build an intelligent system that allows users to quickly extract meaningful insights from large documents without manually searching through them.

---

## 🚀 Features
- User Authentication (Register, Login, Logout)
- Upload and process PDF documents
- Text extraction and preprocessing
- Intelligent text chunking
- Embedding-based similarity search
- Question answering using RAG pipeline
- Optimized for low RAM systems

---

## 🛠️ Tech Stack
- Python
- Flask (Web Framework)
- NLP Techniques (Text Processing, Tokenization)
- Embeddings & Similarity Search
- TinyLLaMA (Lightweight LLM)
- SQLite (Database for authentication)

---

## ⚙️ System Workflow
1. User registers and logs into the system  
2. Uploads a PDF document  
3. Text is extracted from the document  
4. Text is split into smaller chunks  
5. Each chunk is converted into embeddings  
6. User submits a query  
7. System retrieves the most relevant chunks  
8. Response is generated using RAG approach  

---

## 🧠 RAG Architecture
- **Retriever:** Finds relevant document chunks using embeddings  
- **Generator:** Uses a language model to generate answers  
- Combines retrieval + generation for accurate results  

---

## ⚡ Challenges Faced
- Handling large documents efficiently  
- Working under low system memory constraints  
- Optimizing model performance  
- Ensuring accurate retrieval of relevant content  

---

## 📈 Future Improvements
- Integration with advanced LLMs (GPT, LLaMA variants)  
- Use of vector databases like FAISS  
- Support for multiple document formats (DOCX, TXT)  
- Improved UI/UX design  
- Deployment on cloud platforms  

---

## ▶️ Run the Project
```bash
pip install -r requirements.txt
python app.py
```

## 👨‍💻 Author
Nikhil
