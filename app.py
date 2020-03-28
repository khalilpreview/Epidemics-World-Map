import os
import datetime
from flask import Flask , render_template , redirect , url_for

# Flask app initialisation
app = Flask(__name__)


# routes and views start here.
# ...
# home the index route and view
@app.route('/')
def home_page():
    title = 'E-W-M'
    return render_template('index.html' , title=title)

# registration  route and view
@app.route('/register')
def register_page():
    title = 'Registration E-W-M'
    return render_template('registration.html' , title=title)

# login route and view
@app.route('/login')
def registeration_page():
    title = 'Login E-W-M'
    return render_template('login.html' , title=title)

# dashboard route and view
@app.route('/dashboard')
def dashboard_page():
    title = 'Dashboard E-W-M'
    return render_template('dashboard.html' , title=title)