import requests
import os
from elevenlabs import Voice, VoiceSettings, generate, set_api_key

from dotenv import load_dotenv
load_dotenv()

from tools.LLM_tool import LLM.Sales_GPT
set_api_key(os.getenv("ELEVENLABS_API_KEY"))

class TextToSpeech:
    def generate_audio(text):
        """Generates audio using the Eleven Labs Text-to-Speech API"""
        # Calling the LLM func. to get text
        text = LLM()
        
        voice = Voice(
            voice_id = '',
            settings = VoiceSettings(
            stability = 0.71, 
            similarity_boost = 0.5,
            style = 0.0,
            use_speaker_boost = True)
        )
        audio = generate(
            # Need to get this text from LLM model
            text = text,
            voice = voice
            )
        # Play this audio to twilio call
        play(audio)
# TESTING
# TextToSpeech.generate_audio()