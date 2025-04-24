#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import time
from pydub import AudioSegment
from pydub.playback import play
import threading

# Charger le son du métronome
clique = AudioSegment.from_file("clique.wav")  # Assure-toi que tu as un fichier 'clique.wav' pour le son du métronome

# Fonction du métronome
def metronome(tempo):
    interval = 60 / tempo  # Calcul du temps entre chaque battement en secondes
    while True:
        play(clique)  # Joue le son du métronome
        time.sleep(interval)  # Pause entre les battements

# Fonction principale Streamlit
def main():
    st.title("Métronome")

    # Choisir le tempo
    tempo = st.slider("Choisis le tempo (BPM)", min_value=40, max_value=220, value=120, step=1)

    # Bouton pour démarrer le métronome
    if st.button("Démarrer le Métronome"):
        st.write(f"Métronome à {tempo} BPM")
        threading.Thread(target=metronome, args=(tempo,)).start()

if __name__ == "__main__":
    main()

