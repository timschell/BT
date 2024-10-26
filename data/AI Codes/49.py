import datetime

class Event:
    def __init__(self, title, date, time):
        self.title = title
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.title} on {self.date} at {self.time}"

class EventReminder:
    def __init__(self):
        self.events = []

    def add_event(self, title, date, time):
        self.events.append(Event(title, date, time))

    def list_events(self):
        for event in self.events:
            print(event)

    def upcoming_events(self):
        now = datetime.datetime.now()
        upcoming = [event for event in self.events if datetime.datetime.strptime(event.date + ' ' + event.time, '%Y-%m-%d %H:%M') > now]
        return upcoming

def main():
    reminder = EventReminder()
    while True:
        print("\n1. Add Event")
        print("2. List Events")
        print("3. Upcoming Events")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            title = input("Enter event title: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            reminder.add_event(title, date, time)
        elif choice == '2':
            reminder.list_events()
        elif choice == '3':
            upcoming = reminder.upcoming_events()
            for event in upcoming:
                print(event)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
