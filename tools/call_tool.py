import os
from twilio.rest import Client
# from langchain.tools import tool
# from langchain_community.llms import HuggingFaceHub
from gradio_client import Client
# from langchain.chat_models import ChatLiteLLM
from dotenv import load_dotenv
import pyaudio
import speech_recognition as sr

import csv
import pandas as pd

load_dotenv()  # Remove redundant dotenv load

class CallNumber:
    
    # @tool("Dial a phone number")
    @staticmethod
    def make_call():
        """Calls a phone number"""
        account_sid = 'ACea6a7def2b53a8ad97298f9ba69fccf8'
        auth_token = '7d1f0b090ec6cd9460786898798ee6dc'

        to_number = '+916280438234'
        from_number = '+16692023622'
    
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            to=to_number,
            from_=from_number,
            url='http://demo.twilio.com/docs/voice.xml'
        )
        return call.sid

# Example usage:
# call_instance = CallNumber()
# call_instance.make_call()

    # @tool("Reads a number from a csv file")
    @staticmethod
    def read_number():
        """Reads names and numbers from a local CSV file"""
        # Replace the following line with the path to your contacts.csv file
        csv_file_path = "contacts.csv"

        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(csv_file_path)

        # Assuming the first column has names and the second column has numbers
        name_column = "Name"
        number_column = "Phone"

        # Extract names and numbers
        names = df[name_column].tolist()
        numbers = df[number_column].tolist()

        return names, numbers
