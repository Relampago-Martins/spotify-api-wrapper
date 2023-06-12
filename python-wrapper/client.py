"""Classe Cliente"""
from uplink import Consumer, headers, Body
from uplink.commands import get
from uplink.returns import json

from conf import get_token

@headers({
    'Authorization': f'Bearer {get_token()}',
})
class Spotify(Consumer):
    """
        Classe cliente, responsável por se conectar com a api do spotify
        base_url:
    """
    @json
    @get('me/albums')
    def get_albums(self, **kwargs: Body):
        """
            Método responsável por pegar os albuns do usuário
        """
    @json(key='items')
    @get('me/top/tracks?time_range=short_term&limit=10')
    def top_5_tracks(self, **kwargs: Body):
        """
            Método responsável por pegar os top 5 artistas do usuário
        """

if __name__ == "__main__":
    spotify = Spotify(base_url="https://api.spotify.com/v1/")
    tracks = [track['name'] for track in spotify.top_5_tracks()]
    print(tracks)
