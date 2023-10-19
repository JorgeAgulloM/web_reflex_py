import reflex as rx
from web_reflex_py.components.link_button import link_button
from web_reflex_py.components.title import title
from web_reflex_py.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
        title("Personal"),
        link_button(
            'Github', 
            'Con esto conocerás mi potencial', 
            'https://github.com/JorgeAgulloM'
        ),
        link_button(
            'Linkedin', 
            'Para que pueda ojear mi perfil', 
            'https://www.linkedin.com/in/jorgeagullo/'
        ),
        title("Cosas varias"),
        link_button(
            'Twitch', 
            '¿Cuando toca Mouredev?', 
            'https://www.twitch.tv/super_yorch'
        ),
        link_button(
            'Youtube', 
            'Los vídos de mis apps',
            'https://www.youtube.com/channel/UCcox318Jjfm8H6Roesi3SZg'
        ),
        link_button(
            'Click Me!', 
            'recargar pagina', 
            'http://localhost:3000/'
        ),
        width="100%",
        spacing=Size.MEDIUM.value
    )