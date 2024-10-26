class Habit:
    def __init__(self, name):
        self.name = name
        self.completed_days = set()

    def mark_completed(self, day):
        self.completed_days.add(day)

    def __str__(self):
        return f"{self.name}: {len(self.completed_days)} days completed"

class HabitTracker:
    def __init__(self):
        self.habits = []

    def add_habit(self, name):
        self.habits.append(Habit(name))

    def mark_habit_completed(self, name, day):
        for habit in self.habits:
            if habit.name == name:
                habit.mark_completed(day)
                return
        print("Habit not found.")

    def list_habits(self):
        for habit in self.habits:
            print(habit)

def main():
    tracker = HabitTracker()
    while True:
        print("\n1. Add Habit")
        print("2. Mark Habit Completed")
        print("3. List Habits")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            name = input("Enter habit name: ")
            tracker.add_habit(name)
        elif choice == '2':
            name = input("Enter habit name: ")
            day = input("Enter day (YYYY-MM-DD): ")
            tracker.mark_habit_completed(name, day)
        elif choice == '3':
            tracker.list_habits()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
