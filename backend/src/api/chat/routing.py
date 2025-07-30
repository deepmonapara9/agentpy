from fastapi import APIRouter

router = APIRouter()

# /api/chat/
@router.get("/")
def chat_health():
   return {"status": "OK!"} 