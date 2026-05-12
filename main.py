import os

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from dotenv import load_dotenv

from handlers import start, chat, profile

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(chat.router)
dp.include_router(profile.router)

WEBHOOK_PATH = "/webhook"

WEBHOOK_URL = (
    "https://YOUR-APP.onrender.com/webhook"
)


@asynccontextmanager
async def lifespan(app: FastAPI):

    await bot.set_webhook(WEBHOOK_URL)

    print("Webhook set!")

    yield

    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)


@app.post(WEBHOOK_PATH)
async def webhook(request: Request):

    data = await request.json()

    await dp.feed_raw_update(bot, data)

    return {"ok": True}