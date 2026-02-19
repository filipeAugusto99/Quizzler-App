from tkinter import *


THEME_COLOR = "#375362"


class QuizzInterface:
    # Initialise attributes
    def __init__(self):

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
            text="Question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )

        # Buttons
            # Right Button
        self.right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0)
        self.right_button.grid(column=0, row=2)

            # Wrong Button
        self.wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        self.window.mainloop()




