import requests

def get_weather_data (lat, lon):
    api_key = "05405fe3529fd2f607778d7b5f7122bb" # API key for open weather
    base_url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"

    response = requests.get(base_url)
    data = response.json()
    
    if response.status_code == 200:
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        wind_speed = data['wind']['speed']
        return {
            "weather": weather,
            "temperature": temperature,
            "wind_speed": wind_speed
        }
    else:
        return {"error": "Unable to fetch weather data"}