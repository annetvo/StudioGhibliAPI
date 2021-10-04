from app import app
from flask import render_template

@app.route('/')
def home():
    prod_comp='Studio Ghilbli'
    return render_template('index.html', universe=prod_comp)


