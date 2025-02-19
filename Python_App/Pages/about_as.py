

import reflex as rx
from  Python_App import ui
from rxconfig import config

def about_as_page() -> rx.Component:
    # Welcome Page (Index)
    return ui.base_layout(
        # rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading("Welcome to Aboutas Page!", size="9"),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


