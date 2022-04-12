from tkinter import *
from quiz_brain import QuizBrain
from playsound import playsound
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz App")

        self.window.config(padx = 100, pady = 50, bg=THEME_COLOR)
        self.window.geometry("600x600")
        self.window.resizable(width=False, height=False)

        self.score_label = Label(text = "Score: 0", fg= "wheat", bg=THEME_COLOR, font = ("Arial", 16))
        self.score_label.grid(row = 0, column = 0, columnspan = 2)


        self.canvas = Canvas(width = 400, height = 200, bg = "wheat")
        self.question_text = self.canvas.create_text(200, 100, text = "Some questions text....", font = ("Arial", 20), fill = THEME_COLOR, width= 350 )
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady=50)


        true_image = PhotoImage(file="images/true.png")
        false_image = PhotoImage(file="images/false.png")

        self.true_button = Button(image = true_image,  highlightthickness=1, command = self.true_pressed)
        self.false_button = Button(image = false_image, highlightthickness=1, command = self.false_pressed)

        self.true_button.grid(row = 2, column = 1)
        self.false_button.grid(row = 2, column = 0)
       

        self.get_next_question()
        self.window.mainloop()
 

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg = "wheat")
            self.score_label.config(text = "Score: " + str(self.quiz.score) + "/" + str(self.quiz.question_number))
            q_text= self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text = q_text)
        else:
            self.canvas.config(bg = "yellow")
            self.canvas.itemconfig(self.question_text, text = "You've completed the quiz")
            self.score_label.config(text = "Score: " + str(self.quiz.score) + "/" + str(self.quiz.question_number))
            self.true_button.config(state = DISABLED)
            self.false_button.config(state = DISABLED)

    def true_pressed(self):
        is_right= self.quiz.check_answer("True")
        self.give_feedback(is_right)
    

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            playsound('audio/true.wav')
            self.canvas.config(bg="green")
           
        else:
            playsound('audio/false.wav')
            self.canvas.config(bg = "red")
         
        self.window.after(1000, self.get_next_question)