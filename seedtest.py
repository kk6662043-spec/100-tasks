import time

# Sentence to type
sentence = "Python is a powerful programming language"

print("Typing Speed Test")
print("-" * 30)
print("Type the following sentence:")
print(sentence)

input("\nPress Enter when you're ready...")

# Start timer
start_time = time.time()

# User input
typed_text = input("\nStart typing: ")

# End timer
end_time = time.time()

# Calculate time taken
time_taken = end_time - start_time

# Calculate WPM
word_count = len(typed_text.split())
wpm = (word_count / time_taken) * 60

# Check accuracy
accuracy = 100 if typed_text == sentence else (
    sum(1 for a, b in zip(typed_text, sentence) if a == b)
    / len(sentence)
    * 100
)

print("\nResults")
print("-" * 30)
print(f"Time Taken: {time_taken:.2f} seconds")
print(f"Typing Speed: {wpm:.2f} WPM")
print(f"Accuracy: {accuracy:.2f}%")