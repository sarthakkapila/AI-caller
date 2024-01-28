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


# 🚨🚨🚨
# Needs a whole fix
# Need to figure out how can whisper hear what the client is saying while on the call

class STT:
    @staticmethod
    def speech_to_text():
        # Set up the microphone
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

        # Start the conversation loop
        while True:
            try:
                # Collect audio data in real-time
                audio_data = b""
                print("Listening...")

                for i in range(0, int(44100 / 1024 * 5)):  # Adjust the duration as needed
                    audio_data += stream.read(1024)

                print("Processing...")

                # Use Google Web Speech API for real-time transcription
                recognizer = sr.Recognizer()
                audio_text = recognizer.recognize_google(audio_data)

                print("You:", audio_text)

                # Here, you can add your logic to process the result and generate a response

            except KeyboardInterrupt:
                # Break the loop if the user interrupts with Ctrl+C
                break
            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"Error connecting to Google Web Speech API: {e}")

        # Close the microphone stream
        stream.stop_stream()
        stream.close()
        p.terminate()

# Uncomment the following line if you want to run the STT module
# STT.speech_to_text()