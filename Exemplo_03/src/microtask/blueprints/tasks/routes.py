from . import bp

@bp.route('/')
def listar_tarefas():
    return "Listagem de tarefas"