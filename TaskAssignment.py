# Task Assignment System

tasks = []

while True:
    print("\n=== Task Assignment System ===")
    print("1. Assign Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee = input("Enter employee name: ")
        task = input("Enter task: ")

        tasks.append({
            "employee": employee,
            "task": task
        })

        print("Task assigned successfully!")

    elif choice == "2":
        if not tasks:
            print("No tasks assigned.")
        else:
            print("\nAssigned Tasks:")
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['employee']} -> {t['task']}")

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")