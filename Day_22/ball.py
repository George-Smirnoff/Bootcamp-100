from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("White")
        self.up()
        self.x_ext = 3
        self.y_ext = 3


    def start_position(self):
        self.goto(0, random.randint(-150, 150))
        self.bounce_x()

    def move(self):
        self.goto(self.pos() + (self.x_ext, self.y_ext))
        self.detect_wall_y()

    #2 def move(self):
    #2     nex_x = self.xcor() + self.x_ext
    #2     nex_y = self.ycor() + self.y_ext
    #2     self.goto(nex_x, nex_y)

    def detect_wall_y(self):
        ycor = self.ycor()
        if ycor > 280 or ycor < -280:
            self.y_ext *= -1

    def bounce_x(self):
        self.x_ext *= -1

    #2 def bounce_y(self):
    #2     self.y_ext *= -1
    #2
    #2 def bounce_x(self):
    #2     self.x_ext *= -1



