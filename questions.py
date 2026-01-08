fh = open("Question bank.txt",'r')

fh_options = open("options.txt",'r')

fh_correct = open("correct.txt",'r')
    
questions = fh.readlines()

options = fh_options.readlines()

correct_answers = fh_correct.readlines()

c = 1

k = 1

n = 1

op = 0

questions_list = []

options_list = []

correct_ans_list = []

options_per_question = []

while True:
    a_question = ""

    word = ""

    letters = []

    try:
        a = questions.index("question " + str(n+1) + "\n")
        question = slice(questions.index("question " + str(n) + "\n"),a)
    except:
        break

    for element in questions[question]:
        if not element == "\n":
            if not element == ("question " + str(n) + "\n"):
                a_question += (" " + str(element))
                A_question = a_question.replace("\n",'')
    questions_list.append(str(A_question))

    
    n += 1

while True:
    a_option = ""

    try:
        
        b = options.index("option " + str(c+1) + "\n")
        option = slice(options.index("option " + str(c) + "\n"),b)
        
    except:
        break

    for element in options[option]:
        if not element == "\n":
            if not element == ("option " + str(c) + "\n"):
                A_option = element.replace("\n",'')
                options_list.append(str(A_option))

    
    c += 1

while True:
    try:
        options_per_question.append((options_list[op],options_list[op + 1],options_list[op + 2],options_list[op + 3]))  
    except:
        break

    op += 4

while True:
    a_correct_ans = ""

    word = ""

    letters = []

    try:
        a = correct_answers.index("correct ans " + str(k+1) + "\n")
        correct_ans = slice(correct_answers.index("correct ans " + str(k) + "\n"),a)
    except:
        break

##    for element in options[option]:
##        if not element == "\n":
##            if not element == ("option " + str(c) + "\n"):
##                A_option = element.replace("\n",'')
##                options_list.append(str(A_option))

    for element in correct_answers[correct_ans]:
        if not element == "\n":
            if not element == ("correct ans " + str(k) + "\n"):
                #a_correct_ans += (" " + str(element))
                A_correct_ans = element.replace("\n",'')
                correct_ans_list.append(str(A_correct_ans))

    
    k += 1

##print(questions_list)
##print(options_per_question)
##print(correct_ans_list)

fh.close()
fh_options.close()
fh_correct.close()
