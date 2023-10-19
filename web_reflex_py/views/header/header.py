import reflex as rx
from web_reflex_py.components.link_icon import link_icon
from web_reflex_py.styles.styles import Size

def header() -> rx.Component:
 return rx.vstack(
    rx.hstack(
        rx.avatar(name='Jorge Agulló', size='xl'),
        rx.vstack(
            rx.heading(
                'Jorge Agulló', 
                size="lg"
            ),
            rx.text(
                '@Yorchdevelop',
                margin_top="0px !important"
            ),
            rx.hstack(
                link_icon("https://github.com/JorgeAgulloM"),
                link_icon("https://github.com/JorgeAgulloM"),
                link_icon("https://github.com/JorgeAgulloM")
            ),
            align_items="start"
        )
    ),
    rx.text(
        """Indagando en la creación de sitios web usando 
        Python y Reflex. Emocionado por explorar un nueva 
        tecnología para crear webs y construir experiencias 
        digitales atractivas."""
    ),
    spacing=Size.BIG.value,
    align_items="start" 
)