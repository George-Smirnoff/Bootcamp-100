from questionModel import Question
from questionData import Questions
from quizBrain import QuizBrain
from quizUI import UI


def main():


    # conclusion: any dictionary can be represented as class object
    question_bank = []
    question_data = Questions().question_list()
    for data in question_data:
        question_bank.append(
            Question(data["text"], data["answer"])
        )

    quiz = QuizBrain(q_list=question_bank)
    appUI = UI(quiz)

if __name__ == '__main__':
    main()
