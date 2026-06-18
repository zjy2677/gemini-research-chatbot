from fastapi import APIRouter, HTTPException, status

from backend.agent.gemini_client import generate_chat_response
from backend.agent.schemas import ChatRequest, ChatResponse


router = APIRouter(prefix="/api/agent", tags=["agent"])


@router.post("/chat", response_model=ChatResponse)
def chat(payload: ChatRequest):
    try:
        answer = generate_chat_response(
            message=payload.message,
            model=payload.model,
        )
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error),
        ) from error
    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=f"Gemini request failed: {error}",
        ) from error

    return ChatResponse(message=answer, model=payload.model)
