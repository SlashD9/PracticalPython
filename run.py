
import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
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
            return (line_question)
    f.close()

# This functions gets the answer based on then paramenter provided
def get_answer(ans):
    f = open('./text/answer.txt')
    for x, line_answer in enumerate(f):
        if x == ans:
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
    if request.method == 'POST':
        print(request.form)
        
    return render_template("/game.html")
    
@app.route('/game/question/', methods=['GET', 'POST'])
def answer():
    if request.method == 'POST':
        print(request.form)
        
    return render_template("/question.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
            