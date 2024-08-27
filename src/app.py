import streamlit as st
from google.cloud import translate_v2 as translate
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Initialize the Google Translate client with API key
translate_client = translate.Client()

# List of supported languages
SUPPORTED_LANGUAGES = {
    'en': 'English',
    'es': 'Spanish',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'zh': 'Chinese',
    'ja': 'Japanese',
    'ko': 'Korean',
    'hi': 'Hindi'
}

def translate_text(text, target='en'):
    """Translate text to the target language using Google Translate API."""
    result = translate_client.translate(text, target_language=target)
    return result['translatedText']

# Initialize session state for chat history if not already done
if 'history' not in st.session_state:
    st.session_state.history = []

# Streamlit app layout
st.title("Language Translator Chatbot")

# Select language
language = st.selectbox("Select your language:", list(SUPPORTED_LANGUAGES.keys()), format_func=lambda x: SUPPORTED_LANGUAGES[x])

# User input
user_input = st.text_input("Enter your query:")

# When the user submits a query
if st.button("Submit"):
    if user_input:
        # Translate the user input to English
        translated_text = translate_text(user_input, target='en')

        # Add user input and translated text to the history
        st.session_state.history.append(f"You: {user_input} ({SUPPORTED_LANGUAGES[language]})")
        st.session_state.history.append(f"Bot (translated to English): {translated_text}")

# Display the chat history
st.subheader("Chat History")
for message in st.session_state.history:
    st.write(message)
