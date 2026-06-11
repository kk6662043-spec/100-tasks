# Freelance Invoice Generator

print("=== Freelance Invoice Generator ===")

freelancer = input("Freelancer Name: ")
client = input("Client Name: ")
service = input("Service Provided: ")

hours = float(input("Hours Worked: "))
rate = float(input("Rate Per Hour (₹): "))

total = hours * rate

print("\n========== INVOICE ==========")
print("Freelancer :", freelancer)
print("Client     :", client)
print("Service    :", service)
print("Hours      :", hours)
print("Rate       : ₹", rate)
print("-----------------------------")
print("Total Due  : ₹", total)
print("=============================")