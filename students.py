students = {}

while True:
    choice = input("\n1:Add 2:View 3:Update 4:Delete 5:Exit\nChoose: ")

    if choice == "1":
        roll = input("Roll No: ")
        name = input("Name: ")
        students[roll] = name

    elif choice == "2":
        print(students)

    elif choice == "3":
        roll = input("Roll No: ")
        if roll in students:
            students[roll] = input("New Name: ")

    elif choice == "4":
        roll = input("Roll No: ")
        students.pop(roll, None)

    elif choice == "5":
        break