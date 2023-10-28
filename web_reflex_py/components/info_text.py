import reflex as rx
import web_reflex_py.styles.styles as style
from web_reflex_py.styles.colors import Color, TextColor

def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title, 
            font_weight="bold", 
            color=Color.PRIMARY.value
        ),
        f" {body}",
        font_size=style.Size.MEDIUM.value,
        color=TextColor.BODY.value
    )