class Event:
    def __init__(self, name, date, time):
        self.name = name
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.name} on {self.date} at {self.time}"

class EventPlanner:
    def __init__(self):
        self.events = []

    def add_event(self, name, date, time):
        self.events.append(Event(name, date, time))

    def list_events(self):
        for event in self.events:
            print(event)

def main():
    planner = EventPlanner()
    while True:
        print("\n1. Add Event")
        print("2. List Events")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            name = input("Enter event name: ")
            date = input("Enter date (YYYY-MM-DD): ")
            time = input("Enter time (HH:MM): ")
            planner.add_event(name, date, time)
        elif choice == '2':
            planner.list_events()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
