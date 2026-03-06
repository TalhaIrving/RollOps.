"""
This module contains the main application and its configuration.
"""

# Import the necessary modules
from fastapi import FastAPI
from app.routes.sessions import router as sessions_router

# Define the FastAPI app
app = FastAPI()

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}

# Include the sessions router
app.include_router(sessions_router)