import pyaudio
import requests




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

        print("Processing speech....")

        # Use the speech-to-text API
        API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
        headers = {"Authorization": "Bearer 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"}

        def query(data):
                response = requests.post(API_URL, headers=headers, files={"file": audio_data})
                return response.json()

        output = query(audio_data)

        print("You:", output)

        # Here, you can add your logic to process the result and generate a response

    except KeyboardInterrupt:
        # Break the loop if the user interrupts with Ctrl+C
        break

# Close the microphone stream
stream.stop_stream()
stream.close()
p.terminate()




