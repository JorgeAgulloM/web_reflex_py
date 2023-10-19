import reflex as rx
from web_reflex_py.styles.styles import title_style

def title(text: str) ->rx.Component:
    return rx.heading(
        text,
        size="lg",
        style=title_style
    )