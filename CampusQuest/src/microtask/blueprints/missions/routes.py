from flask import render_template
from . import bp

@bp.get('/missoes')
def missoes():
    missoes = [{ 'id': 1, 'titulo': 'Missão 1', 'descricao': 'Descrição da Missão 1' },
              { 'id': 2, 'titulo': 'Missão 2', 'descricao': 'Descrição da Missão 2' },
              { 'id': 3, 'titulo': 'Missão 3', 'descricao': 'Descrição da Missão 3' },
              { 'id': 4, 'titulo': 'Missão 4', 'descricao': 'Descrição da Missão 4' }]
    return render_template('templates/missions/missoes.html', missoes=missoes)