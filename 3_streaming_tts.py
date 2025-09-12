from dotenv import load_dotenv, dotenv_values
import os
from pathlib import Path
from openai import OpenAI
import random

load_dotenv()
if os.getenv("OPENAI_API_KEY") is not None:
    print("Found environment variable for OPENAI_API_KEY")
else:
    print("Environment variable for OPENAI_API_KEY not found")

client = OpenAI()


def text_to_audio(voice, text, tone_and_style_instructions, file_path="speech3_python.mp3"):
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice=voice,
        input=text,
        instructions=tone_and_style_instructions,
    ) as response:
        response.stream_to_file(file_path)



VOICES = ["alloy", "ballad", "fable", "nova"]

INSTRUCTIONS = [
    "Speak in a cheerful and positive tone.",
    "Speak in a deep and serious tone.",
    "Speak in a calm and soothing tone.",
    "Speak in an excited and energetic tone.",
]
with open("poem.txt", "r") as file:
   lines = file.readlines()
   for i,text in enumerate(lines[:3]):
    voice = random.choice(VOICES)
    instruction = random.choice(INSTRUCTIONS)
    file_extension = str(i)+"speech_python_"+voice+".mp3"
    speech_file_path = Path(__file__).parent / file_extension
    text_to_audio(voice, text, instruction, speech_file_path)