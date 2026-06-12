# Event Management System

events = []

while True:
    print("\n===== Event Management System =====")
    print("1. Add Event")
    print("2. View Events")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Event Name: ")
        date = input("Enter Event Date (DD-MM-YYYY): ")
        location = input("Enter Event Location: ")

        events.append({
            "name": name,
            "date": date,
            "location": location
        })

        print("Event added successfully!")

    elif choice == "2":
        if not events:
            print("No events available.")
        else:
            print("\n--- Event List ---")
            for i, event in enumerate(events, start=1):
                print(f"\nEvent {i}")
                print("Name:", event["name"])
                print("Date:", event["date"])
                print("Location:", event["location"])

    elif choice == "3":
        print("Exiting Event Management System...")
        break

    else:
        print("Invalid choice! Please try again.")