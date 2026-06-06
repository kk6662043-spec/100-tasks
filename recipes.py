recipes = {}

while True:
    choice = input("\n(1) Add (2) View (3) Exit: ")

    if choice == "1":
        name = input("Recipe name: ")
        recipe = input("Recipe: ")
        recipes[name] = recipe
        print("Added!")

    elif choice == "2":
        name = input("Search recipe: ")
        print(recipes.get(name, "Not found"))

    elif choice == "3":
        break

    else:
        print("Invalid")