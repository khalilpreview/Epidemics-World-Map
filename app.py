import os
import datetime
from flask import Flask , render_template , redirect , url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    title = 'E-W-M'
    return render_template('index.html' , title=title)