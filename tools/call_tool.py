import os
from twilio.rest import Client

import csv
import pandas as pd

class CallNumber:
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
    
# Added max_calls to avoid too much api usage
    # @tool("Dial a phone number")
    @staticmethod
    def make_call(max_calls):
        """Calls a phone number"""
        account_sid = 'ACea6a7def2b53a8ad97298f9ba69fccf8'
        auth_token = '7d1f0b090ec6cd9460786898798ee6dc'
        
        names, numbers = CallNumber.read_number()

        client = Client(account_sid, auth_token)
        calls_made = 0

        for name, number in zip(names, numbers):
            if calls_made >= max_calls:
                print(f"Stopped making calls after {max_calls} calls.")
                break
            
            print(f"Calling {name} at {number}")
            call = client.calls.create(
                to=number,
                from_='+16692023622',
                url='http://demo.twilio.com/docs/voice.xml'
            )
            print(f"Call SID: {call.sid}")
            
            calls_made += 1
            
