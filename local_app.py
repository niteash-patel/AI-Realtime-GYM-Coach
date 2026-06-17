import streamlit as st
from streamlit_webrtc import webrtc_streamer, WebRtcMode

st.title("🏋️ AI Gym Coach (Local Version)")

webrtc_streamer(
    key="gym",
    mode=WebRtcMode.SENDRECV,
    media_stream_constraints={"video": True, "audio": False}
)