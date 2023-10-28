import reflex as rx
import web_reflex_py.styles.styles as style 

def link_button(title: str, body: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag="arrow_forward",
                    width=style.Size.BIG.value,
                    height=style.Size.BIG.value,
                    margin=style.Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=style.button_title_style),
                    rx.text(body, style=style.button_body_style),
                    spacing=style.Size.SMALL.value,
                    align_items="start",
                    margin=style.Size.ZERO.value
                )
            ),
            vertical_align="center",
            height="100%"
        ),
        href=url,
        is_external=True,
        width="100%",
    )
