import requests
import json

API_KEY = "YOUR_API_KEY"
CITY = "Hyderabad"

URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather():
    response = requests.get(URL)
    data = response.json()

    weather_data = {
        "city": CITY,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["description"]
    }

    with open("../data/weather_data.json", "w") as f:
        json.dump(weather_data, f, indent=4)

    print("Data fetched successfully!")

if __name__ == "__main__":
    fetch_weather()