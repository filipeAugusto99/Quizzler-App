from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizzInterface:
    # Initialise attributes
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        # Create the window tk
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, bg=THEME_COLOR)

        # ScoreLabel
        self.score = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)

        # Create Canvas
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, columnspan=2, row=1, pady=40)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=280,
            text="Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        # Buttons
            # Right Button
        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.true_check)
        self.right_button.grid(column=0, row=2)

            # Wrong Button
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.false_check)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def true_check(self):
        self.give_feedback(is_right = self.quiz.check_answer("True"))


    def false_check(self):
        is_false = self.quiz.check_answer("False")
        self.give_feedback(is_false)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
