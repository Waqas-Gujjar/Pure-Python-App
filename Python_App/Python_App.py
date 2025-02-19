"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from  . import Pages,navigation,chat






app = rx.App()
app.add_page(Pages.home,route=navigation.routes.HOME_ROUTES)
app.add_page(Pages.about_as_page,route=navigation.routes.ABOUT_AS_ROUTES)
app.add_page(chat.chat_pages,route=navigation.routes.CHAT_PAGE_ROUTES)
