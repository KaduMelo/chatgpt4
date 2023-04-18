import os
import openai
openai.api_key = os.environ["OPENAI_API_KEY"]

audio_file = open('audio/german1.mp3', 'rb')
result = openai.Audio.transcribe('whisper-1', audio_file)

print(result)

# result = openai.Audio.translate('whisper-1', audio_file)

# print(result)

