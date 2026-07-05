from fastapi import APIRouter
from pydantic import BaseModel

from app.services.conversation import ConversationEngine

router = APIRouter()

engine = ConversationEngine()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
def chat(request: ChatRequest):
    return {
        "response": engine.chat(request.message)
    }