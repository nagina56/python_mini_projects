print("Welcome to Quiz App!")

questions = [
    {
        "question": "Q1. What is the capital of Pakistan?",
        "options": ["A) Karachi", "B) Islamabad", "C) Lahore", "D) Peshawar"],
        "answer": "b"
    },
    {
        "question": "Q2. Which one is a programming language?",
        "options": ["A) Python", "B) Snake", "C) Tiger", "D) Lion"],
        "answer": "a"
    }
    # {
    #     "question": "Q3. What is 2 + 2?",
    #     "options": ["A) 3", "B) 4", "C) 5", "D) 6"],
    #     "answer": "b"
    # }
]

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").lower()

    if user_answer == q["answer"]:
        print("Correct! 🎉")
        score += 1
    else:
        print("Wrong ❌")

print("\nQuiz Finished")
print("Your Score:", score, "/", len(questions))
print("Thank you for playing!")