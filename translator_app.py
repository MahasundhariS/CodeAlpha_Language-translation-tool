import streamlit as st
from googletrans import Translator
from gtts import gTTS

translator = Translator()

# Language dictionary
LANGUAGES = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "Telugu": "te",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

st.title("🌍 Language Translator App")

# Input text
text = st.text_area("Enter text here")

# Source & Target Language
source_lang = st.selectbox("Source Language", list(LANGUAGES.keys()))
target_lang = st.selectbox("Target Language", list(LANGUAGES.keys()))

# Translate
if st.button("Translate"):
    translated = translator.translate(
        text, src=LANGUAGES[source_lang], dest=LANGUAGES[target_lang]
    )
    st.subheader("Translated Text:")
    st.success(translated.text)

    # Convert to speech
    tts = gTTS(translated.text, lang=LANGUAGES[target_lang])
    audio_file = "translated_audio.mp3"
    tts.save(audio_file)

    # Play audio
    st.audio(audio_file, format="audio/mp3")

    # Download audio
    with open(audio_file, "rb") as f:
        st.download_button("Download Audio", f, file_name=audio_file, mime="audio/mp3")
