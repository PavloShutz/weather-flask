import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')


def get_current_city():
    """Get the current city."""
    location = requests.get('http://ip-api.com/json')
    city = location.json()['city']
    return city


def get_weather():
    """Get weather for the current city."""
    city = get_current_city()
    url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric&lang=en'
    response = requests.get(url)
    data = response.json()
    weather_for_the_next_5_days = [
        {
            'icon': f'http://openweathermap.org/img/wn/{data["list"][day]["weather"][0]["icon"]}@2x.png',
            'description': data["list"][day]["weather"][0]["description"],
            'temperature': data['list'][day]['main']['temp'],
            'speed_of_wind': data['list'][day]['wind']['speed']
        }
        for day in range(5)
    ]
    return weather_for_the_next_5_days


if __name__ == '__main__':
    print(get_weather())
