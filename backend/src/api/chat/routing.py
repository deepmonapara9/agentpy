from fastapi import APIRouter, Depends
from sqlmodel import Session, select
from .models import ChatMessagePayLoad, ChatMessage, ChatMessageListItem

from api.db import get_session
from api.ai.schemas import EmailMessageSchema
from api.ai.services import generate_email_message
from typing import List

router = APIRouter()

# /api/chat/
@router.get("/")
def chat_health():
    return {"status": "OK!"}

# /api/chats/recent/
# This will return the last 10 messages from the database and will be sorted by the id
# curl http://localhost:8000/api/chats/recent/  --> to check the recent messages from the database
@router.get("/recent", response_model=List[ChatMessageListItem])
def chat_recent_messages(session: Session = Depends(get_session)):
    query = select(ChatMessage).order_by(ChatMessage.id.desc())  # sql -> query
    results = session.exec(query).fetchall()[:10]
    return results

# HTTP POST -> payload = {"message": "hello world!"}
# curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello again"}' http://localhost:8000/api/chats/
# curl -X POST -H "Content-Type: application/json" -d '{"message": "Hello again"}' https://agentpy-production.up.railway.app/api/chats/

# To check the model
# curl -X POST -d '{"message": "Give me a summary of why it is good to go outside"}' -H "Content-Type: application/json" http://localhost:8000/api/chats/
@router.post("/", response_model=EmailMessageSchema)
def chat_create_message(
    payload: ChatMessagePayLoad,
    session: Session = Depends(get_session)
):
    data = payload.model_dump()  # pydantic -> dict
    print(data)
    obj = ChatMessage.model_validate(data)  # sqlmodel -> object
    session.add(obj)
    session.commit()
    #  session.refresh(obj) # ensure id/primary key added to the obj instance
    response = generate_email_message(payload.message)
    return response
