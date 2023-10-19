import reflex as rx
import web_reflex_py.styles.styles as style


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(title, font_weight="bold", color="blue"),
        f" {body}",
        font_size=style.Size.MEDIUM.value
    )