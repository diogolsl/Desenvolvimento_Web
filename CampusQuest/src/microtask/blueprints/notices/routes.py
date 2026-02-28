from flask import render_template

from . import bp

@bp.get('/avisos')
def avisos():
    avisos = [] 
    return render_template('notices/aviso.html', avisos=avisos)