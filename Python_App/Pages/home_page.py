

import reflex as rx
from  Python_App import ui
from rxconfig import config

def home() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Reflex GPT", size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )



