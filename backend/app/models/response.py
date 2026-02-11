"""응답 스키마."""
from pydantic import BaseModel


class ChatResponse(BaseModel):
    reply: str
    conversation_id: str
