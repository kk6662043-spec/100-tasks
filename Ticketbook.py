# Bus Ticket Booking App

available_seats = 5
bookings = []

while True:
    print("\n--- Bus Ticket Booking System ---")
    print("1. View Available Seats")
    print("2. Book Ticket")
    print("3. View Bookings")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print(f"Available Seats: {available_seats}")

    elif choice == "2":
        if available_seats > 0:
            name = input("Enter Passenger Name: ")

            bookings.append(name)
            available_seats -= 1

            print("Ticket Booked Successfully!")
        else:
            print("No Seats Available!")

    elif choice == "3":
        print("\nBooked Passengers:")
        if len(bookings) == 0:
            print("No Bookings Found!")
        else:
            for i, passenger in enumerate(bookings, start=1):
                print(f"{i}. {passenger}")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")