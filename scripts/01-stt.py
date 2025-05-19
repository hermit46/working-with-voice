import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("16649.mp3", "rb") as audio_file: #read binary file
  transcript: str = openai.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      response_format="text"
  )

  print(transcript)

  # > "So today I want to talk about the decision..."

# The following process happens:
# 1. Audio is uploaded to the provider
# 2. Provider processes the audio and returns a transcript
# 3. The transcript is returned to the client