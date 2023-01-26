import boto3

dynamo_client = boto3.client('dynamodb')

def get_playlists():
    return dynamo_client.scan(
        TableName='Playlists'
    )

def get_songs():
    return dynamo_client.scan(
        TableName='Songs'
    )