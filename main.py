from spotify import create_spotify_client, play_track

emotion_tracks = {
    "happy": "spotify:track:2nGFzvIC3F1o2Y6XG9kM0i",
    "sad": "spotify:track:5hTpBe8h35rJ67eAWHQsJx",
    "calm": "spotify:track:0VjIjW4GlUZAMYd2vXMi3b",
    "angry": "spotify:track:2b8fOow8UzyDFAE27YhOZM"
}

print("\n🎧 Welcome to your AI Emotion Music Assistant!\n")

emotion = input("How are you feeling today?\n➡ ").lower()

if emotion not in emotion_tracks:
    print("❌ Sorry, I don’t have music for that emotion yet.")
else:
    print(f"\n🧠 Emotion detected: {emotion}")
    print(f"🎵 Playing music for your mood: {emotion}")

    sp = create_spotify_client()
    play_track(sp, emotion_tracks[emotion])
