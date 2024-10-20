import reflex as rx
from CalHacks_CrisisMap.state.state import State

def location_input():
    return rx.vstack(
        rx.input(
            placeholder="Enter zip code...",
            on_change=State.set_zip_code,
            max_length=5,
            type_="tel",
        ),
        rx.button("Submit", on_click=State.convert_zip_to_coords),
        rx.text(State.error, color="red"),
        rx.text(rx.cond(
            State.lat != 37.7749,  # Only show if coordinates have been updated
            rx.vstack(
                rx.text(f"Latitude: {State.lat}"),
                rx.text(f"Longitude: {State.lon}"),
            ),
        )),
        width="100%",
        spacing="4",
    )