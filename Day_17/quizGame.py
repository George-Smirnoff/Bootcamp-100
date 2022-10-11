from questionModel import Question
from questionData import question_data
from quizBrain import QuizBrain


def main():
    # conclusion: any dictionary can be represented as class object
    question_bank = []
    for data in question_data:
        question_bank.append(
            Question(data["text"], data["answer"])
        )

    quiz = QuizBrain(q_list=question_bank)
    while quiz.still_has_question():
        quiz.next_question()

    # You can create a method in class or retrieve the arguments from class
    #1 quiz.final_results()
    print(f"You have completed quiz game. Your final score is: {quiz.score}/{quiz.question_number}")

if __name__ == '__main__':
    main()