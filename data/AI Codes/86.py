def get_weather(city):
    # Mock weather data
    weather_data = {
        "New York": "Sunny, 25°C",
        "London": "Rainy, 15°C",
        "Tokyo": "Cloudy, 20°C"
    }
    return weather_data.get(city, "Weather data not available.")

def main():
    print("Weather Application")
    city = input("Enter city name: ")
    weather = get_weather(city)
    print(f"Weather in {city}: {weather}")

if __name__ == "__main__":
    main()
