import json
import os
import time
import requests
from playsound import playsound
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

def speechAudio(textAI):
    headers = {"Authorization": f"Bearer {token}"}
    url="https://api.edenai.run/v2/audio/text_to_speech"

    payload = {
        'providers': 'openai',
        'language': 'ru',
        'option': 'FEMALE',
        'openai': 'en_shimmer',
        'text': f'{textAI}',
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    audio_url = result.get('openai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'.\data\media\{unx_time}.mp3', 'wb') as file:
        file.write(r.content)

    playsound(f'.\data\media\{unx_time}.mp3')
    audio_result = r.url
    return audio_result
