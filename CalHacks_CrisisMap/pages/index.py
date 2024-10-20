import reflex as rx
from CalHacks_CrisisMap.components.google_map import google_map
from CalHacks_CrisisMap.components.user_input import location_input

def index():
    return rx.center(
        rx.flex(
            rx.box(
                location_input(),
                width="20%",
                max_width="20%",
                bg="white",
                border_radius="md",
                box_shadow="lg",
                padding="4",
            ),
            rx.box(
                google_map(),
                width="80%",
                max_width="80%",
                height="95%",   
                bg="white",
                border_radius="md",
                box_shadow="lg",
            ),
            width="100%",
            max_width="80%",
            height="95%",
            spacing="4",
            align="center",
            justify="center",
        ),
        width="100%",
        height="100vh",
    )