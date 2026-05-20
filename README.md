# Agentic Text-to-SQL System

This repository contains the completed tasks for the Week 3 assignments of the Fuse Fellowship. The objective of this project is to build an AI-powered agentic system that understands natural language questions, breaks them down into structured components, converts them into SQL queries, executes those queries on a PostgreSQL database, handles errors with automated retries, and returns meaningful answers.

## Project Structure

The assignment is divided into four interconnected tasks:

1. **Task 1: SQL Benchmark Dataset & Evaluation Design**
   - Prepared a benchmark dataset of 50 natural language questions.
   - Wrote ground-truth SQL queries for each question (see `task1_ground_truth.md`).
   - Drafted a robust evaluation strategy detailing how to grade Text-to-SQL systems (`task1_evaluation_strategy.md`).

2. **Task 2: Query Understanding (Decomposition)**
   - Decomposed the natural language questions into structural components: Intent, Tables, Columns, Filters, and Joins.
   - Outputs are stored in `task2_decomposition.json`.

3. **Task 3: Text-to-SQL Pipeline and Query Execution System**
   - Built a Python-based execution pipeline (`project/executor.py`) that implements generation, validation, and database execution logic.
   - Includes a robust validator (`project/validator.py`) to prevent destructive queries (blocking INSERT, DELETE, UPDATE, DROP, etc.).
   - Contains an evaluation script (`project/evaluate.py`) that successfully tests the pipeline against the benchmark dataset, ensuring execution capabilities and reporting the success rate.

4. **Task 4: Mini SQL Agent API**
   - Encapsulates the entire pipeline inside a FastAPI web application (`project/main.py`).
   - Exposes a `POST /agent/sql` endpoint that processes incoming questions, executes self-correcting SQL logic with up to 3 retries on failure, and returns the query result alongside a natural language summary.

## Prerequisites

- **Docker & Docker Compose**: Used to run the isolated PostgreSQL database.
- **Python 3.10+**: Used for the Text-to-SQL pipeline and FastAPI.

## Setup Instructions

### 1. Database Initialization

Start the PostgreSQL database. The provided `docker-compose.yml` mounts a `seed.sql` file which automatically initializes the schema and populates the tables on first run.

```bash
docker-compose up -d
```

*(Note: The database is exposed on host port `5433` mapping to container port `5432` to avoid conflicts with existing local PostgreSQL instances).*

### 2. Python Environment Setup

Navigate to the `project/` directory, set up a virtual environment, and install the required dependencies.

```bash
cd project
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Running the Benchmark Evaluation (Task 3)

To test the entire pipeline against the 50 benchmark queries and view the self-correction logic and success rates:

```bash
cd project
source venv/bin/activate
python evaluate.py
```

### 4. Running the Mini SQL Agent API (Task 4)

Start the FastAPI server:

```bash
cd project
source venv/bin/activate
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

You can then test the agent API using `curl` or tools like Postman/Insomnia:

```bash
curl -X POST "http://localhost:8000/agent/sql" \
     -H "Content-Type: application/json" \
     -d '{"question": "How many shipped orders are from usa customers?"}'
```

**Expected JSON Response:**
```json
{
  "sql": "SELECT COUNT(*) FROM orders o JOIN customers c ON o.\"customerNumber\" = c.\"customerNumber\" WHERE o.status = 'Shipped' AND c.country = 'USA';",
  "result": 105,
  "summary": "There are 105 items matching your request.",
  "status": "success"
}
```

## Report Generation

A script named `create_pdf.py` is included to generate a PDF report (`week3_findings_report.pdf`) summarizing the execution of the assignments.

```bash
source project/venv/bin/activate
pip install fpdf2
python create_pdf.py
```
