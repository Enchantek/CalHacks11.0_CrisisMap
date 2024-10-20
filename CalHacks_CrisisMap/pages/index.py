import reflex as rx
from CalHacks_CrisisMap.components.google_map import google_map
#from CalHacks_CrisisMap.state.weather_state import weather_state
from CalHacks_CrisisMap.components.open_weather import get_weather_data
from CalHacks_CrisisMap.components.user_input import location_input
from reflex import Component
import requests
# State to store and manage the lat/lon and map data
class MapState(rx.State):
    lat: float = 37.7749
    lon: float = -122.4194
    population_data: list = []

    def set_coordinates(self, lat, lon):
        """Set the latitude and longitude."""
        self.lat = lat
        self.lon = lon
        self.population_data = get_population_heatmap_data(lat, lon)

    def update_map(self):
        """Update the map with current coordinates and population data."""
        print(f"Updating map with Lat: {self.lat}, Lon: {self.lon}")
        return google_map(self.lat, self.lon, self.population_data)

# Function to get mock population data (replace with real data)
def get_population_heatmap_data(lat, lon):
    return [
        (lat, lon),
        (lat + 0.01, lon + 0.01),
        (lat + 0.02, lon - 0.01),
        (lat - 0.01, lon + 0.02),
        (lat - 0.02, lon - 0.02)
    ]

def create_logo_section():
    """Create the logo section with CrisisMap icon and text."""
    return rx.flex(
        rx.icon(
            alt="CrisisMap Logo",
            tag="map",
            height="2rem",
            margin_right="0.5rem",
            color="#EF4444",
            width="2rem",
        ),
        rx.text.span(
            "CrisisMap",
            font_weight="700",
            color="#ffffff",
            font_size="1.25rem",
            line_height="1.75rem",
        ),
        display="flex",
        align_items="center",
    )

def create_nav_link(link_text):
    """Create a navigation link with hover effect and white text color."""
    return rx.el.a(
        link_text,
        href="#",
        _hover={"color": "#D1D5DB"},
        color="#ffffff",
    )

def create_header():
    """Create the complete header with logo, navigation links, and responsive menu button."""
    return rx.center(
        rx.flex(
            create_logo_section(),
            rx.box(
                create_nav_link(link_text="Home"),
                create_nav_link(link_text="Map"),
                create_nav_link(link_text="Alerts"),
                create_nav_link(link_text="Resources"),
                create_nav_link(link_text="Contact"),
                display=rx.breakpoints(
                    {"0px": "none", "768px": "flex"}
                ),
                column_gap="1rem",
            ),
            rx.box(
                rx.el.button(
                    rx.icon(
                        alt="Menu",
                        tag="menu",
                        height="1.5rem",
                        width="1.5rem",
                    ),
                    _focus={"outline-style": "none"},
                    color="#ffffff",
                ),
                display=rx.breakpoints({"768px": "none"}),
            ),
            width="100%",
            style=rx.breakpoints(
                {
                    "640px": {"max-width": "640px"},
                    "768px": {"max-width": "768px"},
                    "1024px": {"max-width": "1024px"},
                    "1280px": {"max-width": "1280px"},
                    "1536px": {"max-width": "1536px"},
                }
            ),
            display="flex",
            align_items="center",
            justify_content="space-between",
            margin_left="auto",
            margin_right="auto",
        )
    )

# Main layout with static map based on lat/lon
def index():
    # Default lat/lon for map (can adjust these)
    lat, lon = 37.7749, -122.4194
    # Populate population heatmap data for these coordinates
    population_data = get_population_heatmap_data(lat, lon)
    
    return rx.vstack(
        rx.box(
            create_header(),
            width="100%",
        ),
        rx.center(
            rx.flex(
                rx.box(
                    location_input(),
                    id="zip_code_input",
                    width="20%",
                    height="95%",   
                    border_radius="md",
                    box_shadow="lg",
                ),
                rx.box(
                    google_map(lat, lon, population_data),  # Pass lat/lon and population heatmap data
                    id="google_map_container",  # Unique ID for dynamic updates
                    width="80%",
                    height="95%",   
                    bg="white",
                    border_radius="md",
                    box_shadow="lg",
                ),
                width="90%",
                height="calc(100vh - 60px)",  # Adjust this value based on your header height
                align="center",
                justify="center",
            ),
            width="100%",
            height="calc(100vh - 60px)",  # Adjust this value based on your header height
        ),
        width="100%",
        height="100vh",
        spacing="0",
    )