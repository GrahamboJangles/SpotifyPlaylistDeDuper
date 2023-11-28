import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Find this information at https://developer.spotify.com/dashboard and make a developer app
client_id = "your_client_id"
client_secret = "your_client_id"
redirect_uri = "your_redirect_uri"

# Get this info from Spotify itself
spotify_username = "your_spotify_name"
playlist_url = "https://open.spotify.com/playlist/37i9dQZF1DWUVpAXiEPK8P"

# Get the playlist id from the url
playlist_id = playlist_url.split('/')[-1]
playlist_id = playlist_id.split('?')[0]
playlist_id = playlist_id.split('&')[0]

# Set up the Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='playlist-modify-public', username=spotify_username))

# Get the tracks from the playlist
results = sp.playlist_items(playlist_id)

# Dictionary to keep track of track ids and their added_at
track_ids = {}

# Populate the dictionary with track ids and their added_at
while results:
    for item in results['items']:
        track_id = item['track']['id']
        added_at = item['added_at']
        
        if track_id not in track_ids.keys():
            track_ids[track_id] = added_at
        else:
            if added_at > track_ids[track_id]:  # if this track was added later than stored one
                # preserve the first added track and remove this one
                print(f"Removing most recently added duplicate track: {item['track']['name']} by {item['track']['artists'][0]['name']}")
                sp.playlist_remove_all_occurrences_of_items(playlist_id, [track_id])
                
    if results['next']:
        results = sp.next(results)
    else:
        results = None

print("Duplicates removed successfully!")
