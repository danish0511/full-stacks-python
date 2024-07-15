import reflex as rx
from ..ui.base import base_page

class ContactState(rx.State):
    form_data: dict = {}
    
    def handle_submit(self, form_data: dict):
        """Handle the form submit."""
        print(form_data)
        self.form_data = form_data
    

def contact_page() -> rx.Component:
    my_form = rx.form(
            rx.vstack(
                rx.hstack(
                    rx.input(
                        name="first_name",
                        placeholder="First Name",
                        type='text',
                        required=True,
                        width='100%',
                    ),
                    rx.input(
                        name="last_name",
                        placeholder="Last Name",
                        type='text',
                        width='100%',
                    ),
                    width='100%'
                ),
                rx.input(
                    name='email',
                    type='email',
                    placeholder='Your Email',
                    width='100%',
                ),
                rx.text_area(
                    name="message",
                    placeholder='Your message',
                    required=True,
                    width='100%',
                ),
                rx.button("Submit", type="submit"),
            ),
            on_submit=ContactState.handle_submit,
            reset_on_submit=True,
        ),
    
    my_child=rx.vstack(
            rx.heading("Contact Us", size="9"),
            rx.desktop_only(
                rx.box(
                    my_form,
                    width='50vw',
                )
            ),
            rx.mobile_only(
                rx.box(
                    my_form,
                    width='95vw',
                )
            ),
            rx.tablet_only(
                rx.box(
                    my_form,
                    width='75vw',
                )
            ),
            spacing="5",
            justify="center",
            align="center",
            min_height="85vh",
            id="my-child"
        )
    return base_page(my_child)