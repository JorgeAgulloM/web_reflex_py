import reflex as rx
from web_reflex_py.components.link_button import link_button
from web_reflex_py.components.title import title
from web_reflex_py.styles.styles import Size

def links() -> rx.Component:
    return rx.vstack(
        title("Personal"),
        link_button(
            'Github', 
            'Aquí conocerás mi potencial',
            'icons/github.svg', 
            'https://github.com/JorgeAgulloM'
        ),
        link_button(
            'Linkedin', 
            'Para que pueda ojear mi perfil', 
            'icons/linkedin.svg', 
            'https://www.linkedin.com/in/jorgeagullo/'
        ),
        
        title("Cosas varias"),
        link_button(
            'Twitch', 
            '¿Cuando toca Mouredev?', 
            'icons/twitch.svg', 
            'https://www.twitch.tv/super_yorch'
        ),
        link_button(
            'Youtube', 
            'Los vídos de mis apps',
            'icons/youtube.svg', 
            'https://www.youtube.com/channel/UCcox318Jjfm8H6Roesi3SZg'
        ),
        link_button(
            'Click Me!', 
            'recargar pagina', 
            'icons/hand-point-up-regular.svg', 
            'http://localhost:3000/'
        ),
        
        title("Contacto"),
        link_button(
            'Email', 
            'softyorch@gmail.com', 
            'icons/envelope-regular.svg', 
            'mailto:softyorch@gmail.com'
        ),
        
        width="100%",
        spacing=Size.MEDIUM.value
    )