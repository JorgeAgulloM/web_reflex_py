import reflex as rx
from web_reflex_py.styles.styles import Size


def link_icon(img: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=img,
            width=Size.DEFAULT.value
        ),
        href=url,
        is_external=True
    )