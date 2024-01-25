import os
from twilio.rest import Client
# from langchain.tools import tool
# from langchain_community.llms import HuggingFaceHub
from gradio_client import Client
# from langchain.chat_models import ChatLiteLLM
from dotenv import load_dotenv
import pyaudio
import speech_recognition as sr

from dotenv import load_dotenv
load_dotenv() # make sure you have .env file with your API keys, eg., OPENAI_API_KEY=sk-xxx

# Use microsoft/speecht5_tts if this api doesn't work 

class TTS:

#   @tool("Text to Speech tool")
    @staticmethod
    def TTS(text, file_path, voice, second_voice, split_by_newline):
        """Converts text to speech"""
        client = Client("https://manmay-tortoise-tts.hf.space/")
        result = client.predict(
            text,
            file_path,
            voice,
            second_voice,
            split_by_newline,
            api_name="/predict" 
                
#                                   TESTING   
# # Example of using the TTS method
# text_to_convert = "Hey this is Emily from XYZ productions, Is this mr. Kevin talking?!"
# file_path_or_url = "example.txt"
# voice_option = "angie,angie"
# second_voice_option = "angie,angie"
# split_by_newline_option = "Yes"
            )
            # print(result)
