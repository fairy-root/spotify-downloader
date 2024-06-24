# Spotify Downloader

This is a Python script to download single tracks and full albums from Spotify. The script uses the Spotify Web API to fetch metadata and `yt-dlp` to download the tracks.

## Features

- Download single tracks from Spotify.
- Download full albums from Spotify.
- Organize downloaded tracks into folders named after the artist.

## Prerequisites

- Python 3.6+
- Spotify Developer Account

## Setup

1. **Clone the repository:**

   ```sh
   git clone https://github.com/fairy-root/spotify-downloader.git
   cd spotify-downloader
   ```

2. **Install dependencies:**

   Install the required Python packages using `pip`:

   ```sh
   pip install -r requirements.txt
   ```

3. **Set up Spotify API credentials:**

   - Create a Spotify Developer account and register a new application at the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
   - Obtain your `client_id` and `client_secret`.

4. **Set environment variables:**

   Set the `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET` environment variables with your Spotify API credentials:

   ```sh
   export SPOTIPY_CLIENT_ID='your_spotify_client_id'
   export SPOTIPY_CLIENT_SECRET='your_spotify_client_secret'
   ```

## Usage

1. **Run the script:**

   ```sh
   python spotify.py
   ```

2. **Enter the Spotify link:**

   The script will prompt you to enter a Spotify link for a track or album. Enter the link and the script will download the track(s) into a folder named after the artist.

   Example links:
   - Track: `https://open.spotify.com/track/your_track_id`
   - Album: `https://open.spotify.com/album/your_album_id`

## Example

```sh
$ python spotify.py
Enter the Spotify link for a track or album: https://open.spotify.com/album/6QupeOoSn316Iwv9D3tJz7?si=IpEwJ0XGRuelCjfAl1qKew
Downloading album: Hogtied Revisited by The White Buffalo
Downloaded: Love Song #1 by The White Buffalo
Downloaded: BB Guns and Dirt Bikes by The White Buffalo
...
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
```