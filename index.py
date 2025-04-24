import streamlit as st
import time

st.set_page_config(page_title="Métronome", layout="centered")

st.title("🕒 Métronome")

tempo = st.slider("🎵 Tempo (BPM)", 40, 220, 120)
start = st.button("Démarrer le Métronome")

# Lecture du fichier audio
with open("clique.wav", "rb") as f:
    audio = f.read()

# Métronome simple : lecture d'un nombre fixe de battements
if start:
    st.success(f"Démarrage du métronome à {tempo} BPM")
    interval = 60.0 / tempo
    placeholder = st.empty()

    for i in range(20):  # Joue 20 battements
        placeholder.audio(audio, format="audio/wav")
        time.sleep(interval)


