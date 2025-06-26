import json

FILE_NAME = "todo.txt"

def load_tasks():
    try:
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    with open(FILE_NAME, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(tasks):
    title = input("Enter task title: ")
    task = {
        "title": title,
        "completed": False
    }
    tasks.append(task)
    print("Task added.")

def view_tasks(tasks):
    if not tasks:
        print("No tasks to show.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. [{status}] {task['title']}")

def mark_task_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted = tasks.pop(index)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_task_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
