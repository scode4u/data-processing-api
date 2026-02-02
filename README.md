Data Processing API
Overview

Data Processing API is a backend service built with FastAPI that ingests raw CSV files, cleans and processes the data, and exposes analytical insights through REST APIs. A lightweight Streamlit UI is included as a client to demonstrate API usage.

This project focuses on backend engineering, API design, data handling, validation, error handling, and automated testing.

Features: 

CSV file upload and validation
Data cleaning (duplicate removal, missing value handling, type normalization)
In-memory data storage (Phase 1)

Analytical APIs:

Summary statistics
Aggregations (sum, avg, min, max, count)
Filtering
Top N records

Centralized error handling with consistent error responses
Automated API tests using pytest
Streamlit UI as an API consumer (demo client)

Tech Stack : 

Python 3.11
FastAPI
Pandas
Pydantic
Pytest
Streamlit
HTTPX / Requests

Project Structure : 

data-processing-api/
│
├── app/
│   ├── main.py
│   ├── routes/
│   │   ├── upload.py
│   │   └── analytics.py
│   ├── services/
│   │   ├── cleaner.py
│   │   └── utils.py
│   ├── schemas/
│   │   └── responses.py
│
├── streamlit_app/
│   └── app.py
│
├── tests/
│   ├── conftest.py
│   ├── test_upload.py
│   └── test_analytics.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── requirements.txt
├── README.md
└── .gitignore

Setup Instructions
1. Clone the Repository
git clone https://github.com/<scode4u>/data-processing-api.git
cd data-processing-api

2. Create and Activate Virtual Environment
python -m venv venv


Windows:

venv\Scripts\activate


Mac/Linux:

source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

Running the Backend (FastAPI)
uvicorn app.main:app --reload


Backend will be available at:

API: http://localhost:8000
Swagger Docs: http://localhost:8000/docs

Running the Streamlit UI

Open a new terminal (keep FastAPI running):

streamlit run streamlit_app/app.py


Streamlit will run in the browser and interact with the FastAPI backend via HTTP.

API Endpoints
Upload CSV
POST /upload/


Response:

{
  "status": "success",
  "rows": 244,
  "columns": ["col1", "col2", "col3"]
}

Summary
GET /analytics/summary


Returns row count, column count, and numeric summary statistics.

Aggregate
GET /analytics/aggregate?column=<column>&operation=<sum|avg|min|max|count>

Filter
GET /analytics/filter?column=<column>&value=<value>

Top N Records
GET /analytics/top?column=<column>&n=<number>

Error Handling

All errors follow a consistent response format:

{
  "error": "HTTPException",
  "message": "Description of the error",
  "status_code": 400
}

Running Tests
pytest -v


Tests validate:

CSV upload
Analytics aggregation
API response correctness

Design Notes

Streamlit is a client, not part of the backend logic.
Backend logic is fully decoupled from the UI.
Data persistence is intentionally minimal in Phase 1.
Project is structured to scale to database storage and deployment in later phases.

Future Enhancements

Dockerization
Database integration (PostgreSQL)
Background processing
Authentication
CI/CD with GitHub Actions
Deployment (Render, Railway, or AWS)

Author

Surya
Master's in Computer Application (Data Science)
Backend / Data Engineering focused project

License
MIT License