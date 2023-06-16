from tkinter import * 
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

false = "./images/false.png"
true = "./images/true.png"
questions = None

class Quiz_Ui:
    
    def __init__(self, quizbrain:QuizBrain) -> None:
        self.quiz = quizbrain
        self.window = Tk()
        self.window.config(background=THEME_COLOR, pady=20)
        self.is_true = None
        # self.window.geometry("300x500")

        self.score = 0
        self.score_label = Label(text=f"score:{self.score}", fg="white" ,font = ('Arial', 14, "normal"), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(master=self.window, width=300, height = 250, highlightthickness=0, background="white")
        self.canvas.grid(row=1, column=0, padx=20, pady=50, columnspan=2)
        self.question_label = self.canvas.create_text(150, 125, width= 280, text="lorem ipsum", font=("Arial", 20, "italic"), fill=THEME_COLOR)
        
        true_img = PhotoImage(file=true)
        self.true_btn = Button(image=true_img, highlightthickness=0, border=0, command=self.check_true)
        self.true_btn.grid(row=2, column=0)

        false_img = PhotoImage(file=false)
        self.false_btn = Button(image=false_img, highlightthickness=0, border=0, command=self.check_false)
        self.false_btn.grid(row=2, column=1)

        self.get_nxt_qstn()

        self.window.mainloop()
        
    def get_nxt_qstn(self):
        try:
            global questions
            questions = self.quiz.next_question()
            self.canvas.itemconfig(self.question_label, text=questions)
        except IndexError:
            self.canvas.itemconfig(self.question_label, 
                                   text=f"You've completed the quiz.\n your final score was {self.quiz.score}/{self.quiz.question_number}")

    
    def reset_canvas(self):
        self.canvas.config(background="white")


    def check_true(self):
        self.is_true = "true"
        check = self.quiz.check_answer(self.is_true)
        if check == True:
            self.canvas.config(background="green")
            reset = self.window.after(3000, func=self.reset_canvas)
            self.window.after(3000, func=self.get_nxt_qstn)
        else:
            self.canvas.config(background="red")
            reset = self.window.after(3000, func=self.reset_canvas)
            self.window.after(3000, func=self.get_nxt_qstn)

    def check_false(self):
        self.is_true = "false"
        check = self.quiz.check_answer(self.is_true)
        if check == True:
            self.canvas.config(background="green")
            reset = self.window.after(3000, func=self.reset_canvas)
            self.window.after(3000, func=self.get_nxt_qstn)
        else:
            self.canvas.config(background="red")
            reset = self.window.after(3000, func=self.reset_canvas)
            self.window.after(3000, func=self.get_nxt_qstn)
        
        


