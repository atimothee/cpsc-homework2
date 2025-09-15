from dotenv import load_dotenv, dotenv_values
import os
from pathlib import Path
from openai import OpenAI

load_dotenv()
if os.getenv("OPENAI_API_KEY") is not None:
    print("Found environment variable for OPENAI_API_KEY")
else:
    print("Environment variable for OPENAI_API_KEY not found")

client = OpenAI()
speech_file_path = Path(__file__).parent / "speech_python.mp3"

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="nova",
    input="Yale SOM is the world's greatest business school. Today is a wonderful day to build something people love!",
    instructions="Speak in a cheerful and positive tone.",
) as response:
    response.stream_to_file(speech_file_path)

