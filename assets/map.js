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