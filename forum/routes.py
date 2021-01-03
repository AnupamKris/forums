
from flask import render_template, request, redirect, url_for, jsonify, make_response, flash, session
from forum import app, db, bcrypt
from flask import send_from_directory
from flask_login import login_user, login_required, logout_user
import requests
import os
from forum.models import User, Post

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
@app.route('/home', methods=['GET'])
@login_required
def home():
    return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        repassword = request.form['repassword']
        email = request.form['email']
        user = User.query.filter_by(email=email).first()
        if user:
            print('User already exists')
            return make_response({'message': 'Email already exists!'})
        elif password == repassword:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            user = User(password=hashed_password, username=username, type = 3, email=email)
            db.session.add(user)
            db.session.commit()
            print('Creating User')
            flash("Account created successfully.. You can now login")
            return make_response({'message': 'redirect'})
        else:
            print('Password does not match')
            return make_response({'message': 'Passwords does not match!'})
    else:
        return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            return make_response({'data': 'redirect'})
        else:
            return make_response({'data':'true'})
    else:
        return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# -------- Misc Routes -------- #

@app.route('/webpushr-sw.js')
def send():
    return send_from_directory(app.static_folder+os.sep+'js','webpushr-sw.js')

@app.route('/favicon.ico')
def icon():
    return send_from_directory(app.static_folder+os.sep+'icon','favicon.ico')

@app.route('/notif.png')
def notif_icon():
    return send_from_directory(app.static_folder+os.sep+'icon','icon.png')
