import boto3

dynamo_client = boto3.resource('dynamodb')

def get_playlists():
    return dynamo_client.Table('Playlists').scan()

def get_songs():
    return dynamo_client.Table('Songs').scan()

def create_playlist(id, name): 
    dynamo_client.Table('Playlists').put_item(
        Item = {
            'PlaylistID': id,
            'Title': name,
        }
    )

def get_playlist(id): 
    print(id)
    return dynamo_client.Table('Playlists').get_item(
        Key={
            'PlaylistID': id
        }
    )