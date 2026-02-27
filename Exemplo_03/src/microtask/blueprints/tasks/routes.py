from flask import render_template
from . import bp

@bp.route('/')
def listar_tarefas():
    tarefas = [ "Estudar Flask", "Criar API", "Testar aplicação" ]
    return render_template('tasks/listar_tarefas.html', tarefas=tarefas)