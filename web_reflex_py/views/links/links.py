import reflex as rx
from web_reflex_py.components.link_button import link_buttun

def links() -> rx.Component:
    return rx.vstack(
        link_buttun(
            'Click Me!', 
            'recargar pagina', 
            'http://localhost:3000/'
        ),
        link_buttun(
            'Twitch', 
            '¿Cuando toca Mouredev?', 
            'https://www.twitch.tv/super_yorch'
        ),
        link_buttun(
            'Linkedin', 
            'Para que pueda ojear mi perfil', 
            'https://www.linkedin.com/in/jorgeagullo/'
        ),
        link_buttun(
            'Youtube', 
            'Los vídos de mis apps',
            'https://www.youtube.com/channel/UCcox318Jjfm8H6Roesi3SZg'
        ),
        link_buttun(
            'Github', 
            'Con esto conocerás mi potencial', 
            'https://github.com/JorgeAgulloM'
        ),
        width="100%"
    )