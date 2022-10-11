import turtle as t


def move_forward():
    t.forward(10)

def move_back():
    t.backward(10)

def move_right():
    t.right(10)

def move_left():
    t.left(10)

def clear():
    t.clear()
    t.up()
    t.home()
    t.down()

def main():
    t.listen()
    t.onkeypress(move_forward, "w")
    t.onkeypress(move_back, "s")
    t.onkeypress(move_right, "d")
    t.onkeypress(move_left, "a")
    t.onkeypress(clear, "c")


    t.Screen().exitonclick()

if __name__ == '__main__':
    main()