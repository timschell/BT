class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"{self.description} - {status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def complete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].completed = True
        else:
            print("Invalid task number.")

    def list_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index + 1}. {task}")

def main():
    todo = ToDoList()
    while True:
        print("\n1. Add Task")
        print("2. Complete Task")
        print("3. List Tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")
        if choice == '4':
            break
        elif choice == '1':
            description = input("Enter task description: ")
            todo.add_task(description)
        elif choice == '2':
            index = int(input("Enter task number to complete: ")) - 1
            todo.complete_task(index)
        elif choice == '3':
            todo.list_tasks()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
