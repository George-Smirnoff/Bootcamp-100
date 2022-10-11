from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, xcor=0, ycor=0):
        super().__init__()
        self.up()
        self.goto(xcor, ycor)
        self.shape('square')
        self.setheading(270)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("White")

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y > 260:
            pass
        else:
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y < -250:
            pass
        else:
            self.goto(x=self.xcor(), y=new_y)


