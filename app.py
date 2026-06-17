import streamlit as st
from gtts import gTTS
import io

st.title("🏋️ AI Gym Coach (Cloud Version)")

if "name" not in st.session_state:
    st.session_state.name = ""

st.session_state.name = st.text_input("Enter your name")

posture = st.selectbox("Posture", ["good", "ok", "bad"])

def speak(text):
    tts = gTTS(text=text, lang="en")
    audio = io.BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)
    return audio

def feedback(name, posture):
    if posture == "bad":
        return f"{name}, fix your posture!"
    elif posture == "ok":
        return f"{name}, you can improve!"
    return f"Excellent {name}!"

if st.button("Get Feedback"):
    msg = feedback(st.session_state.name, posture)
    st.success(msg)

    audio = speak(msg)
    st.audio(audio, format="audio/mp3")