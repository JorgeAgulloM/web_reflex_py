import reflex as rx

def header() -> rx.Component:
 return rx.vstack(
    rx.hstack(
        rx.avatar(name='Jorge Agulló', size='xl'),
        rx.vstack(
            rx.heading(
                'Jorge Agulló', 
                size="lg"
            ),
            rx.text(
                '@Yorchdevelop',
                margin_top="0px !important"
            ),
            align_items="start"
        )
    ),
    rx.text(
        """Indagando en la creación de sitios web usando 
        Python y Reflex. Emocionado por explorar un nueva 
        tecnología para crear webs y construir experiencias 
        digitales atractivas."""
    ),
    align_items="start" 
)