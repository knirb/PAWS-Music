from flask import Blueprint, render_template
import awscontroller
bp = Blueprint('songs', __name__, url_prefix='/songs')

@bp.route('/', methods=['GET'])
def home():
    res = awscontroller.get_songs()
    print(res)
    return render_template('songs/index.html', res = res)