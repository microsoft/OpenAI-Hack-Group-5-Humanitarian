
import os
import numpy as np
import streamlit as st
from io import BytesIO
import streamlit.components.v1 as components
import streamlit as st

from st_custom_components import st_audiorec
from scipy.io.wavfile import write
from footer import footer

#import whisper
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
language = 'en'
translator = Translator()


if __name__ == "__main__":

    st.title("AI-Powered Multi-Lingual Voice Assistant")

    st.markdown("I can answer questions about the WHO child mortality data.")
    st.markdown("You can ask me questions in Italian and I will respond in Italian.")
    st.markdown("Please enter your question in the text box below:")
   
    question = st.text_input('Question', '')
    if question:
        tquestion = translator.translate(question, src='it', dest='en')
        output = chain(tquestion.text)
        st.markdown(f"The LLM response is: {output}")
        answer = translator.translate(output['answer'], src='en', dest='it')

        st.markdown("Converting response to speech...")
        myobj = gTTS(text=answer.text, lang='it', slow=False)
        myobj.save("response.mp3")
        st.audio("response.mp3")
    
    footer()
