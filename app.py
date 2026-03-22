import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Load API key
api_key = os.getenv("GROQ_API_KEY")

# Load LLM
llm = ChatGroq(
    groq_api_key=api_key,
    model_name="llama-3.3-70b-versatile"
)

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS index
db = FAISS.load_local(
    "faiss_index",
    embeddings,
    allow_dangerous_deserialization=True
)

# Simple memory
chat_history = []
display_history = []

# Home route
@app.route("/")
def home():
    return render_template("index.html", chat_history=display_history)

# Ask route
@app.route("/ask", methods=["POST"])
def ask():
    user_message = request.form["message"]

    # Retrieve similar docs
    docs = db.similarity_search(user_message, k=3)
    context = " ".join([doc.page_content for doc in docs])

    # Previous memory
    history = " ".join(chat_history)

    # Prompt
    prompt = f"""
    You are a professional medical assistant.

    Rules:
    - Answer only from provided context
    - Be medically clear
    - Keep answer concise
    - Advise doctor consultation if serious symptoms exist

    Previous conversation:
    {history}

    Medical context:
    {context}

    Question:
    {user_message}
    """

    # LLM response
    response = llm.invoke(prompt)

    # Save internal memory
    chat_history.append(f"User: {user_message}")
    chat_history.append(f"Bot: {response.content}")

    # Save display history
    display_history.append(("You", user_message))
    display_history.append(("Bot", response.content))

    return render_template("index.html", chat_history=display_history)

if __name__ == "__main__":
    app.run(debug=True)