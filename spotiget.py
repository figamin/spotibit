import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

clientID = '278024b7be9d447fbea9d0cc5660b904'
clientSecret = '5f160c0b60174ee8925f8a67ccf9aab6'
clientCreds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
musicGet = spotipy.Spotify(client_credentials_manager=clientCreds)
token = util.prompt_for_user_token(username='figman57', scope='user-read-currently-playing', client_id=clientID, client_secret=clientSecret, redirect_uri='http://localhost/')
def getSongs():
    results = musicGet.search(q='lil uzi vert', limit=10)
    songs = []
    for i, j in enumerate(results['tracks']['items']):
        test = (j['name'])
        songs.append(test)
    return songs
def isPlaying():

    currentlyPlaying = spotipy.Spotify(auth=token)
    if currentlyPlaying.currently_playing() == "None":
        playing = False
    else:
        playing = True
    return playing

