"""대화 목록/조회 (사이드바용). 최소 구동: 빈 목록 반환."""
from fastapi import APIRouter

router = APIRouter()


@router.get("/conversations")
def list_conversations():
    return {"conversations": []}


@router.get("/conversations/{conversation_id}")
def get_conversation(conversation_id: str):
    return {"conversation_id": conversation_id, "messages": []}
