import json
import os
import time
import requests
from playsound import playsound
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

def speechAudoi(textAI):
    headers = {"Authorization": f"Bearer {token}"}
    url="https://api.edenai.run/v2/audio/text_to_speech"

    payload = {
        'providers': 'openai',
        'language': 'ru',
        'option': 'MALE',
        'openai': 'ru_alloy',
        'text': f'{textAI}',
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    unx_time = int(time.time())

    with open(f'.\data\json\{unx_time}.json', 'w') as file:
        json.dump(result, file , indent=4, ensure_ascii=False)

    audio_url = result.get('openai').get('audio_resource_url')
    r = requests.get(audio_url)

    with open(f'.\data\media\{unx_time}.mp3', 'wb') as file:
        file.write(r.content)

    playsound(f'.\data\media\{unx_time}.mp3')
