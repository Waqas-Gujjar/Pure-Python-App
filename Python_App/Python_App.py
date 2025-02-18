"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from  . import ui,Pages
from rxconfig import config





app = rx.App()
app.add_page(Pages.home_page,route="/")
app.add_page(Pages.about_as,route='/about')
