import os
from twilio.rest import Client
# from langchain.tools import tool
# from langchain_community.llms import HuggingFaceHub
from gradio_client import Client


class Tools:
    
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

# Use microsoft/speecht5_tts if this api doesn't work 

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


#   @tool("Speech to text")
    @staticmethod
    def SST():
        """Converts speech to text"""
        
#   @tool("")
    @staticmethod
    def LLM():
        """ """