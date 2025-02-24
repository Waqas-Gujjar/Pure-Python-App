import reflex as rx
import sqlalchemy
from datetime import datetime ,timezone
from sqlmodel import Field ,Relationship 
from typing import List

def get_utc_now() -> datetime:
    return datetime.now(timezone.utc)



class ChatSession(rx.Model,table=True):
    # tittle : str
    message: List ['ChatSessionMessageModel'] = Relationship(back_populates="chatsession")
    create_at : datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default':sqlalchemy.func.now()
        },
       nullable=False
    )

    update_at : datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            "onupdate":sqlalchemy.func.now(),
            'server_default':sqlalchemy.func.now()
        },
       nullable=False,
    )


class ChatSessionMessageModel(rx.Model,table=True):
    session: int = Field(default=None,foreign_key='chatsession.id')
    content : str
    role:str
    create_at : datetime = Field(
        default_factory=get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={
            'server_default':sqlalchemy.func.now()
        },
       nullable=False
    )

  