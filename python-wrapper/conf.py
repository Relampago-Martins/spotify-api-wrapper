"""Conf file for the Spotify API."""
import os
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID= os.getenv('CLIENT_ID')
CLIENT_SECRET= os.getenv('CLIENT_SECRET')
SCOPE = "user-library-read, user-top-read, user-read-recently-played, user-read-currently-playing"
REDIRECT_URI='https://www.google.com.br'

def get_token():
    """Get the user token from the authorazed user"""
    auth_manager = SpotifyOAuth(scope=SCOPE,
                    client_id=CLIENT_ID, client_secret=CLIENT_SECRET, redirect_uri=REDIRECT_URI)

    return auth_manager.get_access_token(as_dict=False)
