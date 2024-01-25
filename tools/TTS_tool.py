import os
from gradio_client import Client

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