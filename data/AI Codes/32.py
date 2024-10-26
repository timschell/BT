class Trip:
    def __init__(self, date, miles):
        self.date = date
        self.miles = miles

    def __str__(self):
        return f"{self.date}: {self.miles} miles"

class MileageTracker:
    def __init__(self):
        self.trips = []

    def add_trip(self, date, miles):
        self.trips.append(Trip(date, miles))

    def list_trips(self):
        for trip in self.trips:
            print(trip)

    def total_miles(self):
        return sum(trip.miles for trip in self.trips)

def main():
    tracker = MileageTracker()
    while True:
        print("\n1. Add Trip")
        print("2. List Trips")
        print("3. Total Miles")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            miles = float(input("Enter miles: "))
            tracker.add_trip(date, miles)
        elif choice == '2':
            tracker.list_trips()
        elif choice == '3':
            print(f"Total miles: {tracker.total_miles()}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
