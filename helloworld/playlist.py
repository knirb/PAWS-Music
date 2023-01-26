from flask import Blueprint, render_template, request
import awscontroller
bp = Blueprint('playlist', __name__, url_prefix='/playlist')
import string
import random    

@bp.route('/', methods=['GET'])
def home():
    items = awscontroller.get_playlists()['Items']
    return render_template('playlist/index.html', items = items)

@bp.route('/new', methods=['GET'])
def new():
    letters = string.ascii_letters
    id = ''.join(random.choice(letters) for i in range(10));
    return render_template('playlist/new.html', id=id)

@bp.route('/new', methods=['POST'])
def new_playlist_form():
    try:
        id = request.form['id']
        title = request.form['title']
        awscontroller.create_playlist(id, title)
        return render_template('playlist/success.html', title = title)
    except:
        return render_template('500.html')

@bp.route('/<id>', methods=['GET'])
def specific(id):
    try:
        playlist = awscontroller.get_playlist(id)['Item']
        print(playlist)
        return render_template('playlist/id.html', playlist = playlist)
    except:
        return render_template('500.html')
    
