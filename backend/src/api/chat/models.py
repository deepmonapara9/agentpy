from datetime import datetime, timezone
from email import message
from email.policy import default
from sqlmodel import SQLModel, Field, DateTime

# This function will return the current UTC time
def get_utc_now():
   return datetime.now().replace(tzinfo=timezone.utc)

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
   created_at: datetime = Field(
      default_factory = get_utc_now,
      sa_type = DateTime(timezone=True),
      primary_key=False,
      nullable=False,
   )

class ChatMessageListItem(SQLModel):
   id: int | None = Field(default=None)
   message: str
   created_at: datetime = Field(
      default=None,
   )