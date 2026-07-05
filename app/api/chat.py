from fastapi import APIRouter
from pydantic import BaseModel

from app.sessions.session_manager import SessionManager

router = APIRouter()

session_manager = SessionManager()


class ChatRequest(BaseModel):
    session_id: str
    message: str


@router.post("/chat")
def chat(request: ChatRequest):

    engine = session_manager.get_engine(request.session_id)

    return {
        "response": engine.chat(request.message)
    }