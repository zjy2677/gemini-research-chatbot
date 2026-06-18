from fastapi import FastAPI

from backend.agent.router import router as agent_router
from backend.auth.router import router as auth_router
from backend.database import create_tables


app = FastAPI(title="Gemini Research Chatbot API")


@app.on_event("startup")
def start_api():
    create_tables()


@app.get("/api/health")
def health_check():
    return {"status": "ok"}


app.include_router(auth_router)
app.include_router(agent_router)
