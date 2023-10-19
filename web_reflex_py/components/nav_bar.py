import reflex as rx
from web_reflex_py.styles.styles import Size


def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.text(
            'SoftYorch'
        ),
        position='sticky',
        bg='lightgray',
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index='999',
        top="0"
    )
