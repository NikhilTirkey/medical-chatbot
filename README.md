# 🏥 AI Medical Chatbot

An AI-powered medical chatbot built using Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) to provide intelligent responses based on medical data.

---

## 🚀 Features

* 💬 Ask medical-related questions in natural language
* 🧠 Uses LLM for intelligent responses
* 📄 Retrieves relevant information from stored documents (RAG)
* ⚡ Fast and modular backend built with Python

---

## 🛠️ Tech Stack

* Python
* LLM (OpenAI / Groq / other free models)
* RAG (Document indexing & retrieval)
* Flask / FastAPI (if used)

---

## 📂 Project Structure

```
.
├── app.py
├── store_index.py
├── pdf_test.py
├── test_groq.py
├── templates/
├── data/
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/NikhilTirkey/medical-chatbot.git
cd medical-chatbot
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Add environment variables

Create a `.env` file and add:

```
OPENAI_API_KEY=your_api_key
```

### 4. Run the application

```
python app.py
```

---

## 📌 Use Case

This project demonstrates how AI can be used to assist users with medical-related queries by combining LLM reasoning with document retrieval.

---

## ⚠️ Disclaimer

This chatbot is for educational purposes only and should not be used as a substitute for professional medical advice.

---

## 👨‍💻 Author

Nikhil Tirkey
GitHub: https://github.com/NikhilTirkey
