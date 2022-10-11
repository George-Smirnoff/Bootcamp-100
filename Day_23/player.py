from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.color("Black")
        self.up()
        self.goto(0, -280)
        self.setheading(90)
        self.time_coef = 0.1
        self.weight = 10

    def move(self):
        self.forward(20)

    def new_level(self):
        self.goto(0, -280)
        self.weight += 5
        self.time_coef *= 0.9



