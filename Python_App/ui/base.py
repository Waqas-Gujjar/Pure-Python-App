from .navbar import navbar_page
import reflex as rx
def base_layout(*args, **kwargs) -> rx.Component:
    return rx.container(
        navbar_page("navbar"),
        *args, **kwargs

    )