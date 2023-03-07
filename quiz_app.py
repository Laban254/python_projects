questions = [
    {
        "question": "What is the capital of France?",
        "answer": "Paris"
    },
    {
        "question": "What is the highest mountain in the world?",
        "answer": "Mount Everest"
    },
    {
        "question": "What is the largest country by area?",
        "answer": "Russia"
    },
    {
        "question": "What is the currency of Japan?",
        "answer": "Yen"
    },
    {
        "question": "Who is the founder of Microsoft?",
        "answer": "Bill Gates"
    },
    {
        "question": "What is the name of the largest ocean?",
        "answer": "Pacific Ocean"
    },
    {
        "question": "What is the smallest planet in our solar system?",
        "answer": "Mercury"
    },
    {
        "question": "Who wrote the novel 'To Kill a Mockingbird'?",
        "answer": "Harper Lee"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "answer": "Au"
    },
    {
        "question": "Who is the current president of the United States?",
        "answer": "Joe Biden"
    }
]

score = 0

for q in questions:
    print(q["question"])
    user_answer = input("Your answer: ")
    if user_answer.lower() == q["answer"].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {q['answer']}.")

print(f"You scored {score}/{len(questions)}")
