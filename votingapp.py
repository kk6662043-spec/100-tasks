votes = {"Python": 0, "Java": 0}

print("Vote:")
print("1. Python")
print("2. Java")

choice = input("Enter 1 or 2: ")

if choice == "1":
    votes["Python"] += 1
elif choice == "2":
    votes["Java"] += 1
else:
    print("Invalid vote")

print("Results:", votes)