# To-Do List App in Python

# Initialize an empty list to store tasks
tasks = []

def display_tasks():
    """Display all tasks in the list."""
    if not tasks:
        print("\nNo tasks in the to-do list.\n")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
        print()

def add_task():
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!\n")
    else:
        print("Task cannot be empty.\n")

def edit_task():
    """Edit an existing task."""
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to edit: "))
            if 1 <= task_num <= len(tasks):
                new_task = input("Enter the updated task: ").strip()
                if new_task:
                    tasks[task_num - 1] = new_task
                    print("Task updated successfully!\n")
                else:
                    print("Task cannot be empty.\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def delete_task():
    """Delete a task from the list."""
    display_tasks()
    if tasks:
        try:
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task}' deleted successfully!\n")
            else:
                print("Invalid task number.\n")
        except ValueError:
            print("Please enter a valid number.\n")

def clear_tasks():
    """Clear all tasks from the list."""
    confirm = input("Are you sure you want to clear all tasks? (yes/no): ").lower()
    if confirm == "yes":
        tasks.clear()
        print("All tasks cleared successfully!\n")
    else:
        print("Operation canceled.\n")

def to_do_list():
    """Main function to run the To-Do List app."""
    while True:
        print("To-Do List Menu:")
        print("1. Display Tasks")
        print("2. Add Task")
        print("3. Edit Task")
        print("4. Delete Task")
        print("5. Clear All Tasks")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()
        print()

        if choice == "1":
            display_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            clear_tasks()
        elif choice == "6":
            print("Exiting the To-Do List App. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the To-Do List App
if __name__ == "__main__":
    to_do_list()
