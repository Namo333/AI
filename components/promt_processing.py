from g4f.client import Client

def console_chat(promt:str)->str:
    client = Client()
    conversation_history = []
    while True:
        conversation_history.append({"role": "user", "content": promt})
        try:
            response = client.chat.completions.create(
                model='gpt-3.5-turbo',
                messages=conversation_history,
            )
            # Извлекаем текст ответа 
            bot_response_text = response.choices[0].message.content 
        except Exception as e:
            print(f"erors:", e)
            bot_response_text = "Извините, произошла ошибка."

        conversation_history.append({"role": "assistant", "content": bot_response_text})
        print(bot_response_text)
        return conversation_history