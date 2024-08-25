class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"{self.name} [{status}]"

tasks = []

def add_task(name):
    task = Task(name)
    tasks.append(task)

def view_tasks():
    if not tasks:
        print("No tasks in the list.")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def mark_task_completed(index):
    try:
        tasks[index - 1].mark_completed()
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter task name: ")
            add_task(name)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            try:
                index = int(input("Enter task number to mark as completed: "))
                mark_task_completed(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
