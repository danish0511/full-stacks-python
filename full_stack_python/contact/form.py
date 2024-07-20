import reflex as rx
from .state import ContactState
from ..auth.state import SessionState

def contact_form() -> rx.Component:
    return rx.form(
            # rx.cond(
            #     SessionState.my_user_id,
            #     rx.box(
            #         rx.input(
            #             type='hidden',
            #             name="user_id",
            #             value=SessionState.my_user_id
            #         ),
            #         display='none'
            #     ),
                
            #     rx.fragment("")
            # ),
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
    