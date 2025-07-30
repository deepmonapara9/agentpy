from fastapi import FastAPI
from api.db import init_db
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

@app.get("/")
def read_index():
    return {"Hello": "World again"}