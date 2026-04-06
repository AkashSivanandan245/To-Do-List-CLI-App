import json

FILE = "tasks.json"

try:
    with open(FILE, "r") as f:
        tasks = json.load(f)
except:
    tasks = []

while True:
    print("\n1. Add Task")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        with open(FILE, "w") as f:
            json.dump(tasks, f)

    elif choice == "2":
        break

    else:
        print("Invalid choice")