import reflex as rx
from CalHacks_CrisisMap.components.google_map import google_map
from CalHacks_CrisisMap.state.weather_state import weather_state

def index():
    return rx.center(
        rx.box(
            google_map(),
            width="80%",
            max_width="800px",
            height="400px",
            bg="white",
            border_radius="md",
            box_shadow="lg",
        ),
        width="100%",
        height="100vh",
    )