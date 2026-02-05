# WHU-AI-Assistant
An AI campus assistant for Wuhan University providing intelligent information retrieval and Q&amp;A services

This project was built for the **Wuhan University "Volcano Cup" AI Agent Innovation Competition**.

---

## 🚀 Project Overview

This system provides intelligent Q&A services for campus-related information, including:

- Academic affairs guidance
- Campus life services
- University news and announcements
- Freshman onboarding support

It is based on a **Retrieval-Augmented Generation (RAG)** workflow:

User Question → Knowledge Base Retrieval → LLM Generation → Answer Output

---

## 🧠 System Architecture

1. User inputs a campus-related question  
2. The system searches a structured knowledge base  
3. Relevant information is injected into a prompt  
4. Large Language Model generates a natural language answer  

---

## 📂 Project Structure

WHU-AI-Assistant
│── app.py # Main application (Gradio + LLM interaction)
│── knowledge.json # Structured campus knowledge base
│── data_processor.py # Data cleaning and structured extraction module
│── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## 🛠 Installation & Usage

### 1️⃣ Clone the repository

```bash
git clone https://github.com/YX82/WHU-AI-Assistant.git
cd WHU-AI-Assistant
```

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Add your API Key

client = OpenAI(api_key="YOUR_API_KEY")

### 4️⃣ Run the application'

python app.py


