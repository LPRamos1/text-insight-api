# 🔍 TextInsight API

A FastAPI project built to practice backend development, API design, and text processing using Python.

---

## 🚀 Features

- Word and character count
- Estimated reading time calculation
- Top keyword extraction (frequency-based)
- REST API built with FastAPI
- Automatic API documentation (Swagger UI)

---


## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- Pydantic
- Pytest
- Docker (basic usage)

---

## ⚙️ How it works

The API receives a text input, validates it using Pydantic, processes it with basic NLP techniques, and returns structured metrics.

Input → Validation → Processing → JSON Response

---

## 📦 Setup

### Local

```bash
git clone https://github.com/LPRamos1/text-insight-api.git
cd text-insight-api
docker-compose up --build
```
Local
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
🧪 Tests
```bash
pytest tests/
```

## 🎯 Purpose

This project was built as part of my learning process in backend development using FastAPI, focusing on API design, data validation (Pydantic), and modular Python architecture.

It demonstrates how to structure a simple but clean REST API with separation between API layer and business logic.

## 📚 What I learned

- How to build a REST API using FastAPI
- Basic API structure and request validation with Pydantic
- Separation between business logic and API layer
- Basic text processing techniques in Python
- Containerization basics using Docker


