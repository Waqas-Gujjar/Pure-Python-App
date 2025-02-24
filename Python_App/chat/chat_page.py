import reflex as rx
from Python_App import ui
from .forms import chat_form
from .state import ChatMessage, ChatState

# Define a consistent style for chat messages
message_style = dict(
    display="inline-block",
    padding="1.5em",  # Increased padding for better spacing
    border_radius="12px",  # Rounded corners for a modern look
    max_width=["30em", "30em", "50em", "50em", "50em", "50em"],
    box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",  # Subtle shadow
    font_size="1.1em",  # Slightly larger font size
    line_height="1.6",  # Improved readability
)

# Define a function to render individual chat messages
def message_box(chat_message: ChatMessage) -> rx.Component:
    return rx.box(
        rx.box(
            rx.markdown(
                chat_message.message,
                background_color=rx.cond(
                    chat_message.is_bot, 
                    rx.color("mauve", 4),  # Bot message color
                    rx.color("blue", 4)    # User message color
                ),
                color=rx.cond(
                    chat_message.is_bot, 
                    rx.color("mauve", 12),  # Bot text color
                    rx.color("blue", 12)     # User text color
                ),
                **message_style,
            ),
            text_align=rx.cond(chat_message.is_bot, "left", "right"),
            margin_top="1.5em",  # Increased margin for better spacing
        ),
        width="100%",
    )

# Define the chat page layout
def chat_pages():
    return ui.base_layout(
        rx.vstack(
            rx.heading(
                "Chat Here", 
                size="9", 
                color="blue.11",  # Heading color
                margin_bottom="1.5em",  # Spacing below the heading
            ),
            rx.box(
                rx.foreach(ChatState.messages, message_box),
                width="100%",
                padding="2em",  # Padding around the chat box
                background_color="gray.2",  # Light background for the chat area
                border_radius="12px",  # Rounded corners for the chat area
                box_shadow="0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)",  # Subtle shadow
            ),
            chat_form(),
            margin="3em auto",
            spacing="5",
            justify="center",
            min_height="85vh",
            width="90%",  # Limit the width for better readability
            max_width="1200px",  # Maximum width for large screens
        ),
    )