import random

def generate_question():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(operations)

    if operation == '/':
        num1 = num1 * num2  # Ensure that num1 is divisible by num2

    question = f"{num1} {operation} {num2}"
    answer = eval(question)

    return question, answer

def main():
    score = 0
    for _ in range(5):
        question, answer = generate_question()
        print(f"What is {question}?")
        user_answer = float(input("Your answer: "))

        if user_answer == answer:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong. The correct answer is {answer}")

    print(f"Your final score is {score} out of 5")

if __name__ == "__main__":
    main()
