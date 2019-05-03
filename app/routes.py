from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm
from app.models import User
#-----------------------------------------------------------------------------------FIELDS
#-----------------------------------------------------------------------------------ROUTES
@app.route('/')
@app.route('/index')
@login_required
def index():
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
    return render_template('index.html',title = 'Home Page', posts=posts)

""" Login form that serves a template with the flask-wtf login form
    handles user creation """
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:       
        return redirect(url_for('index')) # Return the logged in user to the homepage?
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first() # Get the user from the database
        if user is None or not user.check_password(form.password.data):
            # user does not exist or the wrong password has been entered
            flash('Invalid username or password')
        login_user(user, remember=form.remember_me.data) # Log in the User
        
        # Right after the user is logged in by calling Flask-Login's login_user() 
        # function, the value of the next query string argument is obtained
        next_page = request.args.get('next') 
        if not next_page or url_parse(next_page).netloc != '': # if netloc isn't null, then this is a full url, which we don't want
            next_page = url_for('index')
        return redirect(next_page) #redirect to the home page with the user logged in
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:       
        return redirect(url_for('index')) # Return the logged in user to the homepage?
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)