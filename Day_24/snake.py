from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #1 def create_segmemt(self, position):
    #1     new_segment = Turtle(shape="square")
    #1     new_segment.color("White")
    #1     new_segment.penup()
    #1     new_segment.goto(position)
    #1     return new_segment
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("White")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)


    # Conslusion: You can use a function in class declaration to create a class object with another class object usage
    def create_snake(self):
        for position in STARTING_POSITION:
            # Megred the lines above in one function add_segment
            #1 new_segment = self.create_segmemt(position)
            #1 self.segments.append(new_segment)
            self.add_segment(position)

    def move(self):
        # Move last segmeent on place the segment in front
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        # move first segment forward
        self.head.forward(MOVE_DISTANCE)

    #1 def growth(self):
    #1     last_element_cor = self.segments[len(self.segments) - 1].position()
    #1     new_segment = self.create_segmemt(last_element_cor)
    #1     self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Conclusion: sometimes it makes sense to find another way
    #1 def self_eating(self):
    #1   for segment in range(1, len(self.segments)):
    #1       if self.head.position() == self.segments[segment].position():
    #1           scoreboard.Scoreboard().game_over()


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)