import asyncio
from aiogram import Bot, Dispatcher

import os
import json
import time

from dotenv import load_dotenv

from components.voice_processing import command
from components.promt_processing import console_chat
from components.audio_processing import speechAudio

load_dotenv()
tokenBot = os.getenv("TOKEN_BOT")

bot = Bot(token=tokenBot)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
    