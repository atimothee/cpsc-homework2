from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()
if os.getenv("OPENAI_API_KEY") is not None:
    print("Found environment variable for OPENAI_API_KEY")
else:
    print("Environment variable for OPENAI_API_KEY not found")

