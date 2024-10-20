import reflex as rx

def get_html():
    with open("assets/map.html", "r") as file:
        return file.read()

def google_map():
    return rx.html(get_html())