
import os
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
# Setting some Global variables
qs = int
line_question = ""
ans = int
line_answer = ""

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


@app.route('/')
def index():
    return render_template("/index.html")


@app.route('/about')
def about():
    return render_template("/about.html")


@app.route('/game/', methods=['GET', 'POST'])
def game():
    """Main page with instructions"""
    num = 0
    # Handle POST request
    if request.method == "POST":
        write_to_file("text/users.txt", request.form["username"] + "\n")
        return redirect(url_for("question", username = request.form["username"], num = num))
    return render_template("/game.html")
    
@app.route('/<username>/<num>/', methods=['GET', 'POST'])
def question(username, num):
    number = int(num)
    question = get_question(number)
    answer = get_answer(number)
    score = 0
    
    if request.method == 'POST':
        write_to_file("text/guess.txt", request.form["answer"] + "\n")
        guess = request.form["answer"]
        print(guess)
        print(answer)
        
        if guess == answer:
            score = score + 10
            print(score)
            if number < 19:
                number = number + 1
            else:
                return render_template("/index.html")
        
            
        return redirect(url_for("question", username = username, num = number))
    
    return render_template("/question.html", username=username, question=question, answer=answer)
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            