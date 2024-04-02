import streamlit as st
import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed percent (can go over 100)
    engine.setProperty('volume', 0.9)  # Volume 0-1

    # Synthesize speech
    engine.save_to_file(text, 'output.mp3')

    # Run the engine (only needed if not running inside a GUI)
    engine.runAndWait()

def main():
    st.title("Text-to-Speech App")
    text = st.text_input("Enter the text you want to convert to speech")
    if st.button("Convert to Speech"):
        if text:
            text_to_speech(text)
            st.audio('output.mp3', format='audio/mp3')

if __name__ == "__main__":
    main()

