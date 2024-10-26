import time

class Reminder:
    def __init__(self, message, timestamp):
        self.message = message
        self.timestamp = timestamp

    def __str__(self):
        return f"Reminder: {self.message} at {time.ctime(self.timestamp)}"

class ReminderSystem:
    def __init__(self):
        self.reminders = []

    def add_reminder(self, message, seconds_from_now):
        timestamp = time.time() + seconds_from_now
        self.reminders.append(Reminder(message, timestamp))

    def check_reminders(self):
        current_time = time.time()
        for reminder in self.reminders:
            if current_time >= reminder.timestamp:
                print(reminder)
                self.reminders.remove(reminder)

def main():
    reminder_system = ReminderSystem()
    while True:
        print("\n1. Add Reminder")
        print("2. Check Reminders")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            message = input("Enter reminder message: ")
            seconds = int(input("Enter time in seconds from now: "))
            reminder_system.add_reminder(message, seconds)
        elif choice == '2':
            reminder_system.check_reminders()
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1)

if __name__ == "__main__":
    main()
