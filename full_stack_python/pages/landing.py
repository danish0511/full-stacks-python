import reflex as rx
from ..articles.list import article_public_list_component
from .. import navigation

def landing_component() -> rx.Component:
    return rx.vstack(
        rx.heading("Welcome to BlogPost", size="9"),
        rx.link(
            rx.button("About Us"),
            href=navigation.routes.ABOUT_US_ROUTE,
        ),
        rx.divider(),
        rx.heading("Recent Articles", size="5"),
        article_public_list_component(columns=1, limit=3),
        spacing="5",
        justify="center",
        align="center",
        min_height="85vh",
        id="my-child",
    )