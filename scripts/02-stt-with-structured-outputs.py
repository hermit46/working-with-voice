import os

import instructor
import openai
from dotenv import load_dotenv
from instructor.multimodal import Audio
from openai import OpenAI
from pydantic import BaseModel, Field

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class AudioSnippet(BaseModel):
    title: str = Field(
        ..., description="Concise and descriptive title of the video"
    )
    transcript: str = Field(
        ..., description="Transcript of the video"
    )
    summary: str = Field(
        ..., description="A brief summary of the video's content"
    )
    speakers: list[str] = Field(
        ...,
        description="List of speakers in the video"
    )
    key_points: list[str] = Field(
        ...,
        description="List of key points in the video"
    )

client = instructor.from_openai(OpenAI())

response = client.chat.completions.create(
    model="gpt-4o-audio-preview",
    response_model=AudioSnippet,
    modalities=["text"],
    audio={"voice": "alloy", "format": "wav"},
    messages =[
        {
            "role": "user",
            "content": [
                "Extract the following information from the audio",
                Audio.from_path("local/audio.wav")
            ]
        }
    ]
)

print(response)
