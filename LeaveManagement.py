# Leave Management System

leave_requests = []

while True:
    print("\n=== Leave Management System ===")
    print("1. Apply Leave")
    print("2. View Leave Requests")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        employee = input("Enter Employee Name: ")
        days = input("Enter Number of Leave Days: ")

        leave_requests.append({
            "employee": employee,
            "days": days
        })

        print("Leave request submitted successfully!")

    elif choice == "2":
        if not leave_requests:
            print("No leave requests found.")
        else:
            print("\nLeave Requests:")
            for i, leave in enumerate(leave_requests, start=1):
                print(f"{i}. {leave['employee']} - {leave['days']} day(s)")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid choice. Try again.")