from components.voice_processing import command
from components.promt_processing import answerGPT
from components.audio_processing import speechAudio

def main():
    print("Выберите принцип работы:")
    print("1. Озвучить ответ")
    print("2. Не озвучивать ответ")
    
    while True:
        try:
            answer = int(input("Выбор: "))
            if answer in [1, 2]:
                break
            else:
                print("Пожалуйста, выберите 1 или 2.")
        except ValueError:
            print("Пожалуйста, введите число.")

    print("Выберите способ ввода промта:")
    print("1. Написать текст вручную")
    print("2. Произнести промт словами")

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

    text = answerGPT(promt)

    if answer == 1:
        speechAudio(text)

if __name__ == "__main__":
    main()