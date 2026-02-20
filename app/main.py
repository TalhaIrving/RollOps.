from fastapi import FastAPI
import uuid

app = FastAPI()

sessions = {}

@app.get("/health")
def health_check():
    return {"status": "ok"}

# create a session
@app.post("/sessions")
def create_session():
    session_id = str(uuid.uuid4())
    sessions[session_id] = {}
    return {"session_id": session_id}