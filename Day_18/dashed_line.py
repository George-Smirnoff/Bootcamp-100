import turtle as t

def main():
    for i in range(40):
        t.forward(10)
        if i%2 == 0:
            t.up()
        else:
            t.down()



    screen = t.Screen()
    screen.exitonclick()


if __name__ == '__main__':
    main()