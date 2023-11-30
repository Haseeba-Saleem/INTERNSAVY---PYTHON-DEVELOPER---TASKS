import os

# File to store tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            for line in file:
                task_info = line.strip().split("|")
                try:
                    tasks.append({
                        "id": int(task_info[0]),
                        "description": task_info[1],
                        "status": task_info[2]
                    })
                except ValueError:
                    print(f"Skipping invalid line: {line}")
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task['id']}|{task['description']}|{task['status']}\n")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("ID | Description | Status")
        print("-" * 30)
        for task in tasks:
            print(f"{task['id']} | {task['description']} | {task['status']}")

def add_task(tasks, description):
    new_id = 1 if not tasks else max(task['id'] for task in tasks) + 1
    tasks.append({"id": new_id, "description": description, "status": "Pending"})
    save_tasks(tasks)
    print(f"Task added with ID: {new_id}")

def complete_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'Completed'
            save_tasks(tasks)
            print(f"Task {task_id} marked as completed.")
            return
    print(f"No task found with ID: {task_id}")

def main():
    tasks = load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            description = input("Enter task description: ")
            add_task(tasks, description)
        elif choice == "3":
            task_id = int(input("Enter task ID to mark as completed: "))
            complete_task(tasks, task_id)
        elif choice == "4":
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
