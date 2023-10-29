import reflex as rx
import web_reflex_py.styles.styles as style 

def link_button(title: str, body: str, img: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=img,
                    width=style.Size.LARGE.value,
                    height=style.Size.LARGE.value,
                    margin=style.Size.MEDIUM.value
                ),
                rx.vstack(
                    rx.text(title, style=style.button_title_style),
                    rx.text(body, style=style.button_body_style),
                    align_items="start",
                    spacing=style.Size.ZERO.value,
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
