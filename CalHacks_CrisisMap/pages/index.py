import reflex as rx
from CalHacks_CrisisMap.components.google_map import google_map
from CalHacks_CrisisMap.state.weather_state import weather_state
from CalHacks_CrisisMap.components.open_weather import get_weather_data
from reflex import Component

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

# Fetch weather data
lat, lon = 37.7749, -122.4194
weather_info = get_weather_data(lat, lon)

if 'error' not in weather_info:
    print(f"Temperature: {weather_info['temperature']}°C")
    print(f"Weather: {weather_info['weather']}")
    print(f"Wind Speed: {weather_info['wind_speed']}")
else:
    print(weather_info['error'])

class GoogleMap(Component):
    def render(self):
        lat, lon = 37.7749, -122.4194
        weather_info = get_weather_data(lat, lon)
        
        if 'error' not in weather_info:
            weather_description = weather_info['weather']
            temperature = weather_info['temperature']
            wind_speed = weather_info['wind_speed']
        else:
            weather_description = "Unknown"
            temperature = "N/A"
            wind_speed = "N/A"
        
        # Pass the weather data (including wind speed) to the JavaScript
        return f'''
        <div id="map" style="height: 500px; width: 100%;"></div>
        <script>
        function loadGoogleMapsScript(callback) {{
            var script = document.createElement('script');
            script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyAhDbwUcLTef3gG7ORV6TK5gtIkIpkEsxE&callback=' + callback;
            script.defer = true;
            document.head.appendChild(script);
        }}

        function initMap() {{
            console.log("Initializing Google Map");

            var map = new google.maps.Map(document.getElementById('map'), {{
                center: {{ lat: {lat}, lng: {lon} }},
                zoom: 8
            }});

            // Function to add weather markers
            function addWeatherMarker(lat, lon, weather, temp, wind) {{
                console.log(`Adding marker: lat=${{lat}}, lon=${{lon}}, weather=${{weather}}, temp=${{temp}}°C, wind=${{wind}} m/s`);

                var marker = new google.maps.Marker({{
                    position: {{ lat: lat, lng: lon }},
                    map: map
                }});

                var contentString = `
                    <div>
                        <h3>Weather Information</h3>
                        <p><b>Weather:</b> ${weather}</p>
                        <p><b>Temperature:</b> ${temp}°C</p>
                        <p><b>Wind Speed:</b> ${wind} m/s</p>
                    </div>
                `;

                var infoWindow = new google.maps.InfoWindow({{
                    content: contentString
                }});

                marker.addListener('click', function() {{
                    infoWindow.open(map, marker);
                }});
            }}

            // Adding weather marker with data from Python
            addWeatherMarker({lat}, {lon}, '{weather_description}', '{temperature}', '{wind_speed}');

            // add heatmap layer
            var heatmapData = [
                new google.maps.LatLng(37.7749, -122.4194),
                new google.maps.LatLng(37.7849, -122.4294),
                new google.maps.LatLng(37.7949, -122.4394)
                // add more later
            ];
            var heatmap = new google.maps.visualization.HeatmapLayer({{
            data: heatmapData,
            map: map
            }}
        }}

        // Dynamically load the Google Maps script
        loadGoogleMapsScript('initMap');
        </script>
        '''