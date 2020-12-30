
from flask import render_template
from forum import app
from flask import send_from_directory
import requests

@app.route('/send')
def send_notification():
    proxies = {"https",'proxy.server:3128'}
    headers = {
        'webpushrKey': '843f25b03dab2be8e3fe585d5dea5664',
        'webpushrAuthToken': '20917',
        'Content-Type': 'application/json',
    }

    data = '{"title":"Childrens Day","message":"Holiday","target_url":"pecforums.pythonanywhere.com"}'

    response = requests.post('https://api.webpushr.com/v1/notification/send/all', headers=headers, data=data)

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
