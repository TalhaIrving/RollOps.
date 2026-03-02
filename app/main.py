"""
This module contains the main application and its configuration.
"""

# Import the necessary modules
from fastapi import FastAPI
from app.routes.sessions import router as sessions_router

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

app.include_router(sessions_router)