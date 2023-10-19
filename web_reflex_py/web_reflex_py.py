"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from web_reflex_py.components.nav_bar import nav_bar

class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.vstack(
        nav_bar() 
    )  
    


# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()
