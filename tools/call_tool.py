import os
from twilio.rest import Client
import json
import csv
import pandas as pd
import time

from dotenv import load_dotenv
load_dotenv()  

class CallNumber:
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
        Phone = df[number_column].tolist()

        return names, Phone
    
    def make_call():
        """Calls a phone number"""
        account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        
        names, numbers = CallNumber.read_number()

        client = Client(account_sid, auth_token)
        calls_made = 0
        logs = "logs.json"

        for name, number in zip(names, numbers):
            print(f"Calling {name} at {number}")
            
            try:
                call = client.calls.create(
                    to=number,
                    from_='+16692023622',
                    url='http://demo.twilio.com/docs/voice.xml'
                )
                print(f"Call SID: {call.sid}")
                calls_made += 1
            except Exception as e:
                print(f"Error calling {name} at {number}: {str(e)}")
                continue
            
            while call.CallStatus not in ['completed', 'busy', 'canceled', 'no-answer', 'failed']:
                time.sleep(1) 
            
            with open(logs, 'a') as json_file:
                json.dump(call.sid, json_file)
                json_file.write('\n')


        print("All numbers dialed, total calls made:", calls_made)