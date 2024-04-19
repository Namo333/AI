import os
from dotenv import load_dotenv

from components.voice_processing import command
from components.promt_processing import answerGPT
from components.audio_processing import speechAudoi

def main():
    promt = command()
    text = answerGPT(promt)
    speechAudoi(text)
if __name__ == "__main__":
    main()