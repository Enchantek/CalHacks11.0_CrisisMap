import reflex as rx
from CalHacks_CrisisMap.components.google_map import google_map
#from CalHacks_CrisisMap.state.weather_state import weather_state
from CalHacks_CrisisMap.components.open_weather import get_weather_data
#from CalHacks_CrisisMap.components.user_input import location_input
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

# Main layout with static map based on lat/lon
def index():
    # Default lat/lon for map (can adjust these)
    lat, lon = 37.7749, -122.4194
    # Populate population heatmap data for these coordinates
    population_data = get_population_heatmap_data(lat, lon)
    
    return rx.center(
        rx.flex(
            rx.box(
                google_map(lat, lon, population_data),  # Pass lat/lon and population heatmap data
                id="google_map_container",  # Unique ID for dynamic updates
                width="100%",
                height="100vh",   
                bg="white",
                border_radius="md",
                box_shadow="lg",
            ),
            width="100%",
            height="100vh",
            align="center",
            justify="center",
        ),
        width="100%",
        height="100vh",
    )