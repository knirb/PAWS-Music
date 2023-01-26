#!flask/bin/python
import json
from flask import Flask, Response, render_template
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

""" @application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hej'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200) """

@application.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@application.route('/playlists/')
def playlists():
    return render_template('playlists.html')

if __name__ == '__main__':
    flaskrun(application)

 


