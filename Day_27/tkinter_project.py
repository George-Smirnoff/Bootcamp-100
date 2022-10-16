from tkinter import *

def button_action(label, input):
    print(input.get())
    # label.config(text=input.get())


def main():
    window = Tk()
    window.minsize(width=400, height=400)
    window.title("Tkinter window")
    window.config(padx=100, pady=100)


    # Label
    my_label = Label(text="The Label!", font=("Arial", 24, "bold"))
    # my_label.pack()
    my_label.grid(row=0, column=0)
    my_label.config(padx=50, pady=50)

    # Input
    input = Entry(width=10)
    # input.pack()
    input.grid(row=3, column=4)

    # Button
    button = Button(text='Click me', command=lambda: button_action(my_label, input))
    # button.pack()
    button.grid(row=2, column=2)
    button.config(padx=40, pady=30)

    # New Button
    button = Button(text='Next', command=lambda: button_action(my_label, input))
    # button.pack()
    button.grid(row=1, column=3)



    window.mainloop()

if __name__ == '__main__':
    main()