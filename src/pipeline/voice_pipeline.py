from resemblyzer import VoiceEncoder,preprocess_wav
import numpy as np
import io #helps to load audio files in Librosa
import librosa 
import streamlit as st

@st.cache_resource
def load_voice_encoder():
    return VoiceEncoder

def get_voice_embedding(audio_bytes):
    try:
        encoder = load_voice_encoder()
        audio,sr = librosa.load(io.BytesIO(audio_bytes),sr=16000)
        wav = preprocess_wav(audio)
        embedding = encoder.embed_utterance(wav)
        return embedding.tolist()
    except Exception as e:
        st.error('Voice Recognition Error')
        return None


