import json

FILE = "tasks.json"

try:
    with open(FILE, "r") as f:
        tasks = json.load(f)
except:
    tasks = []

def save():
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_menu():
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║       📋  T O - D O   C L I   A P P         ║")
    print("╠══════════════════════════════════════════════╣")
    print("║                                              ║")
    print("║   1.  ➕  Add Task                           ║")
    print("║   2.  📄  View Tasks                         ║")
    print("║   3.  ✅  Mark Task as Done                  ║")
    print("║   4.  ❌  Remove Task                        ║")
    print("║   5.  🚪  Exit                               ║")
    print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")

def add_task():
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║            ➕  ADD NEW TASK                  ║")
    print("╚══════════════════════════════════════════════╝")
    task = input("  Enter task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save()
        print()
        print("╔══════════════════════════════════════════════╗")
        print("║   [+]  Task added successfully!              ║")
        print("╚══════════════════════════════════════════════╝")
    else:
        print("  ⚠️  No task entered.")

def view_tasks():
    print()
    print("╔══════════════════════════════════════════════╗")
    print("║          📄  Y O U R   T A S K S            ║")
    print("╠══════════════════════════════════════════════╣")
    if not tasks:
        print("║                                              ║")
        print("║   ⚠️  No tasks available.                    ║")
        print("║                                              ║")
    else:
        print("║                                              ║")
        for i, t in enumerate(tasks, 1):
            status = "✔" if t["done"] else "○"
            line = f"   {i:>2}.  [{status}]  {t['task']}"
            print("║" + line.ljust(46) + "║")
        print("║                                              ║")
    print("╚══════════════════════════════════════════════╝")

def mark_done():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to mark done: "))
        tasks[num - 1]["done"] = True
        save()
        print()
        print("╔══════════════════════════════════════════════╗")
        print("║   ✅  Task marked as done!                   ║")
        print("╚══════════════════════════════════════════════╝")
    except:
        print("  ⚠️  Invalid input.")

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("  Enter task number to remove: "))
        removed = tasks.pop(num - 1)
        save()
        print()
        print("╔══════════════════════════════════════════════╗")
        print("║   ✗  Task removed successfully!              ║")
        print("╚══════════════════════════════════════════════╝")
    except:
        print("  ⚠️  Invalid input.")

while True:
    show_menu()
    choice = input("  👉  Choice: ").strip()
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_done()
    elif choice == "4":
        remove_task()
    elif choice == "5":
        print()
        print("╔══════════════════════════════════════════════╗")
        print("║   ✅  Exited the app successfully.            ║")
        print("╚══════════════════════════════════════════════╝")
        break
    else:
        print()
        print("╔══════════════════════════════════════════════╗")
        print("║   ⚠️  Invalid choice. Try again.             ║")
        print("╚══════════════════════════════════════════════╝")