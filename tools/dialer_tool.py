import os
from twilio.rest import Client

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