"""사용자 요청 접수 → main agent 호출."""
import uuid

from fastapi import APIRouter

from app.models.request import ChatRequest
from app.models.response import ChatResponse
from app.agents.main_agent import run as main_agent_run

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    reply = main_agent_run(req.message)
    conversation_id = req.conversation_id or str(uuid.uuid4())
    return ChatResponse(reply=reply, conversation_id=conversation_id)
