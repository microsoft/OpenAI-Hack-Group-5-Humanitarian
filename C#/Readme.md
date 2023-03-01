# OpenAI Hack for Humanitarian causes

## Goal
The aim of this hackathon is to create a tool that can answer questions on World Health Organization (WHO) data. It should take in audio as input in the form of well structured questions and reply in accurate responses also in audio format. 
Adding speech as a frontend facilitates access to people who are visually impaired or to those who want to access information via their phone.

## Getting started with this notebook
1. You will need an OpenAI account and key.
2. You will need to create a [Speech resource](https://ms.portal.azure.com/#create/Microsoft.CognitiveServicesSpeechServices) which will be used for SpeechToText and TextToSpeech conversions.  
    - Get the speech resource key and region.

## Implementation details
This solution has been implemented in C# using the Semantic Kernel SDK library.

We present 3 different ways in which the data can be fed to the LLM model as context.
1. Raw data in Tabular form
2. Pre-processed data in Sentence form
    - The pre-processing step converts the tabular data into textual format. The columns of the dataset are concatenated using column descriptors into sentence form such that the information is captured. 
3. Directly calling into the WHO provided OData APIs https://www.who.int/data/gho/info/gho-odata-api 

### Solution flow

1. The tools prompts the user to ask a question which is recorded via the system microphone.

2. The system converts the speech input into text. This is done using the [Microsoft Cognitive Services SpeechToText SDK](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-speech-to-text). We now have a textual representation of the question.

3. The textual representation of the question is fed into the LLM model, along with the data set to provide context. In this case, we are using OpenAI's "text-davinci-003" model. The LLM model has been abstracted behind the [Semantic Kernel](https://microsoft.sharepoint.com/teams/semantic-kernel) library providing seamless integration to the APIs. Semantic Kernel (SK) is a lightweight SDK enabling integration of AI Large Language Models (LLMs) with conventional programming languages.

4. The QASkill prompt from SK has been modified and used for this scenario. You can find the prompt template [here](https://github.com/microsoft/OpenAI-Hack-Group-5-Humanitarian/blob/main/C%23/skills/QA_WHO_Skill/skprompt.txt)

5. The response from the LLM is converted back to audio format using [Microsoft Cognitive Services TTS SDK](https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/get-started-text-to-speech).
The response is accurate, well-structured and can be played back via the system speakers. 

## Future work

1. For the purpose of this Hack the dataset we are using is relatively small. As the data set increases we would quickly hit the token limit on the model. In order for this solution to be integrated into large scale applications we would need to add support to persist state and build both short term and long term memory. Semantic Kernels provide support for this using Volatile Memory store and Embeddings. You also have the option to plug into persistent storage like Azure CosmosDB, Postgre SQL etc. Semantic Memory provides the capability to index external data sources.

In a nutshell - the Semantic Kernel SDK provides a robust framework that empowers intelligent large scale applications to be seamlessly built leveraging all the functionality of the OpenAI models. 

## References
1. WHO GHO Source Dataset: https://www.who.int/data/gho/data/indicators/indicator-details/GHO/mortality-rate-for-5-14-year-olds-(probability-of-dying-per-1000-children-aged-5-14-years)
2. WHO GHO Data APIs: https://www.who.int/data/gho/info/gho-odata-api
3. Semantic Kernel SDK documentation: https://microsoft.sharepoint.com/teams/semantic-kernel
4. Semantic Kernel GitHub repo: https://github.com/microsoft/semantic-kernel
5. Microsoft Cognitive Services SDK: https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service
