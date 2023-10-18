import reflex as rx

from web_reflex_py import style
from web_reflex_py.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right", color="black"), 
            style=style.question_style
        ),
        rx.box(
            rx.text(answer, text_align="left", color="black"), 
            style=style.answer_style
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.input(
            value=State.question,
            placeholder="Ask a question",
            on_change=State.set_question, 
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer, 
            style=style.button_style,
            color="black",
        ),
    )


def index() -> rx.Component:
    return rx.container(
            chat(),
            action_bar()
        )

# Add state and page to the app.
app = rx.App()
app.add_page(index)
app.compile()