from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv
import asyncio
import os

from handlers import start, chat, profile
from services.db import init_db

load_dotenv()

bot = Bot(
    token=os.getenv("BOT_TOKEN"),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher(storage=MemoryStorage())

dp.include_router(start.router)
dp.include_router(chat.router)
dp.include_router(profile.router)

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())