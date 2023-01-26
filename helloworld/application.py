#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun
import awscontroller

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello Worldddd'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/get-songs', methods=['GET'])
def get_songs():
    return awscontroller.get_songs()


if __name__ == '__main__':
    flaskrun(application)
