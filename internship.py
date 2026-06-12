# Student Internship Portal

internships = [
    {"id": 1, "company": "ABC Tech", "role": "Python Intern"},
    {"id": 2, "company": "XYZ Solutions", "role": "Web Developer Intern"},
]

applications = []

while True:
    print("\n=== Student Internship Portal ===")
    print("1. View Internships")
    print("2. Apply for Internship")
    print("3. View Applications")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("\nAvailable Internships:")
        for internship in internships:
            print(
                f"ID: {internship['id']} | "
                f"Company: {internship['company']} | "
                f"Role: {internship['role']}"
            )

    elif choice == "2":
        name = input("Enter Student Name: ")
        internship_id = int(input("Enter Internship ID: "))

        found = False
        for internship in internships:
            if internship["id"] == internship_id:
                applications.append({
                    "student": name,
                    "company": internship["company"],
                    "role": internship["role"]
                })
                print("Application Submitted Successfully!")
                found = True
                break

        if not found:
            print("Invalid Internship ID!")

    elif choice == "3":
        print("\nApplications:")
        if len(applications) == 0:
            print("No applications found.")
        else:
            for app in applications:
                print(
                    f"Student: {app['student']} | "
                    f"Company: {app['company']} | "
                    f"Role: {app['role']}"
                )

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")