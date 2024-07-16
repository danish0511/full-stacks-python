"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

from .ui.base import base_page
from . import pages, navigation, contact

class State(rx.State):
    """The app state."""
    label = "Welome to Reflex!"
    
    def handle_title_input_change(self, val):
        self.label=val
        
    def did_change(self):
        print("Hello World!")
    
def index() -> rx.Component:
    # Welcome Page (Index)
    my_child=rx.vstack(
            rx.heading(State.label, size="9"),
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)


app = rx.App()
app.add_page(index)
app.add_page(pages.about_page, route=navigation.routes.ABOUT_US_ROUTE)
app.add_page(pages.pricing_page, route=navigation.routes.PRICING_ROUTE)
app.add_page(contact.contact_page, route=navigation.routes.CONTACT_US_ROUTE)
