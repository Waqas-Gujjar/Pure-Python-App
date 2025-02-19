import reflex as rx
# import asyncio
from typing import List

from . import ai


class ChatMessage(rx.Base):
    message : str
    is_bot = False



class ChatState(rx.State):
    did_submit : bool = False
    messages : List[ChatMessage] = []
    @rx.var
    def user_did_submit(self) -> bool:
        return self.did_submit
    
    def get_gpt_message(self):
        gpt_messages = [
            {
                'role' : "user",
                "content" :" your are expert in python "
             }
        ]

        for chat_message in self.messages:
            role = "user"
            if chat_message.is_bot:
                role = "system"
            gpt_messages.append({
                "role": role,
                "content": chat_message.message,
            })
            return gpt_messages
    
    def append_message(self, message,is_boot : bool=False) :
        self.messages.append (ChatMessage(
                message=message,
                is_bot=is_boot,  # assume bot messages are not from the user
            ))
    
    async def handler_submitted(self, form_data:dict):
        print(f"Form data: {form_data}")
        user_message = form_data.get('message')
        if user_message:
            self.did_submit = True
            self.append_message(user_message,is_boot=False)
            yield
            gpt_message = self.get_gpt_message()
            bot_response = ai.get_llm_response(gpt_message)
            # await asyncio.sleep(2)  # simulate network delay
            self.did_submit = False
            self.append_message(bot_response,is_boot=True)
            yield

        