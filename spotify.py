import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import yt_dlp as youtube_dl
import re
import os

# Get Spotify credentials from environment variables
SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SPOTIPY_CLIENT_SECRET')

if not SPOTIPY_CLIENT_ID or not SPOTIPY_CLIENT_SECRET:
    raise ValueError("Please set the SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET environment variables")
    
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                           client_secret=SPOTIPY_CLIENT_SECRET))

def download_from_youtube(query, artist_name):
    # Create directory if it doesn't exist
    if not os.path.exists(artist_name):
        os.makedirs(artist_name)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(artist_name, '%(title)s.%(ext)s'),
        'quiet': True
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch:{query}"])

def download_track(track_id):
    track = sp.track(track_id)
    track_name = track['name']
    artists = ', '.join([artist['name'] for artist in track['artists']])
    query = f"{track_name} {artists} audio"
    artist_name = track['artists'][0]['name']
    download_from_youtube(query, artist_name)
    print(f"Downloaded: {track_name} by {artists}")

def download_album(album_id):
    album = sp.album(album_id)
    album_name = album['name']
    artist = album['artists'][0]['name']
    print(f"Downloading album: {album_name} by {artist}")
    tracks = album['tracks']['items']
    for track in tracks:
        track_id = track['id']
        download_track(track_id)

def main():
    link = input("Enter the Spotify link for a track or album: ")

    track_regex = re.compile(r'open\.spotify\.com/track/([a-zA-Z0-9]+)')
    album_regex = re.compile(r'open\.spotify\.com/album/([a-zA-Z0-9]+)')

    track_match = track_regex.search(link)
    album_match = album_regex.search(link)

    if track_match:
        track_id = track_match.group(1)
        download_track(track_id)
    elif album_match:
        album_id = album_match.group(1)
        download_album(album_id)
    else:
        print("Invalid link. Please enter a valid Spotify track or album link.")

if __name__ == "__main__":
    main()