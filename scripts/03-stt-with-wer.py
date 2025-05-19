import os

import openai
from jiwer import wer
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

with open("audio.mp3", "rb") as audio_file: #read binary file
  transcript: str = openai.audio.transcriptions.create(
      model="whisper-1",
      file=audio_file,
      response_format="text"
  )

# > reference = "So today I talked about the decision..."
# > transcript = "So today I want to talk about the decision..."

error = wer(reference, transcript)

print(error)
# > 0.1