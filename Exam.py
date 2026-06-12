# Online Examination System

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Chennai", "B. Mumbai", "C. New Delhi", "D. Kolkata"],
        "answer": "C"
    },
    {
        "question": "Which language is used for Python development?",
        "options": ["A. Python", "B. Java", "C. C++", "D. HTML"],
        "answer": "A"
    },
    {
        "question": "2 + 3 = ?",
        "options": ["A. 4", "B. 5", "C. 6", "D. 7"],
        "answer": "B"
    }
]

score = 0

print("===== Online Examination System =====")

name = input("Enter Student Name: ")

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        score += 1

print("\n===== Exam Result =====")
print("Student Name:", name)
print("Total Questions:", len(questions))
print("Correct Answers:", score)
print("Wrong Answers:", len(questions) - score)
print("Score:", score, "/", len(questions))

percentage = (score / len(questions)) * 100
print("Percentage:", percentage, "%")