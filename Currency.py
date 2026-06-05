print("Currency Converter")
print("1. USD to INR")
print("2. INR to USD")

choice = input("Choose (1/2): ")

if choice == "1":
    usd = float(input("Enter USD: "))
    print("INR:", usd * 83)

elif choice == "2":
    inr = float(input("Enter INR: "))
    print("USD:", inr / 83)

else:
    print("Invalid choice")