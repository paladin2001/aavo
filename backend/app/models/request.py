"""요청 스키마."""
from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    conversation_id: str | None = None
