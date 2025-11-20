def detect_emotion(text):
    text = text.lower()

    if any(word in text for word in ["sad", "depressed", "lonely"]):
        return "sad"
    if any(word in text for word in ["happy", "excited", "good"]):
        return "happy"
    if any(word in text for word in ["tired", "stress", "overwhelmed"]):
        return "calm"

    return "neutral"
