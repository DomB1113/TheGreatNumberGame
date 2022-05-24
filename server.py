
from unittest.mock import seal
from flask import Flask,redirect,request, render_template, session
import random
app = Flask(__name__)
app.secret_key = "Dominicks secret key!"
@app.route('/')
def index():
    if 'random' not in session:
        session['random']= random.randrange(1,100)
    print(session['random'])
    if 'visits' not in session:
        session['visits']= 0

    return render_template('index.html')

@app.route('/guess', methods= ['POST'])
def guess():
    print(request.form['guess'])
    session['guess'] = request.form['guess'] 
    if int(session['guess']) > int(session['random']):
        return redirect('/toohigh')
    if int(session['guess']) < int(session['random']):
        return redirect('/toolow')
    if int(session['guess']) == int(session['random']):
        return redirect('/congrates')


@app.route('/congrates')
def congrates():
    return render_template('congrates.html')

@app.route('/toohigh')
def toohigh():
    session['visits'] += 1
    return render_template('toohigh.html')

@app.route('/toolow')
def toolow():
    session['visits'] += 1
    return render_template('toolow.html')

@app.route('/tryagain', methods = ['POST'])
def tryagain():
    session.clear()
    return redirect('/')


    
if __name__ == "__main__":
    app.run(debug=True)