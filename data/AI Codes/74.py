def add_task(task_list, task):
    task_list.append(task)

def save_tasks(task_list):
    with open('tasks.txt', 'w') as file:
        for task in task_list:
            file.write(task + "\n")
    print("Tasks saved.")

def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            return file.read().splitlines()
    except FileNotFoundError:
        return []

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Save and Quit")

        choice = input("Enter your choice: ")
        if choice == '3':
            save_tasks(tasks)
            break
        elif choice == '1':
            task = input("Enter task: ")
            add_task(tasks, task)
        elif choice == '2':
            for task in tasks:
                print(task)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
