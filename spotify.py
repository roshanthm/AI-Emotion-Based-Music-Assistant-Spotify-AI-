import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_spotify_client():
    """
    Creates and returns a Spotipy client using the Authorization Code Flow 
    (SpotifyOAuth). This is the recommended, automated way to handle 
    authentication, token caching, and refreshing.
    """
    
    # Define the necessary permissions (scopes) for reading and controlling playback
    # This must match the scopes you need for your project
    SCOPE = "user-read-playback-state user-modify-playback-state"

    # Set up the OAuth Manager object. It will automatically use the 
    # SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, and SPOTIPY_REDIRECT_URI 
    # environment variables set in your .env file.
    auth_manager = SpotifyOAuth(
        scope=SCOPE,
        cache_path=".cache", # Location to store token info
        # show_dialog=True forces a login prompt on first run/when cache expires
        show_dialog=True 
    )

    # Create the Spotify client instance using the auth_manager
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # On the first run, the auth_manager will open a browser to complete the login.
    # It will automatically launch a temporary web server on http://localhost:8888 
    # to capture the token after authorization.

    return sp

def play_track(sp, track_uri):
    """
    Checks for an active device and starts playback of a track by URI.
    
    Args:
        sp (spotipy.Spotify): The authenticated Spotify client.
        track_uri (str): The Spotify URI of the track to play.
    """
    # 1. Get available devices
    devices = sp.devices()
    
    if not devices['devices']:
        print("❌ Error: No active Spotify devices found.")
        print("Please start Spotify playback on a device (e.g., the desktop app or web player) and try running the script again.")
        return False # Return False on failure

    # 2. Use the ID of the first available device
    device_id = devices['devices'][0]['id']
    print(f"▶️ Playing on device: {devices['devices'][0]['name']}")
    
    # 3. Start playback
    try:
        sp.start_playback(uris=[track_uri], device_id=device_id)
        return True # Return True on success
    except Exception as e:
        print(f"❌ Error during playback: {e}")
        return False

# You can remove the manual functions like get_auth_url() from your old file
# as the SpotifyOAuth class handles the entire flow automatically.