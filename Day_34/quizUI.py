from tkinter import *
import quizBrain
import time


class UI:
    # Note: Interesting case how to assign two classes as class variables
    # Where one class working as class parameter
    def __init__(self, quiz_brain: quizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.color = '#375362'
        self.window.title('Quizzler')
        self.window.geometry('350x500')
        self.window.config(padx=20, pady=20, bg=self.color)

        self.font = ('Arial', 20, 'italic')
        self.button_font = ('Arial', 30, 'italic')
        self.score_text = Label(self.window, text='Score: 0', bg=self.color, fg='white')
        self.score_text.grid(row=0, column=1, padx=20, pady=20)

        # Question display
        self.canvas = Canvas(width=300, height=250, bg='White')
        self.question_text = self.canvas.create_text(150, 125, text="Press any button to start the game!", width=280,  fill=self.color)
        self.canvas.grid(row=2, column=0, columnspan=2)

        # Buttons
        self.true_button = Button(text='✔', fg='green', highlightbackground=self.color, font=self.button_font, command=lambda: self.check_button(button='True'))
        self.true_button.grid(row=3, column=0, padx=40, pady=40)

        self.false_button = Button(text='✘', fg='red', highlightbackground=self.color, font=self.button_font, command=lambda: self.check_button(button='False'))
        self.false_button.grid(row=3, column=1, padx=40, pady=40)

        self.update_question()

        self.window.mainloop()

    def update_question(self):
        self.canvas.configure(self.canvas, bg='White')
        if self.quiz.still_has_question():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="End of Quiz!")
            #1 self.true_button["state"] = "disabled"
            #1 self.false_button["state"] = "disabled"
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def check_button(self, button: str):
        self.quiz.answer = self.quiz.check_the_answer(button)
        self.give_feedback()

    def give_feedback(self):
        if self.quiz.answer:
            self.canvas.config(bg='Green')
        else:
            self.canvas.config(bg='Red')
        self.window.after(500, self.update_question)





