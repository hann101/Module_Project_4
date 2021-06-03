from flask import Blueprint, Flask, render_template
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello'


# @bp.route('/')
# def index():
#     return 'index'

@bp.route('/')
def index():
    return render_template('home.html')

@bp.route('/chart')
def chart():
    return render_template('chart.html')
