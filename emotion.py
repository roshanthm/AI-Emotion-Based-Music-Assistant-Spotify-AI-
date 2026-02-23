import torch
from transformers import pipeline

# Use a pre-trained model for emotion/sentiment analysis
# This model is fast and good for general sentiment analysis.
try:
    classifier = pipeline(
        'sentiment-analysis', 
        model='cardiffnlp/twitter-roberta-base-sentiment'
    )
except Exception as e:
    # Fallback in case of model download failure
    print(f"Warning: Failed to load AI model. Falling back to keyword search. Error: {e}")
    classifier = None

def get_emotion_from_sentiment(sentiment_label):
    """
    Maps the model's sentiment labels (LABEL_1=Positive, LABEL_0=Negative, LABEL_2=Neutral) 
    to your project's music categories.
    """
    # Note: RoBERTa models often output LABEL_0, LABEL_1, LABEL_2 
    # instead of text labels like 'positive'.
    
    if sentiment_label == 'LABEL_1' or sentiment_label.lower() == 'positive':
        return "happy"
    elif sentiment_label == 'LABEL_0' or sentiment_label.lower() == 'negative':
        # Negative sentiment maps to 'sad' for music selection
        return "sad" 
    elif sentiment_label == 'LABEL_2' or sentiment_label.lower() == 'neutral':
        # Neutral sentiment maps to 'calm' or background music
        return "calm"
    return "neutral"

def keyword_fallback(text):
    """The original keyword matching logic, used if the AI model fails."""
    text = text.lower()
    if any(word in text for word in ["sad", "depressed", "lonely"]):
        return "sad"
    if any(word in text for word in ["happy", "excited", "good", "great"]):
        return "happy"
    if any(word in text for word in ["tired", "stress", "calm", "chill", "relaxed"]):
        return "calm"
    return "neutral"


def detect_emotion(text):
    """
    Analyzes the input text using the Hugging Face sentiment model,
    or falls back to keyword matching if the model isn't loaded.
    """
    if not text.strip():
        return "neutral"
        
    if classifier:
        try:
            # Use the AI model
            result = classifier(text)[0]
            sentiment_label = result['label']
            emotion = get_emotion_from_sentiment(sentiment_label)
            
            print(f"AI Analysis: {sentiment_label} (Confidence: {result['score']:.2f})")
            return emotion
        
        except Exception as e:
            print(f"AI Model Error during inference: {e}. Falling back to keyword match.")
            return keyword_fallback(text)
    
    # If the classifier was never loaded, use the fallback
    print("Keyword Fallback Mode Active.")
    return keyword_fallback(text)