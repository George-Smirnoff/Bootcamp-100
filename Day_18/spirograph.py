import math_figures
import turtle as t

def main():
    t.speed(0)
    for angle in range(1, 360, 10):
        t.seth(angle)
        t.color(math_figures.randomColor())
        t.circle(100)


    t.Screen().exitonclick()


if __name__ == '__main__':
    main()