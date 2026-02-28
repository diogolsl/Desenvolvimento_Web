from flask import render_template

from . import bp

@bp.get('/ola/<nome>')
def ola(nome):
    return render_template('greet/ola.html', nome=nome)