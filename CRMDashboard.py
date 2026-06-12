# CRM Dashboard

customers = []

while True:
    print("\n=== CRM Dashboard ===")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Customer Name: ")
        email = input("Customer Email: ")

        customers.append({
            "name": name,
            "email": email
        })

        print("Customer added successfully!")

    elif choice == "2":
        if not customers:
            print("No customers found.")
        else:
            print("\nCustomer List:")
            for i, customer in enumerate(customers, start=1):
                print(f"{i}. Name: {customer['name']}, Email: {customer['email']}")

    elif choice == "3":
        print("Exiting CRM Dashboard...")
        break

    else:
        print("Invalid choice! Please try again.")