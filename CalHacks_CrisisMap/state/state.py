import reflex as rx
import requests

class State(rx.State):
    zip_code: str = ""
    lat: float = 37.7749  # Default to San Francisco
    lon: float = -122.4194
    error: str = ""

    def set_zip_code(self, zip_code: str):
        if len(zip_code) <= 5 and zip_code.isdigit():
            self.zip_code = zip_code
            self.error = ""
            print(zip_code)
        else:
            self.error = "Please enter a valid 5-digit zip code."

    def convert_zip_to_coords(self):
        if len(self.zip_code) != 5:
            self.error = "Please enter a valid 5-digit zip code."
            return
        
        api_key = "AIzaSyB00U7TY2GZJANOC34L6KXnWnlr3bax8rE"  # Replace with your actual API key
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={self.zip_code}&key={api_key}"
        
        response = requests.get(url)
        data = response.json()
        
        if data['status'] == 'OK':
            location = data['results'][0]['geometry']['location']
            self.lat = location['lat']
            self.lon = location['lng']
            self.error = ""
        else:
            self.error = "Unable to find coordinates for the given zip code."