class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

class Quiz:
    def __init__(self):
        self.questions = []

    def add_question(self, prompt, answer):
        self.questions.append(Question(prompt, answer))

    def run(self):
        score = 0
        for question in self.questions:
            user_answer = input(question.prompt + " ")
            if user_answer.lower() == question.answer.lower():
                score += 1
        print(f"Your score: {score}/{len(self.questions)}")

def main():
    quiz = Quiz()
    quiz.add_question("What is the capital of France?", "Paris")
    quiz.add_question("What is 2 + 2?", "4")
    quiz.add_question("What color do you get by mixing red and white?", "Pink")
    quiz.run()

if __name__ == "__main__":
    main()
