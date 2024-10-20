import requests

def get_weather_data (lat, lon):
    api_key = "5664c977559d1754054038d48cb98c67" # API key for open weather
    base_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    try:
        response = requests.get(base_url)
        data = response.json()
        print(data)
        if response.status_code == 200:
            data = response.json()
            return {
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "weather": data["weather"][0]["description"],
                'icon': data['weather'][0]['icon'],
                'wind_speed': data['wind']['speed'] # wind speed
                
            }
        else:
            return {'error': f"Error fetching weatherdataw: {response.status_code}"}
    except Exception as e:
        return {'error': f"An error occurred: {str(e)}"}