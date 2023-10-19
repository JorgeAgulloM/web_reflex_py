import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name='Jorge Agulló', size='xl'),
        rx.text('@Yorchdev'),
        rx.text('Hola, mi nombre es Jorge Agulló'),
        rx.text("""Indagando en la creación de sitios web usando 
                Python y Reflex. Emocionado por explorar un nueva 
                tecnología para crear webs y construir experiencias 
                digitales atractivas."""),
    )