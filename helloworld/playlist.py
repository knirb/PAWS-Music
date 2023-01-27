import json
from flask import Blueprint, render_template, request, Response
from helloworld import awscontroller
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
    id = ''.join(random.choice(letters) for i in range(10))
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
        return render_template('playlist/id.html', playlist = playlist)
    except:
        return render_template('500.html')


@bp.route('/add-song/<playlistId>', methods=['PUT'])
def add_song(playlistId):
    try:
        id=request.form['id']
        songTitle=request.form['songTitle']
        artist=request.form['artist']
        link=request.form['link']
        songs = awscontroller.get_playlist(id)['Item']['Songs']
        awscontroller.add_song(id, songTitle, artist, link, playlistId, songs)
    except:
        return render_template('500.html')

@bp.route('/delete/<id>', methods=['DELETE'])
def delete_playlist(id):
    awscontroller.delete_playlist(id)
    return Response(json.dumps({'Output': 'Kingen'}), mimetype='application/json', status=200)