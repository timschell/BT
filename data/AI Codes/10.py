import random

class WeatherScraper:
    def get_weather(self, city):
        weather_conditions = ["Sunny", "Rainy", "Cloudy", "Windy", "Snowy"]
        temperature = random.randint(-10, 40)
        condition = random.choice(weather_conditions)
        return f"The weather in {city} is currently {condition} with a temperature of {temperature}°C."

def main():
    scraper = WeatherScraper()
    while True:
        city = input("Enter a city (or 'exit' to quit): ")
        if city.lower() == 'exit':
            break
        else:
            print(scraper.get_weather(city))

if __name__ == "__main__":
    main()
