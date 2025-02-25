from typing import List
import reflex as rx
from . import ai
from Python_App.model import ChatSession, ChatSessionMessageModel


class ChatMessage(rx.Base):
    """Represents a single chat message in the conversation."""
    message: str  # The content of the message
    is_bot: bool = False  # Whether the message is from the bot


class ChatState(rx.State):
    """Manages the chat state, including user and bot messages."""
    chat_session_id: int = None  # Store only the ID
    did_submit: bool = False  # Whether the user has submitted a message
    messages: List[ChatMessage] = []  # List of chat messages

    @rx.var
    def user_did_submit(self) -> bool:
        """Check if the user has submitted a message."""
        return self.did_submit
    def create_new_chat_session(self):
        with rx.session() as db_session:
            obj = ChatSession()
            db_session.add(obj)
            db_session.commit()
            self.chat_session_id = obj.id  # Store only the ID
 
    def clear_and_start_new_chat(self):
        """Clear the chat state and start a new chat."""
        self.chat_session_id = None
        self.create_new_chat_session()
        self.messages = []
        yield

        


    def on_load(self):
        """Initialize a new chat session when the page loads."""
        self.create_new_chat_session()
        

    def insert_message_into_db(self, content, role="unknown"):
        """Insert a new message into the database."""
        if not hasattr(self, 'chat_session_id') or self.chat_session_id is None:
            return

        with rx.session() as db_session:
            chat_session = db_session.query(ChatSession).get(self.chat_session_id)
            if chat_session is None:
                return

            data = {
                "session_id": chat_session.id,
                "content": content,
                "role": role
            }
            obj = ChatSessionMessageModel(**data)
            db_session.add(obj)
            db_session.commit()

    def get_gpt_message(self):
        """Prepare chat history in a format suitable for the Groq API."""
        gpt_messages = [
            {
                "role": "system",
                "content": "You are an expert at creating recipes like an elite chef. Respond in markdown"
            }
        ]

        for chat_message in self.messages:
            role = "user"
            if chat_message.is_bot:
                role = "system"
            gpt_messages.append({
                "role": role,
                "content": chat_message.message
            })

        return gpt_messages

    def append_message_to_ui(self, message: str, is_bot: bool = False) -> None:
        """Add a new message to the chat history."""
        self.messages.append(ChatMessage(message=message, is_bot=is_bot))

    async def handler_submitted(self, form_data: dict):
        """Handle form submission and generate AI response."""
        user_message = form_data.get("message")
        if user_message:
            self.did_submit = True
            self.append_message_to_ui(user_message, is_bot=False)  # Add to UI
            self.insert_message_into_db(user_message, role="user")  # Insert into DB
            yield  # Yield to update the UI

            # Get AI response
            gpt_message = self.get_gpt_message()
            bot_response = ai.get_llm_response(gpt_message)
            print("Bot response:", bot_response)

            self.did_submit = False
            self.append_message_to_ui(bot_response, is_bot=True)  # Add to UI
            self.insert_message_into_db(bot_response, role="system")  # Insert into DB
            yield  # Yield to update the UI