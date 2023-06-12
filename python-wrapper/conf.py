"""Conf file for the Spotify API."""
from spotipy.oauth2 import SpotifyOAuth


SCOPE = "user-library-read, user-top-read, user-read-recently-played user-read-currently-playing"
CLIENT_ID='be238fff4cba4a93b09c30f2abc1fcad'
CLIENT_SECRET='75bc722ada324380a5e85b0a6c946787'
REDIRECT_URI='https://www.google.com.br'

def get_token():
    """Get the user token from the authorazed user"""
    auth_manager = SpotifyOAuth(scope=SCOPE,
                    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

    return auth_manager.get_access_token(as_dict=False)
