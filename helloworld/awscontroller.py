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

def add_song(songId, title, artist, link, playlistId):
    print(songId, title, artist, link, playlistId)
    return dynamo_client.Table('Playlists').update_item(
        Key = {
            'PlaylistID': playlistId,
        },
        UpdateExpression='SET Songs = :val1',
        ExpressionAttributeValues={
        ':val1': [{'SongID': songId, 'Title': title, 'Artist': artist, 'Link': link}]
    }
    )
