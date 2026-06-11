# Employee Management System

employees = {}

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")
        salary = input("Enter Employee Salary: ")

        employees[emp_id] = {
            "Name": name,
            "Salary": salary
        }

        print("Employee Added Successfully!")

    elif choice == "2":
        if not employees:
            print("No Employee Records Found!")
        else:
            print("\nEmployee List")
            print("-" * 30)
            for emp_id, details in employees.items():
                print(f"ID: {emp_id}")
                print(f"Name: {details['Name']}")
                print(f"Salary: {details['Salary']}")
                print("-" * 30)

    elif choice == "3":
        emp_id = input("Enter Employee ID to Search: ")

        if emp_id in employees:
            print("\nEmployee Found")
            print("ID:", emp_id)
            print("Name:", employees[emp_id]["Name"])
            print("Salary:", employees[emp_id]["Salary"])
        else:
            print("Employee Not Found!")

    elif choice == "4":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")