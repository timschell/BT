import datetime

class WeatherEntry:
    def __init__(self, date, temperature, conditions):
        self.date = date
        self.temperature = temperature
        self.conditions = conditions

    def __str__(self):
        return f"{self.date}: {self.temperature}°C, {self.conditions}"

class WeatherLogger:
    def __init__(self):
        self.entries = []

    def add_entry(self, date, temperature, conditions):
        self.entries.append(WeatherEntry(date, temperature, conditions))

    def list_entries(self):
        for entry in self.entries:
            print(entry)

    def average_temperature(self):
        if not self.entries:
            return 0
        return sum(entry.temperature for entry in self.entries) / len(self.entries)

def main():
    logger = WeatherLogger()
    while True:
        print("\n1. Add Weather Entry")
        print("2. List Weather Entries")
        print("3. Average Temperature")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            temperature = float(input("Enter temperature (°C): "))
            conditions = input("Enter weather conditions: ")
            logger.add_entry(date, temperature, conditions)
        elif choice == '2':
            logger.list_entries()
        elif choice == '3':
            print(f"Average temperature: {logger.average_temperature()}°C")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
