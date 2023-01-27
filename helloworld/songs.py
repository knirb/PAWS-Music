from flask import Blueprint, render_template
from helloworld import awscontroller
bp = Blueprint('songs', __name__, url_prefix='/songs')

@bp.route('/', methods=['GET'])
def home():
    items = awscontroller.get_songs()['Items']
    return render_template('songs/index.html', items = items)