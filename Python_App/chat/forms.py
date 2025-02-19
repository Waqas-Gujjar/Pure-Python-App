import reflex as rx
from .state import ChatState


def chat_form () -> rx.Component:
    return rx.form(
        rx.vstack(
            rx.text_area(
                name="message",
                placeholder="Type your message here",
                required=True,
                width="100%",
            ),
            rx.hstack(
               rx.button('Submit',type="submit"),
               rx.cond(
                   ChatState.user_did_submit,
                   rx.text("Submitted"),
                   rx.fragment(),  
               ),   
            ),
        ),
        on_submit=ChatState.handler_submitted,
        reset_on_submit=True
    )