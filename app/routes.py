from app import app
from flask import render_template



@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Index Page')


@app.route('/under_construction')
def construction():
    return render_template('under_construction.html', title='Under Construction')