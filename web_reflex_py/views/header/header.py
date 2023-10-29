import reflex as rx
from web_reflex_py.components.link_icon import link_icon
from web_reflex_py.components.info_text import info_text
from web_reflex_py.styles.styles import Size
from web_reflex_py.styles.colors import TextColor
from web_reflex_py.styles.colors import Color, TextColor

def header() -> rx.Component:
 return rx.vstack(
    rx.hstack(
        rx.avatar(
            name='Jorge Agulló', 
            size='xl',
            src='avatar.jpg',
            color=TextColor.BODY.value,
            bg=Color.CONTENT.value,
            padding="2px",
            border='4px',
            border_color=Color.PRIMARY.value
        ),
        rx.vstack(
            rx.heading(
                'Jorge Agulló',
                size='lg'
            ),
            rx.text(
                '@Yorchdevelop',
                margin_top=Size.ZERO.value,
                color=TextColor.HEADER.value
            ),
            rx.hstack(
                link_icon(
                    'icons/github.svg',
                    'https://github.com/JorgeAgulloM'
                ),
                link_icon(
                    'icons/linkedin.svg',
                    'https://www.linkedin.com/in/jorgeagullo/'
                ),
                link_icon(
                    'icons/envelope-regular.svg',
                    'mailto:softyorch@gmail.com'
                ),
                spacing=Size.DEFAULT.value
            ),
            align_items="start"
        ),
        spacing=Size.DEFAULT.value
    ),
    rx.flex(
        info_text("+1", "año de experiencia"),
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
        digitales atractivas.""",
        font_size=Size.DEFAULT.value,
        color=TextColor.BODY.value
    ),
    spacing=Size.BIG.value,
    align_items="start" 
)