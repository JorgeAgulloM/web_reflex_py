import reflex as rx
import datetime as dt
from web_reflex_py.styles.styles import Size
from web_reflex_py.styles.colors import Color, TextColor

def footer() -> rx.Component:
    year = dt.date.today().year
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.link(
            f'@2022-{year} SOFTYORCH By JORGE AGULLO V1.',
            href='https://github.com/JorgeAgulloM',
            is_external=True,
            font_size=Size.SMALL.value
        ),
        rx.text(
            'BUILDING SOFTWARE WITH ♥. FROM ELCHE TO THE WORLD!',
            font_size=Size.SMALL.value,
            margin_top=Size.ZERO.value
        ),
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.BIG.value,
        color=TextColor.FOOTER.value
    )