from sqlmodel import SQLModel, Field

class ChatMessagePayLoad(SQLModel):
   # Pydantic model 
   # It is for validation
   message: str

# This is a SQLModel class that represents a chat message in the database
class ChatMessage(SQLModel, table=True):
   # Database table
   # It is for saving, updating, and deleting or getting the chat messages
   id: int | None = Field(default=None, primary_key=True)
   message: str