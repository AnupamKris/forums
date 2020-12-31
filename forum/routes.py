
from flask import render_template
from forum import app
from flask import send_from_directory
import requests
import os
@app.route('/send')
def send_notification():
    headers = {
        'webpushrKey': '56146723d78a3315dc38a4be870b5e94',
        'webpushrAuthToken': '20944',
        'Content-Type': 'application/json',
    }
    icon = app.static_folder+os.sep+'icon'+os.sep+'favicon.ico'
    data = f'{"title":"Childrens Day","message":"Holiday","target_url":"pecforums.pythonanywhere.com", "icon":"{icon}"}'

    response = requests.post('https://api.webpushr.com/v1/notification/send/all', headers=headers, data=data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    username = request.form['username']
    password = request.form['password']


@app.route('/webpushr-sw.js')
def send():
    return send_from_directory(app.static_folder+os.sep+'js','webpushr-sw.js')
@app.route('/favicon.ico')
def icon():
    return send_from_directory(app.static_folder+os.sep+'icon','favicon.ico')
