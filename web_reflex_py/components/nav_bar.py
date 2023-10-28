import reflex as rx
from web_reflex_py.styles.styles import navbar_title_style
from web_reflex_py.styles.styles import Size
from web_reflex_py.styles.colors import Color


def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.span("Soft", color=Color.PRIMARY.value),
            rx.span("Yorch", color=Color.SECONDARY.value),
            style=navbar_title_style
        ),
        position='sticky',
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index='999',
        top="0"
    )
