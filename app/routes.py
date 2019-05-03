from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from app import app
from app.forms import LoginForm
from app.models import User
#-----------------------------------------------------------------------------------FIELDS
#-----------------------------------------------------------------------------------ROUTES
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ben'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title = 'Home', user=user, posts=posts)

""" Login form that serves a template with the flask-wtf login form
    handles user creation """
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:       
        return redirect(url_for('index')) # Return the logged in user to the homepage?
    form = LoginForm()
    if form.validate_on_submit():
        # Get the user from the database
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            # user does not exist or the wrong password has been entered
            flash('Invalid username or password')
        login_user(user, remember=form.remember_me.data) # Log in the User
        return redirect(url_for('/index')) #redirect to the home page with the user logged in
    return render_template('login.html', title='Sign In', form=form)