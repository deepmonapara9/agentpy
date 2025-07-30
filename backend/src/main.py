from fastapi import FastAPI
from api.db import init_db
from api.chat.routing import router as chat_router
from contextlib import asynccontextmanager

# This is the asynchronous context manager that will be used to create the database tables
# It will be called before the app starts and after the app stops before the FastAPI starts 
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Before app startup
    init_db()
    yield
    # After app startup

app = FastAPI(lifespan=lifespan)
app.include_router(chat_router, prefix="/api/chats")

@app.get("/")
def read_index():
    return {"Hello": "World again"}