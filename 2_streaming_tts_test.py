from openai import AsyncOpenAI
import asyncio
import openai
from openai.helpers import LocalAudioPlayer
import os
from dotenv import load_dotenv


load_dotenv()
if os.getenv("OPENAI_API_KEY") is not None:
    print("Found environment variable for OPENAI_API_KEY")
else:
    print("Environment variable for OPENAI_API_KEY not found")

client = AsyncOpenAI()

async def text_to_audio(text, tone_and_style_instructions):

  async with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input=text,
    instructions=tone_and_style_instructions,
    response_format="pcm",
  ) as response:
    await LocalAudioPlayer().play(response)

with open("poem.txt", "r") as file:
   text = file.read()
   asyncio.run(text_to_audio(text, "Speak in a cheerful and positive tone."))