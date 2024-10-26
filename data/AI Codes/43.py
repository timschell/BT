class StudySession:
    def __init__(self, subject, duration):
        self.subject = subject
        self.duration = duration

    def __str__(self):
        return f"{self.subject}: {self.duration} minutes"

class StudyPlanner:
    def __init__(self):
        self.sessions = []

    def add_session(self, subject, duration):
        self.sessions.append(StudySession(subject, duration))

    def list_sessions(self):
        for session in self.sessions:
            print(session)

    def total_study_time(self):
        return sum(session.duration for session in self.sessions)

def main():
    planner = StudyPlanner()
    while True:
        print("\n1. Add Study Session")
        print("2. List Study Sessions")
        print("3. Total Study Time")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            subject = input("Enter subject: ")
            duration = int(input("Enter duration (minutes): "))
            planner.add_session(subject, duration)
        elif choice == '2':
            planner.list_sessions()
        elif choice == '3':
            print(f"Total study time: {planner.total_study_time()} minutes")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
