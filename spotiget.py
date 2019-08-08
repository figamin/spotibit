import requests
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

#clientID = '278024b7be9d447fbea9d0cc5660b904'
#clientSecret = '5f160c0b60174ee8925f8a67ccf9aab6'
clientID = 'aa836a23666f44d6801955021f69b594'
clientSecret = '58a7f746e05e4dc2b17a7a618f92f5f8'
clientCreds = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
musicGet = spotipy.Spotify(client_credentials_manager=clientCreds)
token = util.prompt_for_user_token(username='Studsquito', scope='user-read-currently-playing', client_id=clientID, client_secret=clientSecret, redirect_uri='http://localhost/')
def getSongs():
    results = musicGet.search(q='lil uzi vert', limit=10)
    songs = []
    for i, j in enumerate(results['tracks']['items']):
        test = (j['name'])
        songs.append(test)
    return songs
def isPlaying():

    currentlyPlaying = spotipy.Spotify(auth=token)
    actualPlaying = currentlyPlaying.currently_playing()["is_playing"]
    print(actualPlaying)
    if actualPlaying == "True":
        playing = True
    else:
        playing = False
    return playing

