"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx
from web_reflex_py.components.nav_bar import nav_bar
from web_reflex_py.views.header.header import header
from web_reflex_py.views.links.links import links
from web_reflex_py.views.sponsors.sponsors import sponsors
from web_reflex_py.components.footer import footer
import web_reflex_py.styles.styles as style
from web_reflex_py.styles.styles import Size

class State(rx.State):
    """The app state."""

    pass


def index() -> rx.Component:
    return rx.box(
        nav_bar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                sponsors(),
                max_width=style.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value  
            ),
        ),
        footer(),
    )

 
    


# Add state and page to the app.
app = rx.App(
    style=style.BASE_STYLES
)
app.add_page(
    index,
    title='SoftYorch | Aprendiendo desarrollo web con Python y Reflex',
    description='Hola, mi nombre es Jorge y soy Desarrollador de Aplicaciones Multiplataforma.',
    image="avatar.jpg"
)
app.compile()
