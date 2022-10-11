from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.up()
        self.goto(-160, 260)
        self.color("Black")
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)
