from flask import render_template
from . import bp

bp.get('/')
def home():
    return render_template('templates/pages/home.html')

bp.get('/sobre')
def sobre():
    return render_template('templates/pages/sobre.html')
