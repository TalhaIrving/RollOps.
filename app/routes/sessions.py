"""
This module contains the API endpoints for the sessions resource.
"""






# Import the necessary modules
from fastapi import APIRouter
import uuid


# Define the router
router = APIRouter()

# Define the sessions dictionary
sessions = {}
 
 # Create a new session
@router.post("/sessions")
def create_session():
    # Generate a new session ID
    session_id = str(uuid.uuid4())
    # Add the session to the dictionary
    sessions[session_id] = {}
    # Return the session ID
    return {"session_id": session_id}

# Get a session by ID
@router.get("/sessions/{session_id}")
def get_session(session_id: str):
    # Return the session or an error if not found
    return sessions.get(session_id, {"error": "not found"})