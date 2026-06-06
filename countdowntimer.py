import time

# Set countdown time in seconds
seconds = 10

while seconds > 0:
    print(f"Time left: {seconds} seconds")
    time.sleep(1)
    seconds -= 1

print("Time's up!")