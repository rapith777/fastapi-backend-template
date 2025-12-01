```python
from fastapi import FastAPI
from app.api import items

app = FastAPI(
    title="FastAPI Backend Template",
    description="Minimal example of a FastAPI backend with CRUD endpoints.",
    version="0.1.0",
)


@app.get("/health", tags=["system"])
def health():
    return {"status": "ok"}


# Include routers
app.include_router(items.router, prefix="/items", tags=["items"])
