class Workout:
    def __init__(self, date, exercises):
        self.date = date
        self.exercises = exercises

    def __str__(self):
        return f"{self.date}: {', '.join(self.exercises)}"

class WorkoutTracker:
    def __init__(self):
        self.workouts = []

    def add_workout(self, date, exercises):
        self.workouts.append(Workout(date, exercises))

    def list_workouts(self):
        for workout in self.workouts:
            print(workout)

def main():
    tracker = WorkoutTracker()
    while True:
        print("\n1. Add Workout")
        print("2. List Workouts")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            exercises = input("Enter exercises (comma separated): ").split(", ")
            tracker.add_workout(date, exercises)
        elif choice == '2':
            tracker.list_workouts()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
