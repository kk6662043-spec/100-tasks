# Simple Quiz Application

score = 0

print("Welcome to the Quiz!\n")

# Question 1
print("1. What is the capital of India?")
answer = input("Your answer: ")
if answer.lower() == "delhi":
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

# Question 2
print("2. What is 5 + 3?")
answer = input("Your answer: ")
if answer == "8":
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

# Question 3
print("3. What color is the sky?")
answer = input("Your answer: ")
if answer.lower() == "blue":
    print("Correct!\n")
    score += 1
else:
    print("Wrong!\n")

print("Your final score is:", score, "/3")