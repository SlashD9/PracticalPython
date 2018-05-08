
import os
from flask import Flask, render_template, redirect, request

app = Flask(__name__)


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
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)