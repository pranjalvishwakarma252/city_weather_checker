import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_weather(city_name, api_key, base_url):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    """
    url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # Extract useful info
        city = data["name"]
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        print(f"📍 City: {city}")
        print(f"🌡 Temperature: {temp}°C")
        print(f"☁️ Weather: {weather}")
        print(f"💧 Humidity: {humidity}%")
        print(f"🌬 Wind Speed: {wind_speed} m/s")

    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
    except KeyError:
        print("Unexpected response format. Check API details.")

if __name__ == "__main__":
    # Load API key and base URL from environment
    API_KEY = os.getenv("API_KEY")
    BASE_URL = os.getenv("BASE_URL")

    city = input("Enter city name: ")
    get_weather(city, API_KEY, BASE_URL)