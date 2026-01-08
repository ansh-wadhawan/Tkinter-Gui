import tkinter as tk
from tkinter import ttk
import random
from QuestionConstructor import questions_constructor
from PIL import Image,ImageTk
import ask_the_audience

i = True

class app():
    def __init__(self):

        self.fullscreen = True

        self.level = 1

        self.level1 = 1

        self.survived = 0
        
        self.win = tk.Tk()
        self.win.attributes("-fullscreen",False)
        self.win.geometry("1350x700")
        self.win.bind("<Escape>",self.toggle_fullscreen)
        self.win.configure(background="light blue")

        self.QC = questions_constructor
        
        self.Ques = self.QC.generate(self.level)

        self.Failed = True

        self.style = ttk.Style()
        self.style.configure("My.TFrame",background="blue")
        
        self.content = ttk.Frame(self.win,style="My.TFrame")
        self.content.place(x=0,y=0)

        self.title_lable = tk.Label(width=30,bd=15,height=2,text="QUIZ",font=("times new roman",22,'bold'),relief='raised',fg='gold',bg="dark blue")
        self.title_lable.place(x=475, y=100)

        self.question_label = tk.Label(width=50,bd=15,height=4,text=self.Ques.text,font=("times new roman",18,'bold'),relief='raised',fg='gold',bg="dark blue")
        self.question_label.place(x=400, y=250)

        self.optionA = tk.Button(width=30,bd=10,height=2,text=self.Ques.options[0],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self.button1)
        if self.survived == 0:
            self.optionA.place(x=350,y=500)
        
        self.optionB = tk.Button(width=30,bd=10,height=2,text=self.Ques.options[1],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self.button2)
        if self.survived == 0:
            self.optionB.place(x=750, y=500)

        self.optionC = tk.Button(width=30,bd=10,height=2,text=self.Ques.options[2],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self.button3)
        if self.survived == 0:
            self.optionC.place(x=350,y=600)
        
        self.optionD = tk.Button(width=30,bd=10,height=2,text=self.Ques.options[3],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self.button4)
        if self.survived == 0:
            self.optionD.place(x=750, y=600)


        self.LIFELINES = tk.Label(bd=10,height=2,text="LIFELINES",font=("times new roman",22,'bold'),relief='raised',fg='gold',bg="dark blue")
        self.LIFELINES.place(x=50,y=75)

        self.E = tk.Button(text="EXPERT'S ADVICE",fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self.EXPERT_ADVICE,bd=10)
        if self.survived == 0:
            self.E.place(x=50,y=200)
            
        self.P = tk.Button(text="PHONE A FRIEND",fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self.Phone_a_friend,bd=10)
        if self.survived == 0:
            self.P.place(x=50,y=300)

        self.A = tk.Button(text="ASK THE AUDIENCE",fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self.ASK_THE_AUDIENCE,bd=10)
        if self.survived == 0:
            self.A.place(x=50,y=400)
        
        self.F = tk.Button(text="FIFTY FIFTY",fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=self._5050,bd=10)
        if self.survived == 0:
            self.F.place(x=50,y=500)

        self.used_E = False
        self.used_P = False
        self.used_A = False
        self.used_F = False

        self.bottom_label = 0

        self.survived_Label = 0

        self.survived_Button = 0

        self.winning_Label = 0

        self.winning_Label1 = 0

        self.winning_Button = 0

        self.Failed_Label = 0

        self.get_back_up = True

        self.Failed_Button = 0

    def toggle_fullscreen(self,keypress):
        if self.fullscreen:
            self.fullscreen = False
        else:
            self.fullscreen = True
        self.win.attributes("-fullscreen",self.fullscreen)
        
    def button1(self):
        if self.Ques != 0:
            if self.Ques.correct_ans == self.Ques.options[0]:
                self.survived = True
            else:
                self.Failed = False
                
    def button2(self):
        if self.Ques != 0: 
            if self.Ques.correct_ans == self.Ques.options[1]:
                self.survived = True
            else:
                self.Failed = False

             

    def button3(self):
        if self.Ques != 0: 
            if self.Ques.correct_ans == self.Ques.options[2]:
                self.survived = True
            else:
                self.Failed = False
             

    def button4(self):
        if self.Ques != 0:
            if self.Ques.correct_ans == self.Ques.options[3]:
                self.survived = True
            else:
                self.Failed = False

    def Phone_a_friend(self):
        self.used_P = True
        list1 = [True,False]
        chance = random.choice(list1)

        if chance:
            self.bottom_label = tk.Label(width=65,bd=10,height=2,text="FRIEND'S'S ADVICE: " + self.Ques.correct_ans,font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")
            self.bottom_label.place(x=350,y=690)
        else:
            fake_answer = self.Ques.correct_ans
            while fake_answer == self.Ques.correct_ans:
                fake_answer = random.choice(self.Ques.options)
            self.bottom_label = tk.Label(width=65,bd=10,height=2,text="FRIEND'S'S ADVICE: " + fake_answer,font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")
            self.bottom_label.place(x=350,y=690)
        
        self.P = tk.Button(text="PHONE A FRIEND",fg='gold',bg="dark grey",font=("times new roman",15,'bold'),command=self.button1,bd=10,state="disabled")
        self.P.place(x=50,y=300)
    def EXPERT_ADVICE(self):
        
        self.used_E = True
        
        list1 = [True,True,True,True,False]
        chance = random.choice(list1)

        if chance:
            self.bottom_label = tk.Label(width=65,bd=10,height=2,text="EXPERT'S ADVICE: " + self.Ques.correct_ans,font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")
            self.bottom_label.place(x=350,y=690)
        else:
            fake_answer = self.Ques.correct_ans
            while fake_answer == self.Ques.correct_ans:
                fake_answer = random.choice(self.Ques.options)
            self.bottom_label = tk.Label(width=65,bd=10,height=2,text="EXPERT'S ADVICE: " + fake_answer,font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")
            self.bottom_label.place(x=350,y=690)

        self.E = tk.Button(text="EXPERT'S ADVICE",fg='gold',bg="dark grey",font=("times new roman",15,'bold'),command=self.EXPERT_ADVICE,bd=10,state="disabled")
        self.E.place(x=50,y=200)
    def ASK_THE_AUDIENCE(self):

        self.A = tk.Button(text="ASK THE AUDIENCE",fg='gold',bg="dark grey",font=("times new roman",15,'bold'),command=self.ASK_THE_AUDIENCE,bd=10,state="disabled")
        self.A.place(x=50,y=400)
        
        self.used_A = True

        list2 = [0,0,0,0]

        list1 = [True,True,False]
        chance = random.choice(list1)

        if chance:

            for i in range(0,4):
                if not i == self.Ques.options.index(self.Ques.correct_ans):
                    list2[i] = 20
                else:
                    list2[i] = 60

            ask_the_audience.main([1,2,3,4],list2)

        else:
            list2 = [20,20,20,20]
            a = random.choice(range(0,4))

            list2[a] = 60
            
            ask_the_audience.main([1,2,3,4],list2)
        
    def _5050(self):

        list1 = [0,1,2,3]
        list1.remove(self.Ques.options.index(self.Ques.correct_ans))

        a = random.choice(list1)
        list1.remove(a)

        b = a

        while b == a:
            b = random.choice(list1)
            list1.remove(b)

        if a == 0 or b == 0:
            self.optionA.destroy()
        if a == 1 or b == 1:
            self.optionB.destroy()
        if a == 2 or b == 2:
            self.optionC.destroy()
        if a == 3 or b == 3:
            self.optionD.destroy()
        
        self.used_F = True
        self.F = tk.Button(text="FIFTY FIFTY",fg='gold',bg="dark grey",font=("times new roman",15,'bold'),command=self._5050,bd=10,state="disabled")
        self.F.place(x=50,y=500)

    def Continue(self):
        self.survived = 0
        self.level += 1
        self.Ques = self.QC.generate(self.level)

    def exit1(self):
        self.win.destroy()
        exit()

a = app()

while True:
    try:
        a.win.update()    
    except:
        break

    if a.survived:
        try:
            a.optionA.destroy()
            a.optionB.destroy()
            a.optionC.destroy()
            a.optionD.destroy()
            a.question_label.destroy()

            a.optionA = 0
            a.optionB = 0
            a.optionC = 0
            a.optionD = 0
            a.question_label = 0
            
            a.bottom_label.destroy()
            a.bottom_label = 0
        except:
            pass

        if a.survived_Label == 0 and a.survived_Button == 0:
            if a.level != 9:
                a.survived_Label = tk.Label(width=40,bd=15,height=4,text="CORRECT! YOU PROGRESS TO THE NEXT ROUND",font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")        
                a.survived_Label.place(x=425, y=300)

                a.survived_Button = tk.Button(width=30,bd=10,height=2,text="CONTINUE",fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=a.Continue)        
                a.survived_Button.place(x=475, y=500)
            else:
                if i:
                    a.winning_Label = tk.Label(width=50,bd=15,height=4,text="CONGRATULATIONS!",font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")        
                    a.winning_Label.place(x=425, y=300)

                    a.winning_Label1 = tk.Label(width=50,bd=15,height=4,text="YOU COMPLETED THE QUIZ",font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")        
                    a.winning_Label1.place(x=425, y=450)

                    a.winning_Button = tk.Button(width=30,bd=10,height=2,text="LEAVE",fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=a.exit1)        
                    a.winning_Button.place(x=475, y=600)
                    i = False

    if not a.Failed:
        a.get_back_up = False 
        try:
            a.optionA.destroy()
            a.optionB.destroy()
            a.optionC.destroy()
            a.optionD.destroy()
            a.question_label.destroy()

            a.optionA = 0
            a.optionB = 0
            a.optionC = 0
            a.optionD = 0
            a.question_label = 0

            a.bottom_label.destroy()
            a.bottom_label = 0
        except:
            pass

        if a.Failed_Label == 0 and a.Failed_Button == 0:

            a.Failed_Label = tk.Label(width=44,bd=15,height=4,text="I AM SORRY TO SAY BUT THAT ANSWER WAS WRONG",font=("times new roman",15,'bold'),relief='raised',fg='gold',bg="dark blue")        
            a.Failed_Label.place(x=425, y=300)

            a.Failed_Button = tk.Button(width=30,bd=10,height=2,text="LEAVE",fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=a.exit1)        
            a.Failed_Button.place(x=475, y=500)

    if a.survived == 0:
        try:
            a.survived_Label.destroy()
            a.survived_Button.destroy()

            a.survived_Label = 0
            a.survived_Button = 0
        except:
            pass

        if a.optionA == 0 and a.optionB == 0 and a.optionC == 0 and a.optionD == 0:
            if a.get_back_up:
                a.optionA = tk.Button(width=30,bd=10,height=2,text=a.Ques.options[0],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=a.button1)
                a.optionA.place(x=350,y=500)

                a.optionB = tk.Button(width=30,bd=10,height=2,text=a.Ques.options[1],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=a.button2)
                a.optionB.place(x=750, y=500)

                a.optionC = tk.Button(width=30,bd=10,height=2,text=a.Ques.options[2],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=a.button3)
                a.optionC.place(x=350,y=600)

                a.optionD = tk.Button(width=30,bd=10,height=2,text=a.Ques.options[3],fg='gold',bg="dark blue",font=("times new roman",15,'bold'),command=a.button4)
                a.optionD.place(x=750, y=600)

                a.question_label = tk.Label(width=50,bd=15,height=4,text=a.Ques.text,font=("times new roman",18,'bold'),relief='raised',fg='gold',bg="dark blue")
                a.question_label.place(x=425, y=250)
