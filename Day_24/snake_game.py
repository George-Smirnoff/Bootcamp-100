from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from scorerecord import Scorerecord
import time

def main():
    screen = Screen()
    screen.bgcolor("Black")
    screen.setup(width=600, height=600)
    screen.title("Snake game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()
    record = Scorerecord()

    screen.listen()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")
    # turtle = Turtle(shape='square')
    # turtle.color("white")
    # turtle.resizemode("user")
    # turtle.shapesize(stretch_wid=1, stretch_len=3)
    # turtle.penup()

    game_in = True
    while game_in:
        #1 snake.self_eating()

        # display current segments state
        time.sleep(0.1)
        screen.update()
        snake.move()


        if food.distance(snake.head) < 3:
            snake.extend()
            food.update()
            score.plus_one()

        # Self eating
        for segment in snake.segments[1:]:
            # if segment == snake.head:
            #     pass
             if snake.head.distance(segment) < 3:
                score.game_over()
                record.write_record(score.score, record.record)
                game_in = False

        # Cross the boarder
        if 300 < snake.head.ycor() or snake.head.ycor() < -300 or 300 < snake.head.xcor() or snake.head.ycor() < -300:
            score.game_over()
            record.write_record(score.score, record.record)
            game_in = False

    screen.exitonclick()

if __name__ == '__main__':
    main()