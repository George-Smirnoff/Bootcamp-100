import turtle


def main():
    print(turtle.position())
    for i in range(4):
        turtle.right(90)
        turtle.forward(100)
    # turtle.dot(80, "red")
    my_screen = turtle.Screen()
    my_screen.exitonclick()



if __name__ == '__main__':
    main()


