import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name='Jorge Agulló', size='xl'),
        rx.text('@Yorchdev'),
        rx.text('Hola, mi nombre es Jorge Agulló'),
        rx.text("""¡Hola a todos! Estoy emocionado de compartir 
                que estoy inmerso en el fascinante mundo de la 
                creación de sitios web con Python y Reflex. 
                A través de mi viaje de aprendizaje, he estado 
                explorando las maravillas de la programación web 
                y las posibilidades infinitas que ofrece este campo.
                 Con la ayuda de las robustas capacidades de Python 
                y las funcionalidades dinámicas de Reflex, estoy 
                descubriendo cómo construir sitios web interactivos 
                y atractivos. Cada paso que doy me acerca un poco 
                más a convertir mis ideas en experiencias digitales 
                sólidas y envolventes. ¡Sigan atentos para más 
                actualizaciones sobre mi emocionante viaje de 
                desarrollo web!""")
    )