import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Setting some Global variables
qs = int
line_question = ""
ans = int
line_answer = ""
scores = list()



def write_to_file(filename, data):
    """Handle the process of writing data to a file"""
    with open(filename, "a") as file:
        file.writelines(data)



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
    
def get_scores():
    scores = list()
    with open('./text/score.txt') as f:
        for i in f:
            scores.append(i.strip())
        scores.sort(reverse=True)
    return scores
        

@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/about')
def about():
    return render_template("/about.html")
    
@app.route('/score')
def score():
    scores = get_scores()
    return render_template("/score.html", scores = scores)


@app.route('/game/', methods=['GET', 'POST'])
def game():
    """Main page with instructions"""
    num = 0
    score = 0
    # Handle POST request
    if request.method == "POST":
        write_to_file("text/users.txt", request.form["username"].title() + "\n")
        return redirect(url_for("question", username = request.form["username"].title(), num = num, score = score ))
    return render_template("/game.html")
    
@app.route('/<username>/<num>/<score>', methods=['GET', 'POST'])
def question(username, num, score):
    number = int(num)
    question = get_question(number)
    answer = get_answer(number)
    score = int(score)
        
    
    if request.method == 'POST':
        write_to_file("text/guess.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        guess = guess.lower()
        
        if guess == answer:
            score = score + 10
            if number < 19:
                number = number + 1
            else:
                write_to_file("text/score.txt", str(score) + " Points  -  Username: " + username + "\n")
                return redirect(url_for("score"))
        else:
            score = score - 3
            
        return redirect(url_for("question", username = username, num = number, score = score))
    
    return render_template("/question.html", username=username, question=question, answer=answer)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            