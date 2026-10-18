# Learn AI in 40 Days

This repository contains a 40-day Python and Git training journey.  
It includes fundamentals, algorithms, OOP, data structures, SQL, REST APIs, testing, and Git practice.

**Public learning repository:** never commit real credentials or private data.
The API requires privately configured environment variables; no working login
defaults are published. Read [the security and publishing guide](SECURITY.md)
and [the Day 7 setup instructions](day07/README.md) before running the API.

## What is inside

- Day 1: Git basics
- Day 2: Python fundamentals
- Day 3: OOP library system
- Day 4: Stack and queue
- Day 5: Sorting, searching, recursion, and benchmarking
- Day 6: SQL queries and sample database
- Day 7: FastAPI REST API for books
- Day 8: Git branching, merge conflicts, and rebase
- Day 9: API testing with pytest and FastAPI TestClient
- Day 10: Checkpoint and README cleanup
- Day 11: Repository and factory refactor
- Day 12: Clean code and SOLID notes
- Day 13: Static frontend book catalog
- Day 14: React frontend for books
- Day 15: Layered backend architecture and dependency injection
- Day 16: JWT auth basics
- Day 17: Cloud deployment fundamentals
- Day 18: CI/CD basics with GitLab pipeline
- Day 19: Debugging and structured logging
- Day 20: Phase 2 full-stack checkpoint
- Day 21: AI/ML landscape notes
- Day 22: How LLMs work at a high level
- Day 23: Prompt engineering basics

## Day 7 API

The Day 7 app is a simple REST API for books with these endpoints:

- `GET /books`
- `GET /books/{id}`
- `POST /books`
- `PUT /books/{id}`
- `DELETE /books/{id}`

## How to run the API

From your repository root, go to the Day 7 folder:

```powershell
cd day07
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

First configure `SECRET_KEY`, `DEMO_USERNAME`, and `DEMO_PASSWORD` as described
in [Day 7 authentication setup](day07/README.md#authentication). There are no
fallback credentials. Then, from the Day 7 folder, run the API:

```powershell
uvicorn app:app --reload
```

Open the API docs in your browser:

```text
http://127.0.0.1:8000/docs
```

## How to run the tests

Tests create random test-only credentials; you do not need to configure real
secrets. From the Day 7 folder:

```powershell
pytest
```

Optional: install `pytest-cov` in your local environment before running coverage.
To run coverage:

```powershell
pytest --cov=app --cov-report=term-missing
```

To generate the HTML coverage report:

```powershell
pytest --cov=app --cov-report=html
```

## Project structure

```text
training-journal/
	day01-notes.md
	day02/
	day03/
	day04/
	day05/
	day06/
	day07/
		app.py
		requirements.txt
		tests/
	day08/
```

## Notes

- Day 7 uses FastAPI with in-memory book data.
- Day 9 uses pytest and TestClient for API testing.
- Generated files like `.coverage`, `htmlcov/`, and `__pycache__/` are ignored.
- Generated databases, agent runtime memory, logs, local backups, and real environment files are ignored too.
- The Day 26 agent uses its built-in default preferences when no local memory file exists.
- Days 11, 15, 16, 19, and 20 all build on the Day 7 API.
- Days 17 and 20 use deployment targets outside the repository, so their folders contain summary notes rather than infrastructure files.

## Recreate the Day 6 sample database

The repository includes SQL schema, seed data, queries, and example output rather
than a generated database. From the repository root, this command creates or
**resets** the local sample database (do not run it against valuable data):

```powershell
python -c "import sqlite3; from pathlib import Path; db = sqlite3.connect('day06/store.db'); db.executescript(Path('day06/schema.sql').read_text()); db.close()"
```

The generated database stays on your machine and is ignored by Git.

## Progress folders

- Existing implementation folders: `day01` to `day14`
- Added summary folders for the later work: `day09`, `day10`, `day11`, `day15`, `day16`, `day17`, `day18`, `day19`, `day20`, `day21`, `day22`, `day23`
- Each new folder contains a short summary of what was completed or learned for that day.
