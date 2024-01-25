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

class call_number:
    
#   @tool("Dial a phone number")
    @staticmethod
    def call_number():
        """Calls phone number"""
        account_sid = 'ACea6a7def2b53a8ad97298f9ba69fccf8'
        auth_token = '7d1f0b090ec6cd9460786898798ee6dc'

        to_number = '+916280438234'
        from_number= '+16692023622'
    
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url='http://demo.twilio.com/docs/voice.xml'
        )
        return call.sid


