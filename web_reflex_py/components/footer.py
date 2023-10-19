import reflex as rx
import datetime as dt
from web_reflex_py.styles.styles import Size

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
            margin_top="0px !important"
        ),
        margin_bottom=Size.BIG.value
    )