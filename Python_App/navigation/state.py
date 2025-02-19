import reflex as rx
from . import routes 

class NavState(rx.State):  # ✅ Correct
    def to_home(self):
        """
        on click event

        """
        return rx.redirect(routes.HOME_ROUTES)
    
    def to_about_as(self):
        """
        on click event
        
        """
        return rx.redirect(routes.ABOUT_AS_ROUTES)
    
    def to_chat_page(self):
        """
        on click event
        
        """
        return rx.redirect(routes.CHAT_PAGE_ROUTES)




