# OpenAI Hack for Humanitarian Causes

## Goal
Create a tool for visually-impaired individuals that can answer questions on World Health Organization (WHO) Global Health Observatory (GHO) datasets, which are typically tabular in nature. This tool should accept factual questions from natural speech (e.g audio recorded from a mic), query an appropriate dataset, and provide accurate, verifiable responses. The responses should be presented in audio format.

As an extension, the tool can accept questions in languages other than English and respond in the same language.

## Solution Summary
The code in this folder provides an end-to-end Python solution that meets the goal. The solution makes use of open-source Python packages, does not require a lot of compute and is portable. For instance, it can be run for free in the cloud using Google Colab. The only cost for running the code would be the charges for using the OpenAI API for running the queries.

A web app for direct interaction that can be hosted in the cloud is also provided.

## Solution Details
This solution comprises the following steps.

* Extract the data from the WHO GHO website: we demonstrate three ways to do this:
    - using web scraping tools
    - using the GHO ODATA API: The list of indicators that can be queried can be seen here: https://ghoapi.azureedge.net/api/Indicator. For this prototype, we focussed on `CHILDMORT5TO14` which provides child mortality rates for 5-14 year olds, by country and by year.
    - manually downloading from the WHO GHO website by exporting it to CSV format

* Convert the tabular data into textual format. Here we concatenate the columns of the dataset using column descriptors into a sentence that captures the information in the columns of interest. These sentences are then further concatenated to create our training dataset. For the initial prototype, we use a very tiny training dataset consisting of just five rows in the data table. We will discuss how to handle the full dataset in the future extensions section.

* Provide a means to feed in a question from a microphone. We do this by providing an audio recording widget. The audio captured for the question is saved in WAV format.

* Transcribe the audio file to text (perform speech-to-text conversion). This is done using the excellent and free OpenAI `whisper` library, which is very accurate and handles speaker accents quite well. We now have a textual representation of the question. For non-English questions, translation can also be performed using Whisper.

* Generate an appropriate prompt combining the training data and the question and pass it to the large language model (LLM). In our case, we use OpenAI's text-davinci-003 model. We use the `langchain` package to simplify our interactions with the LLM.

* The LLM correctly answers our question. We take the text response of the LLM (the responses can be translated into another language using Google Translate) and convert it to audio using the gTTS (Google Translate Text-to-Speech) library. The resulting .mp3 file can be played over the speakers.

## Web App Implementation
We have created a web app that has interactive widgets to select a language, record the question, feed the question to the LLM and play the audio response. This web app is built using the Streamlit library. 

## Handling Large Source Datasets
In the initial approach prototyped in the notebook, the entire training dataset is provided within the prompt. This obviously cannot scale as the dataset size increases, since the LLMs currently available via API can handle only 2047 tokens (about 3000 words)

The solution for this is to convert the training dataset into an embedding format. This can be done using the low-cost OpenAI model `text-embedding-ada-002` or for free using `hkunlp/instructor-large` model, available from HuggingFace.

These embeddings can be stored as indexed vectorstore. For question-answering, we do a cosine similarity search between the embedding generated from the question with the stored embeddings, take the top-ranking embedding and use the Open AI model to generate a response using this embedding. This approach allows us to base answers on a dataset of our choice, and provide accurate and verifiable responses. We do this using the langchain library. With this approach we can point to the exact reference within our dataset where the answer is found and the LLM does not "hallucinate" the answer. If the answer cannot be found in any of the embeddings, it simply says "it does not know the answer".

## Code Layout
* Python directory has a jupyter notebook `openai_hackathon_humanitarian.ipynb` which details all the steps in developing this solution.
* app subdirectory has the Streamlit web apps:
    - app.py: app which takes input from mic, uses a small training set and outputs audio.
    - app_nomic.py: modification of app.py that runs remotely. Streamlit by default runs on a non-https port, when run remotely, most browsers block mic access if not running https. So in this version, the question has to be entered as text.
    - app_embed.py: extension of app_nomic.py that uses embeddings. This is trained on the 2019 WHO child mortality data for all countries. The app supports questions and basic reasoning over all the data.
    - app_embed_lang.py: extension of app_embed.py that takes in text questions in Italian and produces audio responses in Italian
    - app_embed_lang_nomic.py: extension of app_embed_lang.py that can take in questions in audio (English, Spanish, Italian) and respond in audio in the same language. Has to be run locally because of the browser limitation with mic acess from a remote site without https.
* requirments.txt: lists all the libraries needed to run this code. Recommend running with Python 3.9 in a Conda environment.

## App Deployment
* Prerequisite: MacOS or Linux host with Python & Conda
* Create a Conda environment
* Install the requirements
* Provide OpenAI API key
* Run the app:
```
cd Python/app
conda create -y -n openai_hack python=3.9
conda activate openai_hack
pip install -r requirements.txt
export OPENAI_API_KEY = <your-api-key>
streamlit run <app.py>
```
* A docker image can be created for portability, if desired

## Usage Costs
* Speech-to-Text API: `whisper` $0.006 / min (rounded to nearest second). Whisper can also be used for language translation.
* OpenAI Large Language Model:
    - `text-davinci-003`: $0.12 / 1K tokens. This model is used for question-answering. This API will comprise the bulk of the cost of this app. We can explore performance with lower cost models. The chatGPT models are also available now, and they supposedly 10x cheaper than our current model.
    - `text-embedding-ada-002`: $0.0004 per 1000 tokens. This model is used to generate embeddings of your private dataset. The cost translates to ~$1 for 3000 pages of text. There is a free model (hkunlp instructor embedding) that provides comparable performance that could be an alternative.
* Text-to-Speech and Translation API: we used Google Translate which is free.
* Costs for app hosting/storage, not substantial. Generation and usage of embeddings does not require heavy compute. It can be run on the lowest-tier cloud VM.
* The Azure Cognitive Services API can also be used for speech-to-text transcription/translation and for text-to-speech conversion with translation.

# To Do:
* Use newer ChatGPT API
* Use Instruct Embeddings instead of Ada
* Build dockerized version of app

## References
1. WHO GHO Source Dataset: https://www.who.int/data/gho/data/indicators/indicator-details/GHO/mortality-rate-for-5-14-year-olds-(probability-of-dying-per-1000-children-aged-5-14-years)
2. WHO GHO APO: https://www.who.int/data/gho/info/gho-odata-api
3. WHO GHO Available Indicators: https://ghoapi.azureedge.net/api/Indicator
4. OpenAI Whisper: https://openai.com/research/whisper
5. OpenAI LLMs: https://platform.openai.com/docs/api-reference/completions/create
5. LangChain: https://langchain.readthedocs.io/en/latest/index.html
6. LangChain Embeddings Approach for Question-Answering: https://langchain.readthedocs.io/en/latest/modules/indexes/getting_started.html
7. Instructor Embeddings: https://instructor-embedding.github.io/
6. gTTS (Google Translate's Text-To-Speech API): https://gtts.readthedocs.io/en/latest/index.html

