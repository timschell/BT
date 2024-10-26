class WeightEntry:
    def __init__(self, date, weight):
        self.date = date
        self.weight = weight

    def __str__(self):
        return f"{self.date}: {self.weight} kg"

class WeightTracker:
    def __init__(self):
        self.entries = []

    def add_entry(self, date, weight):
        self.entries.append(WeightEntry(date, weight))

    def list_entries(self):
        for entry in self.entries:
            print(entry)

def main():
    tracker = WeightTracker()
    while True:
        print("\n1. Add Weight Entry")
        print("2. List Weight Entries")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            weight = float(input("Enter weight (kg): "))
            tracker.add_entry(date, weight)
        elif choice == '2':
            tracker.list_entries()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
