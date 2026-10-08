import os
import requests

API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    print("API key not found.")
    print("Please set the OPENWEATHER_API_KEY environment variable.")
    exit()

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n--- Weather Information ---")
        print("City:", city)
        print("Temperature:", temperature, "°C")
        print("Humidity:", humidity, "%")
        print("Weather:", weather)
        print("Wind Speed:", wind_speed, "m/s")

    elif response.status_code == 404:
        print("City not found.")

    elif response.status_code == 401:
        print("Invalid API key.")

    else:
        print("Unable to fetch weather data.")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException:
    print("Network error. Please check your internet connection.")