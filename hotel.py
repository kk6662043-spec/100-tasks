# Hotel Booking System

rooms = {
    101: "Available",
    102: "Available",
    103: "Available"
}

while True:
    print("\n--- Hotel Booking System ---")
    print("1. View Rooms")
    print("2. Book Room")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nRoom Status:")
        for room, status in rooms.items():
            print(f"Room {room}: {status}")

    elif choice == "2":
        room_no = int(input("Enter Room Number: "))

        if room_no in rooms:
            if rooms[room_no] == "Available":
                customer = input("Enter Customer Name: ")
                rooms[room_no] = f"Booked by {customer}"
                print("Room Booked Successfully!")
            else:
                print("Room Already Booked!")
        else:
            print("Invalid Room Number!")

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")