qs = int
line = ""
def get_question(qs):
    f = open('./text/question.txt')
    for x, line in enumerate(f):
        if x == qs:
            return (line)
    f.close()

get_question(qs)



