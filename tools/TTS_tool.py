import requests

# Finally decided to go with elven labs because it offers like 10k chracters for free i.e. around 10 calls.
# The high level code is loaded just need to add a way for the llm to communicate with this part of code
# And this part of code to send audio as well that through twilio.

class TextToSpeech:
    @staticmethod
    def generate_audio():
        """Generates audio using the Eleven Labs Text-to-Speech API"""
        url = "https://api.elevenlabs.io/v1/text-to-speech/<voice-id>"

        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": "<xi-api-key>"
        }

        data = {
            "text": "Born and raised in the charming south, "
                    "I can add a touch of sweet southern hospitality "
                    "to your audiobooks and podcasts",
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        response = requests.post(url, json=data, headers=headers)
        
        CHUNK_SIZE = 1024
        
        with open('output.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

