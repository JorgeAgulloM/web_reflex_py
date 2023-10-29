### Sponsors Link ###
import reflex as rx
from web_reflex_py.styles.styles import Size

def link_sponsor(img: str, url: str) -> rx.Component:
    return rx.link(
        rx.image(
            height=Size.VERY_BIG.value,
            src=img
        ),
        href=url,
        is_external=True
    )

