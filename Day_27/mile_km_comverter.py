from tkinter import *

def convert(miles):
    kms = float(miles.get()) * 1.609344
    result = Label(text=round(kms, 3), anchor='n')
    result.grid(row=2, column=2)

def main():
    window = Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=200, height=120)
    window.config(padx=20, pady=20)

    # Input
    mile_input = Entry()
    mile_input.config(width=10)
    mile_input.grid(row=1, column=2)


    # Labels
    label_equal = Label(text="is equal to")
    label_equal.grid(row=2, column=1)
    label_miles = Label(text="Miles")
    label_miles.grid(row=1, column=3)
    label_km = Label(text="Km")
    label_km.grid(row=2, column=3)


    # Button
    convert_button = Button(text='Convert', command=lambda: convert(mile_input))
    convert_button.grid(row=3, column=2)



    window.mainloop()


if __name__ == '__main__':
    main()