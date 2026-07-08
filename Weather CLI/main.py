import requests
from dotenv import load_dotenv
import os
from rich.console import Console

load_dotenv()
API_KEY = os.getenv("API_KEY")
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

console = Console()

def get_weather(city):
    params = {"q" : city, "appid" : API_KEY, "units" : "metric"}
    response = requests.get(BASE_URL, params=params)
    return response.json()

def display_weather(data):
    console.print(f"🌍 City: {data["name"]}")
    console.print(f"🌡️ Temp: {data["main"]["temp"]}°C")
    console.print(f"💧 Humidity: {data["main"]["humidity"]}%")
    console.print(f"💨 Wind: {data["wind"]["speed"]} m/s")
    console.print(f"☁️ Condition: {data["weather"][0]["description"]}")

def main():
    city = input("Enter City: ")
    data = get_weather(city)

    if data.get("cod") != 200:
        print(f"❌ Error: {data.get('message')}")
    else:
        display_weather(data)

main()