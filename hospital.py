# Hospital Management System

patients = []

while True:
    print("\n=== Hospital Management System ===")
    print("1. Add Patient")
    print("2. View Patients")
    print("3. Search Patient")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter Patient Name: ")
        age = input("Enter Age: ")
        disease = input("Enter Disease: ")

        patient = {
            "Name": name,
            "Age": age,
            "Disease": disease
        }

        patients.append(patient)
        print("Patient added successfully!")

    elif choice == "2":
        if len(patients) == 0:
            print("No patient records found.")
        else:
            print("\nPatient Records:")
            for p in patients:
                print(f"Name: {p['Name']}, Age: {p['Age']}, Disease: {p['Disease']}")

    elif choice == "3":
        search_name = input("Enter Patient Name to Search: ")

        found = False
        for p in patients:
            if p["Name"].lower() == search_name.lower():
                print("\nPatient Found:")
                print(f"Name: {p['Name']}")
                print(f"Age: {p['Age']}")
                print(f"Disease: {p['Disease']}")
                found = True

        if not found:
            print("Patient not found.")

    elif choice == "4":
        print("Thank you!")
        break

    else:
        print("Invalid choice. Try again.")