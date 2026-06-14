# Simple AI-Based Code Generator

def generate_code(prompt):
    prompt = prompt.lower()

    if "calculator" in prompt:
        return """
def add(a, b):
    return a + b

print("Result:", add(10, 20))
"""

    elif "hello world" in prompt:
        return """
print("Hello, World!")
"""

    elif "for loop" in prompt:
        return """
for i in range(5):
    print(i)
"""

    else:
        return "# Sorry, no code template available."

# User Input
user_prompt = input("Enter your coding request: ")

# Generate Code
generated_code = generate_code(user_prompt)

print("\\nGenerated Code:")
print(generated_code)