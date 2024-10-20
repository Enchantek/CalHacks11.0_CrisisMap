let map;

function initMap() {
    // Initialize the Google Map centered on a default location
    map = new google.maps.Map(document.getElementById("map"), {
        zoom: 6,
        center: { lat: 25.7617, lng: -80.1918 }, // Miami as default center
    });
    // Fetch and display weather data
    fetchWeatherData();
}

async function fetchWeatherData() {
    const api_key = '30bfedf90f5f33c670ff02053c1e493e';
    const url = `api.openweathermap.org/data/2.5/forecast?lat=44.34&lon=10.99&appid={30bfedf90f5f33c670ff02053c1e493e}`;

    try {
        const response = await fetch(url);
        const data = await response.json();
        console.log(data);
        // const hurricaneCoordinates = [
        //     { lat: 25.7617, lng: -80.1918 },
        //     { lat: 26.7617, lng: -81.1918 },
        //     { lat: 27.7617, lng: -82.1918 },
        // ];

        addHurricaneZone(map, hurricaneCoordinates);
    } catch (error) {
        console.error("Error fetching weather data:", error);
    }
}

function addHurricaneZone(map, hurricaneCoordinates) {
    const dangerZone = new google.maps.Polygon({
        paths: hurricaneCoordinates,
        strokeColor: "#FF0000",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#FF0000",
        fillOpacity: 0.35,
    });
    dangerZone.setMap(map);
}
