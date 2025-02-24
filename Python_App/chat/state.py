from typing import List
import reflex as rx
from . import ai
from Python_App.model import ChatSession as ChatModel

class ChatMessage(rx.Base):
    """Represents a single chat message in the conversation."""

    message: str  # The content of the message
    is_bot: bool = False  # Whether the message is from the bot


class ChatState(rx.State):
    """Manages the chat state, including user and bot messages."""

    did_submit: bool = False  # Whether the user has submitted a message
    messages: List[ChatMessage] = []  # List of chat messages


    

    @rx.var
    def user_did_submit(self) -> bool:
        """Check if the user has submitted a message."""
        return self.did_submit
    
    def on_load(self):
        with rx.session() as session:
            result = session.exec(
                ChatModel.select()
            ).all
            print(result)

    def get_gpt_message(self):
        """
        Prepare chat history in a format suitable for the Groq API.

        Returns:
            List of messages formatted for the Groq API.
        """
        # System message to set the bot's behavior
        gpt_messages = [
            {
                "role": "system",
                "content": "You are an expert at creating recipes like an elite chef. Respond in markdown"
            }
        ]

        # Append user and bot messages to the list
        for chat_message in self.messages:
            role = "assistant" if chat_message.is_bot else "user"
            gpt_messages.append({
                "role": role,
                "content": chat_message.message,
            })

        return gpt_messages

    def append_message(self, message: str, is_bot: bool = False) -> None:
    #   if not is_bot:
    #         with rx.session() as session:
    #             obj = ChatModel(
    #                     tittle = message,
    #         )
    #             session.add(obj)
    #             session.commit()

      """
        Add a new message to the chat history.
        Args:
            message: The text content of the message.
            is_bot: True if the message is from the bot, False if from the user.
        """
      self.messages.append(ChatMessage(message=message, is_bot=is_bot))

    async def handler_submitted(self, form_data: dict):
        """
        Handle the form submission, process the user message, and generate a response from the AI.

        Args:
            form_data: Dictionary containing the user's input message.
        """
        print(f"Form data received: {form_data}")  # Debugging: Log the form data

        # Extract the user's message from the form data
        user_message = form_data.get("message")
        if user_message:
            self.did_submit = True
            self.append_message(user_message, is_bot=False)  # Add the user's message to the chat history
            yield  # Yield to update the UI

            # Get AI response
            gpt_message = self.get_gpt_message()  # Prepare the message for the Groq API
            bot_response = ai.get_llm_response(gpt_message)  # Get the bot's response
            print("Bot response:", bot_response)  # Debugging: Log the bot's response

            self.did_submit = False
            self.append_message(bot_response, is_bot=True)  # Add the bot's response to the chat history
            yield  # Yield to update the UI