from fastapi import FastAPI
from app.api import items
from app.db import Base, engine
from app import models

# Create DB tables on startup (demo style)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI Backend Template",
    description="Minimal example of a FastAPI backend with CRUD endpoints.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}


app.include_router(items.router, prefix="/items", tags=["items"])

