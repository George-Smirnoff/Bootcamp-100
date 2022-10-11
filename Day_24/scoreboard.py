from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.goto(-100, 270)
        self.color("Yellow")
        # Conclusion: Don't try to bring the complexity from scratch
        # Move FONT to global var
        #1 self.write(arg=f"Score: {self.score}", align="center", font=('Arial', 20, 'normal'))
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def plus_one(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.up()
        self.goto(0, 0)
        self.color("Red")
        self.write(arg=f"GAME OVER!", align=ALIGNMENT, font=('Arial', 40, 'normal'))
