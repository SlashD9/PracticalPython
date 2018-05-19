# Setting some Global variables
qs = int
line_question = ""
ans = int
line_answer = ""

# This functions gets the question based on then paramenter provided
def get_question(qs):
    f = open('./text/question.txt')
    for x, line_question in enumerate(f):
        if x == qs:
            line_question = line_question.replace("\n", "")
            return (line_question)
    f.close()

# This functions gets the answer based on then paramenter provided
def get_answer(ans):
    f = open('./text/answer.txt')
    for x, line_answer in enumerate(f):
        if x == ans:
            line_answer = line_answer.replace("\n", "")
            return (line_answer)
    f.close()
    
# This function gets the scores and returns them in a list
def get_scores():
    scores = list()
    with open('./text/score.txt') as f:
        for i in f:
            scores.append(i.strip())
        scores.sort(reverse=True)
    return scores




