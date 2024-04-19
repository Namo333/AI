import speech_recognition as sr

def command():
    objectR = sr.Recognizer()
    source = sr.Microphone()

    with source as source:
        print("Говорите")
        objectR.pause_threshold = 0.5
        objectR.adjust_for_ambient_noise(source, duration=0.5)
        audio = objectR.listen(source)
    try:
        promt = objectR.recognize_google(audio, language="ru-RU").lower()
        print("Вы сказали: " + promt)
    except sr.UnknownValueError:
        print("Я вас не понимаю")
        promt = command()
    except sr.RequestError as e:
        print("Произошла ошибка при запросе к сервису распознавания: {0}".format(e))
    return promt