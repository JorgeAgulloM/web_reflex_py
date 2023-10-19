import reflex as rx
import web_reflex_py.styles.styles as style 

def link_buttun(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward",
                    width=style.Size.DEFAULT.value,
                    height=style.Size.DEFAULT.value
                ),
                rx.vstack(
                    rx.text(title, style=style.button_title_style),
                    rx.text(body, style=style.button_body_style),
                    align_items="start"
                )
            ),
            padding=style.Size.DEFAULT.value,
            height='100px'
        ),
        href=url,
        is_external=True,
        width="100%",
    )
