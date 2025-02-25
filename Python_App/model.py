import reflex as rx
import sqlalchemy
from datetime import datetime, timezone
from sqlmodel import Field, Relationship
from typing import List, Optional

# Function to get the current UTC time
def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)

# Define the ChatSession model
class ChatSession(rx.Model, table=True):
    # Relationship to ChatSessionMessageModel
    messages: List["ChatSessionMessageModel"] = Relationship(back_populates="session")

    # Timestamp for when the chat session was created
    create_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now(),
        },
        nullable=False,
    )

    # Timestamp for when the chat session was last updated
    update_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "onupdate": sqlalchemy.func.now(),
            "server_default": sqlalchemy.func.now(),
        },
        nullable=False,
    )

# Define the ChatSessionMessageModel model
class ChatSessionMessageModel(rx.Model, table=True):
    # Foreign key to the ChatSession model
    session_id: int = Field(default=None, foreign_key="chatsession.id", nullable=False)  # Add nullable=False

    # Relationship to ChatSession
    session: "ChatSession" = Relationship(back_populates="messages")

    # Message content
    content: str = Field(nullable=False)  # Ensure the content is required

    # Role of the message sender (e.g., "user" or "bot")
    role: str = Field(nullable=False)  # Ensure the role is required

    # Timestamp for when the message was created
    create_at: datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "server_default": sqlalchemy.func.now(),
        },
        nullable=False,
    )