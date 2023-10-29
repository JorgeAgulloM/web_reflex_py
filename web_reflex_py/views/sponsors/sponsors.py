### Sponsors ###

import reflex as rx
from web_reflex_py.components.title import title
from web_reflex_py.components.link_sponsor import link_sponsor
from web_reflex_py.styles.styles import Size

def sponsors() -> rx.Component:
    return rx.vstack(
        title('Colaboran'),
        rx.hstack(
            link_sponsor(
                "reflex_white.svg",
                "https://reflex.dev/"
            ),
            link_sponsor(
                "logo_python_es.png",
                "https://es.python.org/"
            ),
            spacing=Size.DEFAULT.value,
            width="100%",
            align_items="start"
        )
    )
    