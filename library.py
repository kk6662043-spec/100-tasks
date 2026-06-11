# Library Management System

books = []

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book = input("Enter Book Name: ")
        books.append(book)
        print("Book Added Successfully!")

    elif choice == "2":
        print("\nAvailable Books:")
        if len(books) == 0:
            print("No Books Available!")
        else:
            for i, book in enumerate(books, start=1):
                print(f"{i}. {book}")

    elif choice == "3":
        search = input("Enter Book Name to Search: ")

        if search in books:
            print("Book Found!")
        else:
            print("Book Not Found!")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")