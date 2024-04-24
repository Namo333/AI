import os
from g4f.client import Client
import json
import time

def console_chat(prompt: str) -> list:
    # Создаем экземпляр клиента для взаимодействия с GPT-3
    client = Client()
    
    # Инициализируем историю разговора с начальной фразой пользователя
    conversation_history = [{"role": "user", "content": prompt}]
    
    # Создаем директорию, если она не существует
    unx_time = int(time.time())
    os.makedirs(f".\\data\\{unx_time}\\json\\", exist_ok=True)
    
    # Открываем файл для записи
    with open(f".\\data\\{unx_time}\\json\\{unx_time}.json", 'w', encoding="utf-8") as file:
        json.dump({"title": unx_time, "chat": conversation_history}, file, indent=4, ensure_ascii=False)
    
    while True:
        # Запрашиваем ответ от бота, передавая ему историю разговора
        try:
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=conversation_history,
            )
            
            # Получаем текст ответа от бота из полученного ответа
            bot_response_text = response.choices[0].message.content
        except Exception as e:
            # В случае ошибки выводим сообщение об ошибке и предлагаем извинение
            print(f"error:", e)
            bot_response_text = "Извините, произошла ошибка."
        
        # Добавляем ответ бота в историю разговора и выводим его на экран
        conversation_history.append({"role": "assistant", "content": bot_response_text})
        print(bot_response_text)
        
        # Ждем ответ пользователя и добавляем его в историю разговора
        user_input = input("Введите промт: ")
        conversation_history.append({"role": "user", "content": user_input})
        
        # Проверяем, если пользователь ввел определенную команду для завершения диалога
        if user_input.lower() == "exit":
            break
        
        # Сохраняем историю разговора в JSON после каждого взаимодействия
        with open(f".\\data\\{unx_time}\\json\\{unx_time}.json", 'w', encoding="utf-8") as file:
            json.dump({"title": unx_time, "chat": conversation_history}, file, indent=4, ensure_ascii=False)
        
    return conversation_history

def main():
    prompt = "Привет"
    console_chat(prompt)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nвыход")