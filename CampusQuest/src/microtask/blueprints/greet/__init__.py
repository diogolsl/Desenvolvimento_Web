from flask import Blueprint

bp = Blueprint('greet', __name__)

from . import routes