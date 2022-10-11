class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def to_bool(self, answer):
        return answer.lower() in ['true', '1', 't', 'y', 'yes']

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q{self.question_number}: {current_question.text} True/False? ")
        # Conclusion: Doesn't make sense to put all text and answer if we use only one current_question.answer
        self.check_the_answer(guess, current_question.answer)

    def check_the_answer(self, guess, answer):
        answer = self.to_bool(answer)
        if self.to_bool(guess) == answer:
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong...")
        print(f"The correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

    def final_results(self):
        print(f"You have completed quiz game. Your final score is: {self.score}/{self.question_number}")





