import reflex as rx
from web_reflex_py.components.link_icon import link_icon
from web_reflex_py.components.info_text import info_text
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
        ),
        spacing=Size.DEFAULT.value
    ),
    rx.flex(
        info_text("+2", "años de experiencia"),
        rx.spacer(),
        info_text("Android", "Jetpack compose"),
        rx.spacer(),
        info_text("Python", "FastApi y Reflex"),
        width="100%"
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