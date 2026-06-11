# Freelancer Marketplace - Simple Example

freelancers = []
jobs = []

while True:
    print("\n--- Freelancer Marketplace ---")
    print("1. Register Freelancer")
    print("2. Post Job")
    print("3. View Freelancers")
    print("4. View Jobs")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Freelancer Name: ")
        skill = input("Skill: ")
        freelancers.append({"name": name, "skill": skill})
        print("Freelancer Registered Successfully!")

    elif choice == "2":
        title = input("Job Title: ")
        budget = input("Budget: ")
        jobs.append({"title": title, "budget": budget})
        print("Job Posted Successfully!")

    elif choice == "3":
        print("\n--- Freelancers ---")
        for f in freelancers:
            print(f"Name: {f['name']}, Skill: {f['skill']}")

    elif choice == "4":
        print("\n--- Jobs ---")
        for j in jobs:
            print(f"Job: {j['title']}, Budget: ₹{j['budget']}")

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")