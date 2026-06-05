notes = []

while True:
    print("\n1. Add Note")
    print("2. View Notes")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        note = input("Enter note: ")
        notes.append(note)

    elif choice == "2":
        print("\nNotes:")
        for i, note in enumerate(notes, 1):
            print(f"{i}. {note}")

    elif choice == "3":
        break

    else:
        print("Invalid choice")