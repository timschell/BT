class TodoItem:
    def __init__(self, task, priority):
        self.task = task
        self.priority = priority

    def __str__(self):
        return f"{self.task} - Priority: {self.priority}"

class TodoList:
    def __init__(self):
        self.items = []

    def add_item(self, task, priority):
        self.items.append(TodoItem(task, priority))

    def list_items(self):
        for item in sorted(self.items, key=lambda x: x.priority):
            print(item)

def main():
    todo_list = TodoList()
    while True:
        print("\n1. Add Todo Item")
        print("2. List Todo Items")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            break
        elif choice == '1':
            task = input("Enter task: ")
            priority = int(input("Enter priority (1 is highest): "))
            todo_list.add_item(task, priority)
        elif choice == '2':
            todo_list.list_items()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
