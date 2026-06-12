# Complaint Management Portal

complaints = []

while True:
    print("\n=== Complaint Management Portal ===")
    print("1. Add Complaint")
    print("2. View Complaints")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your name: ")
        complaint = input("Enter complaint: ")

        complaints.append({
            "name": name,
            "complaint": complaint
        })

        print("Complaint submitted successfully!")

    elif choice == "2":
        if not complaints:
            print("No complaints found.")
        else:
            print("\nComplaint List:")
            for i, c in enumerate(complaints, start=1):
                print(f"{i}. {c['name']} - {c['complaint']}")

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Please try again.")