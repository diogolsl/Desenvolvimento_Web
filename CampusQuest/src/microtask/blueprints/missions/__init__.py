from flask import Blueprint

bp = Blueprint('missions', __name__)

from . import routes
