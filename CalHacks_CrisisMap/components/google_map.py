#https://maps.googleapis.com/maps/api/js?key=AIzaSyBmIovXybK7OPKtoADkd1WpSq7iMAkCctw&callback=initMap
#https://maps.googleapis.com/maps/api/js?key=AIzaSyABud6rxzKEJjIWnYedmenSem0_basmLsY&callback=

import reflex as rx
import requests

def google_map(lat=37.7749, lon=-122.4194, heatmap_data=None):
    # Create a string for heatmap data points in JavaScript
    heatmap_data_js = ','.join([f"new google.maps.LatLng({lat}, {lon})" for lat, lon in heatmap_data]) if heatmap_data else ""

    return rx.html(f"""
        <div id="map" style="height: 1000px; width: 100%;"></div>
        <script>
            function initMap() {{
                var map = new google.maps.Map(document.getElementById('map'), {{
                    center: {{ lat: {lat}, lng: {lon} }},
                    zoom: 8
                }});

                if ({'true' if heatmap_data else 'false'}) {{
                    var heatmap = new google.maps.visualization.HeatmapLayer({{
                        data: [
                            {heatmap_data_js}
                        ],
                        map: map
                    }});
                }}
            }}
        </script>
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyABud6rxzKEJjIWnYedmenSem0_basmLsY&libraries=visualization&callback=initMap" async defer></script>
    """)