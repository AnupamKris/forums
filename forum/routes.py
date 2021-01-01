
from flask import render_template, request, redirect, url_for
from forum import app, db, bcrypt
from flask import send_from_directory
from flask_login import login_user, login_required, logout_user
import requests
import os
@app.route('/send')
def send_notification():
    headers = {
        'webpushrKey': '56146723d78a3315dc38a4be870b5e94',
        'webpushrAuthToken': '20944',
        'Content-Type': 'application/json',
    }

    data = '{"title":"Childrens Day","message":"Holiday","target_url":"pecforums.pythonanywhere.com", "icon":"https://pecforums.pythonanywhere.com/notif.png"}'

    response = requests.post('https://api.webpushr.com/v1/notification/send/all', headers=headers, data=data)

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            return redirect(url_for('forum_home'))
        else:
            flash('Login Unsuccessful!')
            return render_template('home.html')
    else:
        return render_template('home.html')

@app.route('/forum_home')
def forum_home():
    return None

@app.route('/webpushr-sw.js')
def send():
    return send_from_directory(app.static_folder+os.sep+'js','webpushr-sw.js')

@app.route('/favicon.ico')
def icon():
    return send_from_directory(app.static_folder+os.sep+'icon','favicon.ico')

@app.route('/notif.png')
def notif_icon():
    return send_from_directory(app.static_folder+os.sep+'icon','icon.png')
