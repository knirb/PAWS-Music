from flask import Blueprint, render_template
import awscontroller
bp = Blueprint('playlist', __name__, url_prefix='/playlist')

@bp.route('/', methods=['GET'])
def home():
    res = awscontroller.get_playlists()
    return render_template('playlist/index.html', res = res)

