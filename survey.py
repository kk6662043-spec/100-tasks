# Survey Management System

surveys = []

while True:
    print("\n--- Survey Management System ---")
    print("1. Take Survey")
    print("2. View Responses")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter your Name: ")
        age = input("Enter your Age: ")

        print("\nSurvey Question:")
        answer = input("Are you satisfied with our service? (Yes/No): ")

        surveys.append({
            "name": name,
            "age": age,
            "answer": answer
        })

        print("Survey submitted successfully!")

    elif choice == "2":
        if not surveys:
            print("No survey responses found.")
        else:
            print("\n--- Survey Responses ---")
            for i, survey in enumerate(surveys, start=1):
                print(f"\nResponse {i}")
                print("Name:", survey["name"])
                print("Age:", survey["age"])
                print("Answer:", survey["answer"])

    elif choice == "3":
        print("Exiting Survey System...")
        break

    else:
        print("Invalid choice. Please try again.")