from turtle import Screen
import paddle
import ball
import score

def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("Black")
    screen.title("Pong")
    screen.tracer(0)

    l_paddle = paddle.Paddle(xcor=-350)
    r_paddle = paddle.Paddle(xcor=350)
    game_ball = ball.Ball()
    game_score = score.Score()

    screen = Screen()
    screen.listen()
    screen.onkey(r_paddle.move_up, "Up")
    screen.onkey(r_paddle.move_down, "Down")
    screen.onkey(l_paddle.move_up, "w")
    screen.onkey(l_paddle.move_down, "s")
    # self = Turtle()

    # self.goto(xcor, ycor)

    game_on = True
    while game_on:
        screen.update()
        game_ball.move()

        # Detect paddles
        xcor = game_ball.xcor()
        if xcor > 360:
            game_score.score_left += 1
            game_score.update_score()
            game_ball.start_position()
        elif xcor < -360:
            game_score.score_right += 1
            game_score.update_score()
            game_ball.start_position()
        elif (xcor > 340 and game_ball.distance(r_paddle) < 55) or (xcor < -340 and game_ball.distance(l_paddle) < 55):
                game_ball.bounce_x()


        #2 # Detect y-wall
        #2 ycor = game_ball.ycor()
        #2 if ycor > 280 or ycor < -280:
        #2     game_ball.bounce_y()
        #2
        #2 # Detect paddles
        #2 xcor = game_ball.xcor()
        #2 if (xcor > 340 and game_ball.distance(r_paddle) < 55) or (xcor < -340 and game_ball.distance(l_paddle) < 55):
        #2     game_ball.bounce_x()


    screen.exitonclick()

if __name__ == '__main__':
    main()