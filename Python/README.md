# OpenAI Hack for Humanitarian Causes

## Goal
Create a tool that can answer questions on World Health Organization (WHO) Global Health Observatory (GHO) datasets, which are typically tabular in nature. This tool should accept factual questions from natural speech (e.g audio recorded from a mic), query an appropriate dataset, and provide accurate, verifiable responses. The responses should be presented in audio format.

## Solution Summary
The code in this folder provides an end-to-end Python solution that meets the goal. The solution makes use of open-source Python packages, does not require a lot of compute and is portable. For instance, it can be run for free in the cloud using Google Colab. The only cost for running the code would be the charges for using the OpenAI API for running the queries.

## Solution Details
This solution comprises the following steps.

* Extract the data from the WHO GHO website: we demonstrate three ways to do this:
- using web scraping tools
- using the GHO ODATA API: The list of indicators that can be queried can be seen here: https://ghoapi.azureedge.net/api/Indicator. For this prototype, we focussed on `CHILDMORT5TO14` which provides child mortality rates for 5-14 year olds, by country and by year.
- manually downloading from the WHO GHO website by exporting it to CSV format

* Convert the tabular data into textual format. Here we concatenate the columns of the dataset using column descriptors into a sentence that captures the information in the columns of interest. This sentences are then further concatenated to create our training dataset. For the initial prototype, we use a very tiny training dataset consisting of just five rows in the data table. We will discuss how to handle the full dataset in the future extensions section.

* Provide a means to feed in a question from a microphone. We do this by providing an audio recording widget. The audio captured for the question is saved in WAV format.

* Transcribe the audio file to text (perform speech-to-text conversion). This is done using the excellent and free OpenAI `whisper` library, which is very accurate and handles speaker accents quite well. We now have a textual representation of the question.

* Generate an appropriate prompt combining the training data and the question and pass it to the large language model (LLM). In our case, we use OpenAI's text-davinci-003 model. We use the `langchain` package to simplify our interactions with the LLM.

* The LLM correctly answers our question. We take the text response of the LLM and convert it to audio using the gTTS (Google Translate Text-to-Speech) library. The resulting .mp3 file can be played over the speakers.

## Future Extensions 1 (Web App)
Create a web app that has interactive widgets to record the question, feed the question to LLM and play the audio response. We will build this web app using the Streamlit library. 

## Future Extensions 2 (Handling Large Source Datasets)
The approach shown here where the entire training dataset is provided within the prompt obviously cannot scale as the dataset size increases, since the LLMs currently available via API can handle only 2047 tokens. 

The solution for this is to convert the training dataset into an embedding format. This can be done using the low-cost OpenAI model `text-embedding-ada-002` or for free using `hkunlp/instructor-large` model, available from HuggingFace.

These embeddings can be stored as indexed vectorstore. For question-answering, we do a cosine similarity search between the embedding generated from the question with the stored embeddings, take the top-ranking embedding and use the Open AI model to generate a response using this embedding. This approach allows us to base answers on a dataset of our choosing, and provide accurate and verifiable responses. We do this using the langchain library. With this approach we can point to the exact reference within our dataset where the answer is found and the LLM does not "hallucinate" the answer. If the answer cannot be found in any of the embeddings, it simply says "it does not know the answer".

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

