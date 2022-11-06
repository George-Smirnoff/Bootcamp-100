class QuizBrain:
    def __init__(self, q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0
        self.current_question = None
        self.answer = None


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def to_bool(self, answer) -> bool:
        return answer.lower() in ['true', '1', 't', 'y', 'yes']

    def next_question(self) -> str:
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q{self.question_number}: {self.current_question.text}"

    def check_the_answer(self, guess):
        answer = self.current_question.answer
        if self.to_bool(guess) == self.to_bool(answer):
            self.score += 1
            return True
        else:
            return False

    def final_results(self):
        print(f"You have completed quiz game. Your final score is: {self.score}/{self.question_number}")





