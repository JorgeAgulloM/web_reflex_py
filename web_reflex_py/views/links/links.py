import reflex as rx
from web_reflex_py.components.link_button import link_buttun

def links() -> rx.Component:
    return rx.vstack(
        link_buttun('Click Me!', 'http://localhost:3000/'),
        link_buttun('Twitch', 'https://www.twitch.tv/super_yorch'),
        link_buttun('Linkedin', 'https://www.linkedin.com/in/jorgeagullo/'),
        link_buttun('Youtube', 'https://www.youtube.com/channel/UCcox318Jjfm8H6Roesi3SZg'),
        link_buttun('Github', 'https://github.com/JorgeAgulloM'),
    )