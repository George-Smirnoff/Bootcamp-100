import turtle
import random


# class my_turtle():
#     def __init__(self, color, xposition, yposition):
#         self.color = color
#         self.distance = 0
#         self.xposition = xposition
#         self.yposition = yposition

def main():
    start_game = False
    turtle.setup(width=500, height=400)
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    message = f"Which turtle will win the race, choose color:\n{colors}"
    user_bet = turtle.textinput(title='Make your bet', prompt=message)
    ypos = -90
    turtle_list = []

    for color in colors:
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.color(color)
        new_turtle.penup()
        new_turtle.goto(-230, ypos)
        ypos += 30
        turtle_list.append(new_turtle)


    if user_bet:
        start_game = True

    # Conclusion: It's possible to create multiple objects with a loop, and work with each object also using loop!
    # important to use correct refernces
    while start_game:
        for turt in turtle_list:
            if turt.xcor() > 230:
                start_game = False
                winning_color = turt.pencolor()
                print(winning_color)
                if winning_color == user_bet:
                    print(f"You won! The {winning_color} turtle is the winner!")
                else:
                    print(f"You lose! The {winning_color} turtle is the winner!")

            rand_distance = random.randint(0, 10)
            turt.forward(rand_distance)



    turtle.Screen().exitonclick()

if __name__ == '__main__':
    main()