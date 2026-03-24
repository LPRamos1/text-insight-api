# 🔍 TextInsight API

A functional **FastAPI** application designed to practice text processing and API development. This project was built to demonstrate clean code structure, data validation with Pydantic, and basic containerization with Docker.

## 🚀 Key Features
- **Text Metrics**: Calculates word count, character count, and estimated reading time.
- **Keyword Extraction**: Identifies the top 5 most frequent words (filtering short words).
- **Interactive Docs**: Automatic Swagger UI for easy testing of endpoints.
- **Developer Ready**: Includes unit tests and Docker configuration.

## 🛠️ Tech Stack (Beginner Level)
- **Python 3.11**
- **FastAPI**: Used for routing and request handling.
- **Pydantic**: Ensuring data integrity via schemas.
- **Docker**: Simple containerization for local development.
- **Pytest**: Unit testing for the analysis logic.

## 📦 Installation & Setup

### Using Docker (Recommended)
1. Clone the repository:
   ```bash
   git clone [https://github.com/LPRamos1/text-insight-api.git](https://github.com/LPRamos1/text-insight-api.git)
   cd text-insight-api
    ```
2. Run with Docker Compose:
 ```bash
docker-compose up --build
```
3. Access the API documentation at: http://localhost:8080/docs

### Manual Setup (Local Venv)
1. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the server:
```bash
uvicorn app.main:app --reload
```

## 🧪 Running Tests
To run the automated test suite, use:
```bash
pytest tests/
```