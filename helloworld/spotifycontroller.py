# import spotipy 
# from spotipy.oauth2 import SpotifyClientCredentials

# auth_manager = SpotifyClientCredentials()
# sp = spotipy.Spotify(auth_manager=auth_manager)
# playlists = sp.user_playlists('spotify')

# def get_playlists():
#     return playlists

# def get_song(search_term):
#     tracks_items = sp.search(search_term,1,0,"track")
#     first_song = tracks_items['tracks']['items'][0]
#     song_url = first_song['external_urls']['spotify']
#     iframe_url = "https://open.spotify.com/embed/track/" + song_url.rsplit('/', 1)[-1]
#     artist = first_song['artists'][0]['name']
#     song_name = first_song['name']

#     return {
#         "iframe_url": iframe_url,
#         "artist": artist,
#         "song_name": song_name
#     }