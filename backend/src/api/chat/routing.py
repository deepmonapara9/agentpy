from fastapi import APIRouter, Depends
from sqlmodel import Session
from .models import ChatMessagePayLoad, ChatMessage
from api.db import get_session

router = APIRouter()

# /api/chat/
@router.get("/")
def chat_health():
    return {"status": "OK!"}

# HTTP POST -> payload = {"message": "hello world!"}
@router.post("/", response_model=ChatMessage)
def chat_create_message(
    payload: ChatMessagePayLoad,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()  # pydantic -> dict
    print(data)
    obj = ChatMessage.model_validate(data)  # sqlmodel -> object
    session.add(obj)
    session.commit()
    session.refresh(obj)
    return obj
