# 🔍 TextInsight API

A simple FastAPI project built to practice backend development and text processing fundamentals using Python.

---

## 🚀 Features

- Word and character count
- Estimated reading time calculation
- Top keyword extraction (frequency-based)
- REST API with FastAPI
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

The API receives a text input, processes it using basic NLP techniques, and returns simple metrics such as word count and keyword frequency.

Input → Text processing → JSON response

---

## 📦 Setup

### Docker

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
🎯 Purpose

This project was built as part of my learning process in backend development using FastAPI, focusing on API design, data validation, and simple text processing.


