# Spotify Playlist Duplicate Remover

- This Python script removes duplicate tracks from a specified Spotify playlist using the Spotify API.

- If a duplicate is found, it removes the most recently added instance while preserving the first one.

## Prerequisites

1. [Create a Spotify Developer account and create a new app using this link](https://developer.spotify.com/dashboard/applications).
2. Note down the `Client ID`, `Client Secret`, and `Redirect URI` in your Spotify Developer Dashboard.

## Setup

1. Install the required library:

   ```bash
   pip install spotipy
   ```

2. Replace the placeholders in the script with your own information.
3. Run the script.

## Script Explanation
The script uses the spotipy library to interact with the Spotify API.
It retrieves the tracks from the specified playlist and identifies duplicates based on their id and added_at timestamp.

