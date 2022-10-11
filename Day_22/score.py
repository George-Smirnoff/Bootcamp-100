from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 40, 'normal')

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_left = 0
        self.score_right = 0
        self.ht()
        self.goto(0, 250)
        self.color("Yellow")
        self.write(arg=f"{self.score_left} : {self.score_right}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.write(arg=f"{self.score_left} : {self.score_right}", align=ALIGNMENT, font=FONT)