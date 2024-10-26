def display_todo_list(todo_list):
    print("\nTo-Do List:")
    for i, task in enumerate(todo_list):
        print(f"{i+1}. {task}")
    print()

def main():
    todo_list = []
    while True:
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            todo_list.append(task)
        elif choice == '2':
            task_number = int(input("Enter task number to remove: ")) - 1
            if 0 <= task_number < len(todo_list):
                todo_list.pop(task_number)
            else:
                print("Invalid task number.")
        elif choice == '3':
            display_todo_list(todo_list)
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
   
