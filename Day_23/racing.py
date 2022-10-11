import random
from turtle import Screen
import time
import player
import scoreboard
import block


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("White")
    screen.tracer(0)

    game_player = player.Player()
    game_score = scoreboard.Scoreboard()

    # We can move random choise and blocks declaration to blocks class
    sampleList = (0, 1)
    blocks = []

    screen.listen()
    screen.onkey(game_player.move, "Up")

    game_in = True
    while game_in:
        time.sleep(game_player.time_coef)
        screen.update()

        # Create random blocks
        if 1 in random.choices(sampleList, weights=(100, game_player.weight), k=1):
            blocks.append(block.Block())

        # Move blocks with collision condition
        for game_block in blocks:

            if game_player.distance(game_block) < 18:
                # print(game_player.distance(game_block))
                game_in = False

            if game_block.xcor() > -300:
                game_block.forward(10)
            else:
                blocks.remove(game_block)
            game_block.move()

        if game_player.ycor() > 290:
            game_score.update_score()
            game_player.new_level()


    screen.exitonclick()

if __name__ == '__main__':
    main()