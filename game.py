import random

secret = random.randint(1, 10)

guess = int(input("Guess a number (1 to 10): "))

if guess == secret:
    print("Correct! You win 🎉")
else:
    print("Wrong! The number was", secret)