import turtle
import random


class Food(turtle.Turtle):
    def __init__(self, ):
        super().__init__()
        self.shape("circle")
        self.up()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("Green")
        self.update()

    def update(self):
        x_cor = random.randrange(-280, 280, 20)
        y_cor = random.randrange(-280, 280, 20)
        # self.up() # to request it once
        self.goto(x_cor, y_cor)
