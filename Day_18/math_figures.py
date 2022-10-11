import turtle as t
import random


def randomColor():
    t.Screen().colormode(255)
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def main():

    for times in range(3, 10):
        t.pencolor(randomColor())
        angel = 360/times
        for _ in range(times):
            t.right(angel)
            t.forward(50)




    t.Screen().exitonclick()

if __name__ == '__main__':
    main()


