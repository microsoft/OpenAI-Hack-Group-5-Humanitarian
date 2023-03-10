
import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components
import streamlit as st

from st_custom_components import st_audiorec
from scipy.io.wavfile import write
from footer import footer

import whisper
import warnings
warnings.filterwarnings('ignore')

from googletrans import Translator

import requests
import json
import pandas as pd
import faiss
import pickle
from langchain.llms import OpenAI
from langchain.chains import VectorDBQAWithSourcesChain
from gtts import gTTS

#os.environ["OPENAI_API_KEY"] = "<your-api-key>"#

index = faiss.read_index("docs.index")
with open("faiss_store.pkl", "rb") as f:
    store = pickle.load(f)

store.index = index
chain = VectorDBQAWithSourcesChain.from_llm(llm=OpenAI(temperature=0), vectorstore=store)
translator = Translator()
model = whisper.load_model("base")
src_dict = {"English": "en", "Italian": "it", "Spanish": "es"}


if __name__ == "__main__":

    st.title("Multi-Lingual AI Voice QA Assistant")

    st.markdown("I can answer questions about the WHO child mortality data. You can ask me questions in English, Italian or Spanish.")
    st.markdown("Record your question using the Start / Stop buttons below. Press Reset before asking a new question.")

    lang = st.radio("Source language:", ("English", "Italian", "Spanish"), horizontal=True)
    src = src_dict[lang]
    
    wav_audio_data = st_audiorec()
    if wav_audio_data is not None:
        st.markdown("Audio data captured from microphone.")
   
        data = np.frombuffer(wav_audio_data, dtype=np.int16)
        write("example.wav", 88200, data)
        st.markdown("Audio data saved as WAV file.")
                
        #result = model.transcribe("example.wav")
        os.system(f"whisper --model tiny --language {src} --task transcribe --output_format json example.wav")
        my_json = json.load(open('example.json'))
        question = my_json["text"]
        st.markdown(f"Your question has been transcribed as: **{question}**")
   
        if src != "en":
            tquestion = translator.translate(question, src='it', dest='en')
            question = tquestion.text

        output = chain(question)
        st.markdown(f"The LLM response is: {output}")

        if src != "en":
            tanswer = translator.translate(output['answer'], src='en', dest='it')
            answer = tanswer.text
        else:
            answer = output['answer']

        st.markdown("Converting response to speech...")
        myobj = gTTS(text=answer, lang=src, slow=False)
        myobj.save("response.mp3")
        st.audio("response.mp3")
    
    footer()
