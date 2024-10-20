import reflex as rx

def location_input():
    return rx.vstack(
        rx.input(placeholder="Search here...", max_length=20)
    )