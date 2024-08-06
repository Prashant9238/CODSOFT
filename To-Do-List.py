tasks = []
def display_menu():
    print("Welcome to To-Do List App")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")
    print()
def view_todo_list():
    if not tasks:
        print("Your To-Do List is empty!")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print(f"Task '{task}' added to the To-Do List.")
def mark_completed():
    view_todo_list()
    if tasks:
        try:
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            if 0 <= task_index < len(tasks):
                print(f"Marked '{tasks[task_index]}' as completed.")
                del tasks[task_index]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to mark as completed.")
def delete_task():
    view_todo_list()
    if tasks:
        try:
            task_index = int(input("Enter the task number to delete: ")) - 1
            if 0 <= task_index < len(tasks):
                print(f"Deleted '{tasks[task_index]}' from the To-Do List.")
                del tasks[task_index]
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No tasks to delete")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_todo_list()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_completed()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
