import reflex as rx
import requests

def google_map():
    return rx.html("""
        <div id="map" style="height: 400px; width: 100%;"></div>
        <script>
            function initMap() {
                var map = new google.maps.Map(document.getElementById('map'), {
                    center: {lat: 37.78476, 122.40252},
                    zoom: 8
                });
            }
        </script>
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAhDbwUcLTef3gG7ORV6TK5gtIkIpkEsxE&callback=initMap"
        async defer></script>
    """)

# Function to get lat/lon from Google Geocoding API using ZIP code
def get_lat_lon_from_zip(zip_code):
    google_api_key = "AIzaSyAhDbwUcLTef3gG7ORV6TK5gtIkIpkEsxE"  # Replace with your actual Google API key
    geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={zip_code}&key={google_api_key}"
    
    response = requests.get(geocode_url)
    data = response.json()
    
    if data['status'] == 'OK':
        location = data['results'][0]['geometry']['location']
        return location['lat'], location['lng']
    else:
        return None, None