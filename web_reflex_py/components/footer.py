import reflex as rx
import datetime as dt


def footer() -> rx.Component:
    year = dt.date.today().year
    return rx.vstack(
        rx.image(src='favicon.ico'),
        rx.link(
            f'@2022-{year} SOFTYORCH By JORGE AGULLO V1.',
            href='https://github.com/JorgeAgulloM',
            is_external=True
        ),
        rx.text('BUILDING SOFTWARE WITH ♥. FROM ELCHE TO THE WORLD!')
    )