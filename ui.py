from tkinter import * 
THEME_COLOR = "#375362"

false = "./images/false.png"
true = "./images/true.png"

class Quiz_Ui:
    
    def __init__(self) -> None:
        self.window = Tk()
        self.window.config(background=THEME_COLOR, pady=20)
        # self.window.geometry("300x500")

        self.score = 0
        self.score_label = Label(text=f"score:{self.score}", fg="white" ,font = ('Arial', 14, "normal"), bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(master=self.window, width=300, height = 250, highlightthickness=0)
        self.canvas.grid(row=1, column=0, padx=20, pady=20, columnspan=2)
        
        self.true_img = PhotoImage(file=true)
        self.true_btn = Button(image=self.true_img, highlightthickness=0, border=0)
        self.true_btn.grid(row=2, column=0)

        self.false_img = PhotoImage(file=false)
        self.false_btn = Button(image=self.false_img, highlightthickness=0, border=0)
        self.false_btn.grid(row=2, column=1)

        self.window.mainloop()
        


