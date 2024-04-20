import json
import time

from components.voice_processing import command
from components.promt_processing import console_chat
from components.audio_processing import speechAudio

def writejson(chat_history, audioUrl):
    print("chat_history:", chat_history)
    
    for message in chat_history:
        print("Тип данных content:", type(message["content"]))

    unx_time = int(time.time())

    # Извлекаем нужные данные из chat_history (предполагаем, что это список)
    chat_data = [
        {"role": message["role"], "content": message["content"]} 
        for message in chat_history
    ]

    result_form = {
        "title": unx_time,
        "chat": chat_data,
        "audioUrl": audioUrl if audioUrl else None 
    }

    with open(f".\data\json\{unx_time}.json", 'w', encoding="utf-8") as file:
        json.dump(result_form, file, indent=4, ensure_ascii=False)
    
    print(result_form)

def main():
    print('''Выберите принцип работы:
          
    1. Озвучить ответ
    2. Не озвучивать ответ
    ''')
    
    while True:
        try:
            answer = int(input("Выбор: "))
            if answer in [1, 2]:
                break
            else:
                print("Пожалуйста, выберите 1 или 2.")
        except ValueError:
            print("Пожалуйста, введите число.")

    print('''Выберите способ ввода промта:
          
    1. Написать текст вручную
    2. Произнести промт словами
    ''')

    while True:
        try:
            input_method = int(input("Выбор: "))
            if input_method in [1, 2]:
                break
            else:
                print("Пожалуйста, выберите 1 или 2.")
        except ValueError:
            print("Пожалуйста, введите число.")

    if input_method == 1:
        promt = input("Введите промт: ")
    else:
        promt = command()

    chat_history = console_chat(promt)

    if answer == 1:
        audio = speechAudio(chat_history)
    else:
        audio = None

    writejson(chat_history, audio)

if __name__ == "__main__":
    main()
    