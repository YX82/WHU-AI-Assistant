# 🎓 WHU-AI-Assistant  
An Intelligent Campus Q&A System for Wuhan University

This project was developed for the **Wuhan University "Volcano Cup" AI Agent Innovation Competition**.  
It provides an AI-powered question answering system based on official university website data.

---

## 🚀 Project Overview

WHU-AI-Assistant is an intelligent campus information assistant that can answer questions about:

- University introduction and history  
- Academic affairs and departments  
- Library services  
- Student affairs and campus services  
- Admissions and employment information  

Unlike traditional chatbots, this system does **not rely on fixed Q&A pairs**.  
Instead, it retrieves relevant content from a **real knowledge base built from official WHU websites**.

---

## 🧠 System Architecture

The system follows a lightweight **Retrieval-Based QA pipeline**:

User Question  
→ Text Vectorization (TF-IDF)  
→ Similarity Matching  
→ Retrieve Most Relevant Document  
→ Return Answer  

---

## 📚 Knowledge Base Construction

To ensure authoritative and up-to-date information, the knowledge base is built from **official Wuhan University websites** using automated web crawling.

### 🔍 Data Sources

The system collects data from multiple university portals, including:

- Wuhan University official website  
- Undergraduate Affairs Office  
- Graduate School  
- Library  
- Student Affairs Office  
- Career Services  
- Admissions websites  
- Administrative departments

### 🤖 Web Crawling Method

A browser automation crawler based on **Selenium** is used to:

1. Load dynamic web pages rendered by JavaScript  
2. Extract visible textual content  
3. Clean and store structured knowledge entries  

This avoids common issues where traditional crawlers fail to retrieve content from modern university portals.

Run the crawler with:

```bash
python build_knowledge.py
