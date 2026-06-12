# Customer Feedback System

feedbacks = []

while True:
    print("\n--- Customer Feedback System ---")
    print("1. Add Feedback")
    print("2. View Feedback")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Customer Name: ")
        rating = input("Rating (1-5): ")
        comment = input("Feedback: ")

        feedbacks.append({
            "name": name,
            "rating": rating,
            "comment": comment
        })

        print("Feedback added successfully!")

    elif choice == "2":
        if not feedbacks:
            print("No feedback available.")
        else:
            print("\nCustomer Feedbacks:")
            for i, fb in enumerate(feedbacks, start=1):
                print(f"\nFeedback {i}")
                print("Name:", fb["name"])
                print("Rating:", fb["rating"])
                print("Comment:", fb["comment"])

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")