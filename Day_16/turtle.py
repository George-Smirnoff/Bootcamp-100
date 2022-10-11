from turtle import Turtle, Screen


def main():
    Timmy = Turtle()
    print(Timmy)
    Timmy.shape("turtle")
    Timmy.color("green")
    Timmy.forward(100)
    Timmy.left(40)
    Timmy.forward(100)



    my_screen = Screen()
    my_screen.exitonclick()



if __name__ == '__main__':
    main()


