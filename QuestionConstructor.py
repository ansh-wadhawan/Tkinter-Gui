import random

from questions import questions_list
from questions import options_per_question
from questions import correct_ans_list

class Question():
    def __init__(self,text,options,correct_ans):
        self.text = text
        self.options = options
        self.correct_ans = correct_ans

class Question_Constructor():
    def __init__(self):
        self.level = 0
        self.ques = 0
        
    def generate(self,level):
        self.level = level
##        a = self.level * 5
##        b = a + 5
        self.ques = level
        text = questions_list[self.ques]
        correct_ans = correct_ans_list[self.ques]
        options = options_per_question[self.ques]
        question = Question(text,options,correct_ans)
        return question

questions_constructor = Question_Constructor()

QUESTION = questions_constructor.generate(0)

        
        
        
