import time

class Task:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f"{self.name}: {self.duration} seconds"

class TaskTimer:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, duration):
        self.tasks.append(Task(name, duration))

    def start_timer(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                print(f"Starting timer for {task.name}...")
                time.sleep(task.duration)
                print(f"{task.name} completed!")
                return
        print("Task not found.")

    def list_tasks(self):
        for task in self.tasks:
            print(task)

def main():
    timer = TaskTimer()
    while True:
        print("\n1. Add Task")
        print("2. Start Task Timer")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            name = input("Enter task name: ")
            duration = int(input("Enter duration (seconds): "))
            timer.add_task(name, duration)
        elif choice == '2':
            task_name = input("Enter task name to start: ")
            timer.start_timer(task_name)
        elif choice == '3':
            timer.list_tasks()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
