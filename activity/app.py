from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/registration')
def registration():
    return render_template('registration.html')

@app.route('/method')
def method():
    return render_template('method.html')



