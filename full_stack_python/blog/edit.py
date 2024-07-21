import reflex as rx
from ..ui.base import base_page
from . import forms
from .state import BlogEditFormState


def blog_post_edit_page() -> rx.Component:
    my_form = forms.blog_post_edit_form()
    post = BlogEditFormState.post

    my_child = rx.cond(
        post,
        rx.vstack(
            rx.heading("Editing ", post.title, size="9"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width="50vw",
                )
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width="95vw",
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width="75vw",
                )
            ),
            spacing="5",
            align="center",
            min_height="95vh",
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
