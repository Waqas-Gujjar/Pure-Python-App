from .navbar import base_navbar
from .footer import base_footer
import reflex as rx
def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        base_navbar(),
        rx.fragment(*args, 
                    **kwargs
        ),
        base_footer(), 

    )