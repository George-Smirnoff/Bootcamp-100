import turtle


def main():
    # circle(50)
    print(turtle.position())
    turtle.dot(20, "blue")
    # turtle.forward(100)
    turtle.setx(50)
    # turtle.heading()
    # turtle.home()
    print(turtle.position())

    # turtle.dot(80, "red")
    my_screen = turtle.Screen()
    my_screen.exitonclick()



if __name__ == '__main__':
    main()


