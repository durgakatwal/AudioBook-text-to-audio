import os
import streamlit as st
from gtts import gTTS

# Directories for uploaded files and generated audio files
UPLOAD_FOLDER = 'uploads'
OUTPUT_FOLDER = 'output'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Function to convert text to audiobook using gTTS
def convert_text_to_audio(text, output_path):
    tts = gTTS(text=text, lang='en')
    tts.save(output_path)

# Streamlit app
st.title("Text to Audiobook Converter")

# Upload file section
uploaded_file = st.file_uploader("Choose a text file", type="txt")

if uploaded_file is not None:
    # Read the uploaded text file
    text = uploaded_file.read().decode("utf-8")

    # Display the text for user confirmation
    st.text_area("Text from the file", text, height=200)

    # Button to convert text to audiobook
    if st.button("Convert to Audiobook"):
        # Generate audiobook
        output_file = os.path.join(OUTPUT_FOLDER, "audiobook.mp3")
        convert_text_to_audio(text, output_file)

        # Provide a download link for the generated audiobook
        with open(output_file, "rb") as audio_file:
            audio_bytes = audio_file.read()
            st.download_button("Download Audiobook", data=audio_bytes, file_name="audiobook.mp3", mime="audio/mpeg")
