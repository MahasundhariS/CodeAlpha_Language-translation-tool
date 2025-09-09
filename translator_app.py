import streamlit as st
from googletrans import Translator
from gtts import gTTS
import os

st.title("🌍 English ↔ Tamil Translator with Voice")

# Input text
text = st.text_area("Enter text:")

# Language selection
option = st.selectbox("Choose translation direction:", 
                      ("English → Tamil", "Tamil → English"))

if st.button("Translate"):
    translator = Translator()
    
    if option == "English → Tamil":
        translated = translator.translate(text, src="en", dest="ta")
    else:
        translated = translator.translate(text, src="ta", dest="en")
    
    st.write("### ✅ Translated Text:")
    st.success(translated.text)

    # Save audio
    tts = gTTS(translated.text, lang="ta" if option == "English → Tamil" else "en")
    tts.save("output.mp3")
    st.audio("output.mp3")
