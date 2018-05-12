qs = int
line_question = ""
def get_question(qs):
    f = open('./text/question.txt')
    for x, line_question in enumerate(f):
        if x == qs:
            return (line_question)
    f.close()



ans = int
line_answer = ""
def get_answer(ans):
    f = open('./text/answer.txt')
    for x, line_answer in enumerate(f):
        if x == ans:
            return (line_answer)
    f.close()




