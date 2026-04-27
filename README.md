## 🔍 TextInsight API

A RESTful API built with FastAPI for analyzing text data and extracting linguistic insights.
This project focuses on backend engineering best practices, including clean architecture, validation, and database integration.

## 📌 Project Status

This project is under active development and has been recently refactored to improve architecture and scalability.

## 🚀 Features

- Text analysis (word count, character count, reading time)
- Keyword extraction using frequency-based approach
- Full CRUD operations with PostgreSQL
- Input validation with Pydantic
- Service layer for business logic isolation
- Automated tests with Pytest
- Containerized environment using Docker

## 🛠️ Tech Stack

- Python 3.11
- FastAPI
- SQLAlchemy
- PostgreSQL
- Pydantic
- Pytest
- Docker

## ⚙️ Architecture

Client Request  
→ FastAPI Routes  
→ Pydantic Schemas (validation)
→ Service Layer  
→ Analyzer Module
→ Database (PostgreSQL)
→ Response

## 📦 Project Structure

app/
├── api/
│ ├── deps.py
│ └── routes/
│ └── analysis.py
├── db/
│ ├── base.py
│ └── session.py
├── models/
│ └── analysis.py
├── schemas/
│ └── analysis.py
├── services/
│ └── analysis_service.py
├── analyzer.py
└── main.py

tests/

## ▶️ Running the Project

### With Docker

```bash
docker-compose up --build
```

## Locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 🔌 API Endpoints

Method Endpoint Description
POST /analysis/ Create analysis
GET /analysis/ List all analyses
GET /analysis/{id} Get analysis by ID
PUT /analysis/{id} Update analysis
DELETE /analysis/{id} Delete analysis

## 📥 Example Request

{ "title": "Sample Text", "content": "This is a simple example text for analysis." }

## 📤 Example Response

{ "id": 1, "title": "Sample Text", "content": "This is a simple example text for analysis.", "word_count": 9, "char_count": 49, "reading_time_minutes": 0.01 }

## 🧪 Tests

```bash
pytest tests/
```

## 🎯 Purpose

This project was built to practice backend development with FastAPI, focusing on:

- Backend architecture
- REST API design
- Database integration
- Clean code and separation of concerns
- Testing

## 📚 Key Learnings

- Structuring scalable FastAPI applications
- Using SQLAlchemy ORM with PostgreSQL
- Separating concerns (routes, services, models)
- Data validation with Pydantic
- Error handling and transactions
- Containerization basics using Docker

## 🚧 Limitations

- Keyword extraction is frequency-based
- No authentication
- No pagination (yet)
- No database migrations (Alembic not implemented)

## 🔮 Future Improvements

- Add pagination and filtering
- Implement JWT authentication
- Introduce Alembic for migrations
- Improve NLP processing (TF-IDF / embeddings)
- Add logging and monitoring
