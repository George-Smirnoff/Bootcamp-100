from tkinter import *
import requests


def get_comment():
    URL = 'https://api.kanye.rest'
    # sending get request and saving the response as response object
    request = requests.get(url=URL)

    # extracting data in json format
    data = request.json()

    # extracting message from json
    comment = data.get('quote')

    # update the quote_text with a new comment
    canvas.itemconfig(quote_text, text=comment)



window = Tk()
window.title("Mem-Man saying...")
window.config(padx=50 ,pady=50)

canvas = Canvas(width=200, height=200)
quote_text = canvas.create_text(100, 100, text="Hello, Bro!!!", width=150, font=("Courier", 16, "bold"))
canvas.grid(row=0, column=0)

# Create Button with man Image
man_image = PhotoImage(file='laughing_man.png')
man_button = Button(image=man_image, highlightthickness=0, command=get_comment)
man_button.grid(row=0, column=1)

window.mainloop()