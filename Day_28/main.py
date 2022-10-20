import time
from tkinter import *
from PIL import ImageTk, Image
import datetime

# ------------------------ CONSTANTS ------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1500
SHORT_BREAK_MIN = 300
LONG_BREAK_MIN = 1200
REPS = 0
TIMER = None

# ------------------------ TIMER RESET ------------------------
def reset_timer():
    global REPS, TIMER

    window.after_cancel(TIMER)
    REPS = 0
    canvas.itemconfig(timer, text="00:00")
    timer_text.config(text="Timer", fg=GREEN)
    check_icon.config(text="")

# ------------------------ TIMER MECHANISM ------------------------
def start_timer():
    global REPS
    REPS += 1
    check_icon.config(text="")

    if REPS % 7 == 0:
        countdown(LONG_BREAK_MIN)
        timer_text.config(text="Long Break!", fg=PINK)
    elif REPS % 2 != 0:
        countdown(WORK_MIN)
        timer_text.config(text="WORK", fg=GREEN)
    elif REPS % 2 == 0:
        countdown(SHORT_BREAK_MIN)
        timer_text.config(text="Break", fg=RED)





# ------------------------ COUNTDOWN MECHANISM ------------------------
def countdown(count):
    global REPS, TIMER
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer, text=f"{minutes}:{seconds:02d}")
    # canvas.itemconfig(timer, text=f"{datetime.timedelta(seconds=count)}")
    if count > 0:
        TIMER = window.after(1000, countdown, count - 1)
    elif REPS % 2 != 0:
        check_icon.config(text="✓")

# ------------------------ UI SETUP ------------------------
window = Tk()
window.title('Pomodoro')
window.minsize(width=600, height=600)
window.config(padx=20, pady=20, background=YELLOW)


# Image
canvas = Canvas(width=450, height=450, bg=YELLOW, highlightthickness=0)
img = ImageTk.PhotoImage(Image.open("tomato.jpg"))
canvas.create_image(225, 225, image=img)
timer = canvas.create_text(225, 270, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

# Buttons
start_button = Button(text='Start', command=start_timer)
start_button.grid(row=3, column=1)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(row=3, column=3)


# Labels
timer_text = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, "bold"))
timer_text.grid(row=1, column=2)

check_icon = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, "bold"))
check_icon.grid(row=3, column=2)


window.mainloop()