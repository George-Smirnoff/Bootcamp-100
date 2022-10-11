from turtle import Turtle, Screen
import random

COLORS = ["red", "yellow", "blue", "green", "purple"]
START_X = 290

class Block(Turtle):
    # Improve: Create a separate function ot create a block
    # Use empty list for init method blocks = []
    def __init__(self):
        super(Block, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.up()
        self.setheading(180)
        self.move()
        self.start_setup()

    # Improve: We can move all moving functionality to this method
    def move(self):
        self.forward(10)
    #     if self.xcor() > -300:
    #         self.forward(10)
    #     else:
    #         self.start_setup()

    def start_setup(self):
        self.color(random.choice(COLORS))
        self.goto(x=START_X, y=random.randrange(-250, 280, 10))

