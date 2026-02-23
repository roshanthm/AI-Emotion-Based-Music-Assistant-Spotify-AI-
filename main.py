from spotify import create_spotify_client, play_track
from emotion import detect_emotion # Import the new AI function

# Mapping of detected emotion to Spotify Track URIs
# These are your examples from the original file (can be changed later)
emotion_tracks = {
    "happy": "spotify:track:2nGFzvIC3F1o2Y6XG9kM0i", # Example: Good Feeling
    "sad": "spotify:track:5hTpBe8h35rJ67eAWHQsJx",   # Example: Lovely
    "calm": "spotify:track:0VjIjW4GlUZAMYd2vXMi3b",  # Example: Blinding Lights (Mapped to Neutral/Calm)
    "angry": "spotify:track:2b8fOow8UzyDFAE27YhOZM", # Example: R U Mine?
    "neutral": "spotify:track:7wBJfE2PBHFWk5zNnDgHRF" # Example: General mood track
}

print("\n🎧 Welcome to your AI Emotion Music Assistant!\n")

# 1. Get user input
user_input = input("How are you feeling today? (Tell me in a sentence or phrase)\n➡ ")

# 2. Detect emotion using the new AI model (or keyword fallback)
detected_emotion = detect_emotion(user_input)

# Check if the detected emotion has a track mapped
track_uri = emotion_tracks.get(detected_emotion, emotion_tracks["neutral"])

print(f"\n🧠 Final Mood Detected: {detected_emotion.upper()}")

# 3. Get Spotify client (This is where the automatic login happens)
print("⚙️ Initializing Spotify Client (First run requires browser login)...")
sp = create_spotify_client()

# 4. Play music
if sp:
    print(f"🎵 Attempting to play track for mood: {detected_emotion}")
    if play_track(sp, track_uri):
        print("✅ Playback command sent successfully!")
    else:
        print("❌ Failed to start playback. Check your Spotify app and try again.")
else:
    print("❌ Could not connect to Spotify. Please check your network and credentials.")