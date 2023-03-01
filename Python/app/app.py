import streamlit as st

from st_custom_components import st_audiorec
import numpy as np
from scipy.io.wavfile import write
from footer import footer

import whisper
import warnings
warnings.filterwarnings('ignore')

import os
import requests
import json
import pandas as pd
from langchain.llms import OpenAI
from gtts import gTTS

os.environ["OPENAI_API_KEY"] = "<your-api-key>"
model = whisper.load_model("base")
df = pd.read_csv('../mortality_data.csv')
# concatenate values from first 5 rows of column 'text'
train_data = df['TextValue'][0:5].str.cat(sep='. ')
llm = OpenAI(temperature=0)
language = 'en'


if __name__ == "__main__":

    st.title("AI-Powered QA Voice Assistant")

    st.markdown("I can answer questions about the WHO child mortality data.")
    st.markdown("Record your question using the Start / Stop buttons below. Press Reset before asking a new question.")

    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        st.markdown("Audio data captured from microphone.")
   
        data = np.frombuffer(wav_audio_data, dtype=np.int16)
        write("example.wav", 88200, data)
        st.markdown("Audio data saved as WAV file.")
                
        result = model.transcribe("example.wav")
        question = result["text"]
        st.markdown(f"Your question has been transcribed as: **{question}**")

        prompt = f"""
Use only the dataset provided to answer the question. 

Dataset: {train_data} 

Question: {question}"""

        output = llm(prompt)
        st.markdown(f"The response from our model is: **{output}**")

        st.markdown("Converting response to speech. Listen to it using the audio player below.")
        myobj = gTTS(text=output, lang=language, slow=False)
        myobj.save("response.mp3")
        st.audio("response.mp3")
    
    footer()