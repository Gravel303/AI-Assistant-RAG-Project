# 📚 AI Study Assistant

An AI-powered study assistant built with Streamlit, Gemini, FAISS, and Retrieval-Augmented Generation (RAG).

Upload a PDF document and interact with it using AI-powered chat, summaries, quizzes, and flashcards.

---

## 🚀 Features

### 💬 Chat with Documents

- Ask questions about uploaded PDFs
- Conversational memory for follow-up questions
- Query rewriting for better retrieval
- Context-aware responses using RAG

### 📄 Document Summaries

- Generate concise study summaries
- Extract key concepts and topics
- Create revision-friendly notes

### 📝 Quiz Generator

- Generate multiple-choice quizzes from uploaded documents
- Useful for self-assessment and exam preparation

### 🃏 Flashcard Generator

- Automatically create study flashcards
- Question-and-answer format
- Focused on important concepts

### 📚 Source Attribution

- Displays the source pages used to generate answers
- Improves transparency and trust

### ⚡ Efficient Retrieval

- Text chunking with overlap
- Gemini embeddings
- FAISS vector search
- Persistent local storage

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Google Gemini API
- FAISS
- PyPDF
- NumPy
- Pickle

---

## 🏗️ System Architecture

PDF Upload

↓

Text Extraction

↓

Chunking

↓

Embeddings

↓

FAISS Vector Index

↓

Retrieval

↓

Gemini Response Generation

↓

Answer + Sources

---

## 📦 Installation

Clone the repository:

```bash
git clone <repository-url>
cd <repository-name>
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

---

## 📖 Usage

1. Upload a PDF document.
2. Wait for processing and indexing.
3. Ask questions about the document.
4. Generate summaries, quizzes, or flashcards.
5. Review source pages used for answers.

---

## 🔮 Future Improvements

- Multi-document support
- ChromaDB integration
- Better source citations
- Export summaries and flashcards
- User accounts and saved study sessions
- Local embedding models

---

## 🎯 Project Goals

This project was built to learn and demonstrate:

- Retrieval-Augmented Generation (RAG)
- Vector embeddings
- Semantic search
- Prompt engineering
- AI application development
- Streamlit deployment

---

## 📄 License

This project is intended for educational and learning purposes.

## Live Demo

https://ai-assistant-rag-project-mbqtsgfvg9ab623mbyk9er.streamlit.app/
