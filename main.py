#
# @Author: Bhaskar S
# @Blog:   https://www.polarsparc.com
# @Date:   30 Aug 2021
#

from flask import request, session, redirect, jsonify
from flask.templating import render_template
from config.config import app
from model.user import User

@app.before_request
def verify_logged():
    app.logger.debug('Reuqest path: %s' % request.path)
    if 'logged_user_id' not in session and request.path in ['/secure']:
        return redirect('/login')

@app.route('/')
def index():
    return render_template('welcome.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        return render_template('signup.html')
    email = None
    if 'email' in request.json:
        email = request.json['email']
    if email is None or len(email.strip()) == 0:
        return jsonify({'url': '/signup', 'code': 1001, 'error': 'Invalid email !!!'}), 400
    password1 = None
    if 'password1' in request.json:
        password1 = request.json['password1']
    if password1 is None or len(password1.strip()) == 0:
        return jsonify({'url': '/signup', 'code': 1002, 'error': 'Invalid password !!!'}), 400
    password2 = None
    if 'password2' in request.json:
        password2 = request.json['password2']
    if password1 != password2:
        return jsonify({'url': '/signup', 'code': 1003, 'error': 'Password confirmation failed !!!'}), 400
    user = User.register(email, password1)
    msg = 'User %s successfully registered!' % user
    app.logger.info(msg)
    return jsonify({'url': '/signup', 'code': 0, 'email-id': email})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('welcome.html')
    email = None
    if 'email' in request.json:
        email = request.json['email']
    if email is None or len(email.strip()) == 0:
        return jsonify({'url': '/login', 'code': 1004, 'error': 'Invalid email !!!'}), 400
    password = None
    if 'password' in request.json:
        password = request.json['password']
    if password is None or len(password.strip()) == 0:
        return jsonify({'url': '/login', 'code': 1005, 'error': 'Invalid password !!!'}), 400
    user = User.query_by_email(email)
    if user is None:
        return jsonify({'url': '/login', 'code': 1004, 'error': 'Invalid email !!!'}), 400
    if not user.verify_password(password):
        return jsonify({'url': '/login', 'code': 1005, 'error': 'Invalid password !!!'}), 400
    msg = 'User %s successfully logged in!' % user
    app.logger.info(msg)
    session['logged_user_id'] = email
    return jsonify({'url': '/login', 'code': 0, 'email-id': email})

@app.route('/secure', methods=['GET'])
def secure():
    return render_template('secure_notes.html')

@app.route('/logout', methods=['GET'])
def logoff():
    session.pop('logged_user_id', None)
    return render_template('welcome.html')
