from datetime import datetime

class Task:
    def __init__(self, title, due_date):
        self.title = title
        self.due_date = due_date

    def __str__(self):
        return f"{self.title} - Due: {self.due_date}"

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, due_date):
        self.tasks.append(Task(title, due_date))

    def list_tasks(self):
        for task in self.tasks:
            print(task)

    def upcoming_tasks(self):
        now = datetime.now().date()
        upcoming = [task for task in self.tasks if datetime.strptime(task.due_date, '%Y-%m-%d').date() >= now]
        return upcoming

def main():
    scheduler = TaskScheduler()
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Upcoming Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            title = input("Enter task title: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            scheduler.add_task(title, due_date)
        elif choice == '2':
            scheduler.list_tasks()
        elif choice == '3':
            upcoming = scheduler.upcoming_tasks()
            for task in upcoming:
                print(task)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
