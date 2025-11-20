# 🎧 AI Emotion-Based Music Assistant  
### _AI that understands your mood and plays the perfect Spotify track._

This project is an intelligent, emotion-aware music companion that interacts with you, detects your mood, and automatically plays songs on Spotify that fit your emotional state.  

It combines **AI conversation**, **emotion classification**, and **Spotify playback** into one complete system — running fully on your local machine.

---

## 🚀 Features

- 🗣️ **Conversational mood detection**  
  AI asks how you feel and interprets your emotion intelligently.

- 🎵 **Spotify auto-play**  
  The assistant automatically selects and plays a track matching your mood.

- 🤝 **Secure OAuth authentication**  
  Uses official Spotify login (no unsafe methods).

- ⚡ Runs fully local  
  No servers, no backend – just Python + your Spotify account.

---

## 🛠️ Technologies Used

- **Python 3.10**
- **Spotipy** (Spotify Web API)
- **Hugging Face Transformers** (emotion classification / text processing)
- **dotenv** (safe secret management)
- **Spotify Developer App** (OAuth authentication)

---

## 📂 Project Structure

```
ai-music-emotion-assistant/
│
├── main.py              # Main execution logic
├── spotify.py           # Spotify authentication + playback functions
├── .env                 # Stores Spotify credentials (ignored in Git)
├── requirements.txt     # All dependencies
└── README.md            # Project documentation
```

---

## 🔧 Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/your-username/ai-music-emotion-assistant.git
cd ai-music-emotion-assistant
```

### 2. Create a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 4. Set Up Spotify Developer Credentials

1. Go to: https://developer.spotify.com/dashboard  
2. Create an app  
3. Add Redirect URI:

```
http://localhost:8888/callback
```

4. Copy:
   - Client ID  
   - Client Secret  

5. Create a `.env` file:

```
SPOTIPY_CLIENT_ID=YOUR_ID_HERE
SPOTIPY_CLIENT_SECRET=YOUR_SECRET_HERE
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback
```

---

## ▶️ Running the Assistant

```bash
python main.py
```

### The assistant will:

1. Greet you  
2. Ask how you feel  
3. Detect the emotion  
4. Open a Spotify login link  
5. Play the matching soundtrack on your active Spotify device  

---

## 📌 Supported Moods

- **happy**
- **sad**
- **relaxed**
- **angry**
- **energetic**

You can expand this easily.

---

## 🌟 Future Enhancements (optional for project report)

- Voice-based emotion detection  
- Real-time facial emotion detection (OpenCV)  
- Web dashboard  
- Playing full mood-based playlists  
- AI-generated music (MusicGen integration)

---

