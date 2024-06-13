import streamlit as st
import pyttsx3
import base64

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1
    
    # Save speech to bytes
    temp_file = "output2.mp3"
    engine.save_to_file(text, temp_file)
    engine.runAndWait()
    
    # Read the audio file as bytes
    with open(temp_file, "rb") as file:
        audio_bytes = file.read()

    return audio_bytes

def main():
    st.title("Text-to-Speech App")
    text = st.text_input("Enter the text you want to convert to speech")
    if st.button("Convert to Speech"):
        if text:
            audio_bytes = text_to_speech(text)
            st.audio(audio_bytes, format='audio/mp3', start_time=0)

if __name__ == "__main__":
    main()
