import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def create_spotify_client():
    """
    Creates and returns a Spotipy client using SpotifyOAuth.
    This automatically handles the Authorization Code Flow, 
    token caching (.cache file), and token refreshing.
    """
    
    # Get the required scope from your .cache file (already defined)
    SCOPE = "user-read-playback-state user-modify-playback-state"

    # 1. Set up the OAuth Manager object
    auth_manager = SpotifyOAuth(
        client_id=os.getenv("SPOTIPY_CLIENT_ID"),
        client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
        # Spotipy will now use this URI and try to start a temporary server to listen for the redirect
        redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
        scope=SCOPE,
        cache_path=".cache",
        show_dialog=True # Forces a login prompt on first run if cache fails
    )

    # 2. Create the Spotify client using the auth_manager
    # This is the key change. Spotipy now handles the full authorization lifecycle.
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # Check if a token was successfully obtained (this handles the first-run logic)
    if not sp.auth_manager.get_cached_token():
        # If no token is cached, prompt the user to complete the flow manually
        auth_url = sp.auth_manager.get_authorize_url()
        print(f"Token not found. Please log in using this link:\n{auth_url}")
        print("\nAfter successful authorization, Spotipy will automatically grab the token and cache it.")

    return sp

def play_track(sp, track_uri):
    """
    Checks for an active Spotify device and starts playback of a track.
    """
    
    # Check for active devices (a very common reason for playback to fail)
    devices = sp.devices()
    
    if not devices['devices']:
        print("❌ Error: No active Spotify devices found.")
        print("Please start Spotify playback on a device (e.g., the desktop app, web player, or phone) and try running the script again.")
        return

    # Use the ID of the first available device
    device_id = devices['devices'][0]['id']
    print(f"▶️ Playing on device: {devices['devices'][0]['name']}")
    
    # Start playback
    sp.start_playback(uris=[track_uri], device_id=device_id)