from flask import render_template
from . import bp

@bp.get('/missoes')
def missoes():
    missoes = [
            {
                'titulo': 'Missão 1: Exploração do Campus',
                'descricao': 'Explore o campus e encontre pontos de interesse, como bibliotecas, laboratórios e áreas de lazer.',
                'recompensa': '50 pontos de experiência'
            }
        ]
    return render_template('templates/missions/missoes.html', missoes=missoes)