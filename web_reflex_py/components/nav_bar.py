import reflex as rx

def nav_bar() -> rx.Component:
    return rx.hstack(
        rx.text(
            'SoftYorch',
            heigth='40px',
            color='white',
        ),
        position='sticky',
        bg='blue',
        padding_x='8px',
        padding_y='16px',
        z_index='999',
    )