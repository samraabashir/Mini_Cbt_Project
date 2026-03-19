
from datetime import datetime

class Question:
    def __init__(self, text, options, answer):
        self.text = text
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class QuizResult:
    def __init__(self, score):
        self.score = score
        self.timestamp = datetime.now()

    def get_result(self):
        return f'Score: {self.score} at {self.timestamp}'