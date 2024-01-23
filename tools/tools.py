import os
from twilio.rest import Client
from langchain.tools import tool
from langchain_community.llms import HuggingFaceHub
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


#   @tool("Text to Speech tool")
    @staticmethod
    def TTS():
        """Converts text to speech"""
        client = Client("https://manmay-tortoise-tts.hf.space/")
result = client.predict(
				"Howdy!",	# str in 'Text (Provide either text, or upload a newline separated text file below):' Textbox component
				"https://github.com/gradio-app/gradio/raw/main/test/test_files/sample_file.pdf",	# str (filepath or URL to file)
								# in 'Upload a text file' File component
				"angie,angie",	# str (Option from: [('angie', 'angie'), ('deniro', 'deniro'), ('freeman', 'freeman'), ('halle', 'halle'), ('lj', 'lj'), ('myself', 'myself'), ('pat2', 'pat2'), ('snakes', 'snakes'), ('tom', 'tom'), ('daws', 'daws'), ('dreams', 'dreams'), ('grace', 'grace'), ('lescault', 'lescault'), ('weaver', 'weaver'), ('applejack', 'applejack'), ('daniel', 'daniel'), ('emma', 'emma'), ('geralt', 'geralt'), ('jlaw', 'jlaw'), ('mol', 'mol'), ('pat', 'pat'), ('rainbow', 'rainbow'), ('tim_reynolds', 'tim_reynolds'), ('atkins', 'atkins'), ('dortice', 'dortice'), ('empire', 'empire'), ('kennard', 'kennard'), ('mouse', 'mouse'), ('william', 'william'), ('jane_eyre', 'jane_eyre'), ('random', 'random')])
								# in 'Select voice:' Dropdown component
				"angie,angie",	# str (Option from: [('angie', 'angie'), ('deniro', 'deniro'), ('freeman', 'freeman'), ('halle', 'halle'), ('lj', 'lj'), ('myself', 'myself'), ('pat2', 'pat2'), ('snakes', 'snakes'), ('tom', 'tom'), ('daws', 'daws'), ('dreams', 'dreams'), ('grace', 'grace'), ('lescault', 'lescault'), ('weaver', 'weaver'), ('applejack', 'applejack'), ('daniel', 'daniel'), ('emma', 'emma'), ('geralt', 'geralt'), ('jlaw', 'jlaw'), ('mol', 'mol'), ('pat', 'pat'), ('rainbow', 'rainbow'), ('tim_reynolds', 'tim_reynolds'), ('atkins', 'atkins'), ('dortice', 'dortice'), ('empire', 'empire'), ('kennard', 'kennard'), ('mouse', 'mouse'), ('william', 'william'), ('jane_eyre', 'jane_eyre'), ('random', 'random')])
								# in '(Optional) Select second voice:' Dropdown component
				"Yes",	# str in 'Split by newline (If [No], it will automatically try to find relevant splits):' Radio component
				api_name="/predict"
)
return result    