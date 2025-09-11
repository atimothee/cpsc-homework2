source .env

curl https://api.openai.com/v1/audio/speech \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini-tts",
    "input": "This is the best class ever! Today is a wonderful day! Yale is a wonderful university!",
    "voice": "ballad",
    "instructions": "Speak in a cheerful and positive tone."
  }' \
  --output speech.mp3
