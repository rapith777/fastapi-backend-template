# FastAPI Backend Template

A small, minimal backend built with **FastAPI**, **Pydantic** and
**SQLAlchemy**, showing how I structure a simple CRUD API.

## Features

- FastAPI app with a clean structure
- SQLAlchemy models and database session helper
- Pydantic schemas for request/response validation
- CRUD endpoints for a simple `Item` resource

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload

