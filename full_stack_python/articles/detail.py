import reflex as rx
from ..ui.base import base_page
from . import state

def article_detail_page() -> rx.Component:
    my_child = rx.cond(
        state.ArticlePublicState.post,
        rx.vstack(
            rx.hstack(
                rx.heading(state.ArticlePublicState.post.title, size="9"),
                align="end",
            ),
            rx.text("By: ", state.ArticlePublicState.post.userinfo.user.username),
            rx.text(state.ArticlePublicState.post.publish_date),
            rx.text(state.ArticlePublicState.post.content, white_space="pre-wrap"),
            spacing="5",
            align="center",
            min_height="85vh",
        ),
        rx.hstack(
            rx.heading("Blog Post Not Found"),
            spacing="5",
            align="center",
            justify="center",
            min_height="85vh",
        ),
    )
    return base_page(my_child)
