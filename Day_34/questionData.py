import requests
import html

# question_data = [
#     {"text": "A slug's blood is green.", "answer": "True"},
#     {"text": "The loudest animal is the Africa Elephant.", "answer": "False"},
#     {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"},
#     {"text": "Is Tartu the capital of Estonia.", "answer": "False"},
#     {"text": "Ping-Pong originated in England", "answer": "False"},
# ]

# TODO: Retrieve token for session
# TODO: Choose the difficulty


# https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean
class Questions:
    def __init__(self):
        self.url = 'https://opentdb.com/api.php'
        self.number = 10
        self.type = 'boolean'
        self.questions = []
        # self.difficulty = medium


    def question_request(self):
        questions_request = requests.get(url=self.url, params=self.question_params())
        questions_request.raise_for_status()
        questions_data = questions_request.json()
        return questions_data

    def question_params(self):
        question_params = {
            "amount": str(self.number),
            "type": self.type
        }
        return question_params

    def question_list(self):
        questions_data = self.question_request()
        for question in questions_data['results']:

            structure = {
                "text": html.unescape(question['question']),
                "answer": question['correct_answer']
            }
            self.questions.append(structure)
        return self.questions
