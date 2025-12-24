from pydantic import BaseModel
from typing import Optional, List, Literal

Role = Literal["system", "user", "assistant"]

class ChatMessage(BaseModel):
    role: Role
    content: str

class SendMessageRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class SendMessageResponse(BaseModel):
    session_id: str
    assistant_message: str
    model: str
