import os
from dotenv import load_dotenv

from components.voice_processing import command
from components.promt_processing import answerGPT

# load_dotenv()
# TOKEN = os.getenv("TOKEN")

def main():
    promt = command()
    answerGPT(promt)

if __name__ == "__main__":
    main()