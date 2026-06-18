from pydantic import BaseModel


class ChatRequest(BaseModel):
    message: str
    model: str


class ChatResponse(BaseModel):
    message: str
    model: str
