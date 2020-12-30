
from flask import render_template
from forum import app
from flask import send_from_directory


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    username = request.form['username']
    password = request.form['password']

@app.route('/webpushr')
def send():
    return send_from_directory('js', 'webpushr-sw.js')
