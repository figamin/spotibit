import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
clientCreds = SpotifyClientCredentials(client_id='278024b7be9d447fbea9d0cc5660b904', client_secret='5f160c0b60174ee8925f8a67ccf9aab6')
musicGet = spotipy.Spotify(client_credentials_manager=clientCreds)
def getSongs():
    results = musicGet.search(q='24k magic', limit=10)
    songs = []
    for i, j in enumerate(results['tracks']['items']):
        test = (j['name'])
        songs.append(test)
    return songs

