import os
import asyncio

from contextlib import asynccontextmanager

from fastapi import FastAPI, Request

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import Update
from aiogram.fsm.storage.memory import MemoryStorage

from dotenv import load_dotenv

from handlers import start, chat, profile

from services.db import init_db

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_PATH = "/webhook"

WEBHOOK_URL = (
    "https://russianteacherbot-mxzt.onrender.com/webhook"
)

bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)

dp = Dispatcher(
    storage=MemoryStorage()
)

dp.include_router(start.router)
dp.include_router(chat.router)
dp.include_router(profile.router)


@asynccontextmanager
async def lifespan(app: FastAPI):

    await init_db()

    await bot.set_webhook(WEBHOOK_URL)

    print("Webhook set!")

    yield

    await bot.delete_webhook()


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():

    return {
        "status": "ok"
    }


@app.post(WEBHOOK_PATH)
async def webhook(request: Request):

    data = await request.json()

    update = Update.model_validate(data)

    asyncio.create_task(
        dp.feed_update(bot, update)
    )

    return {"ok": True}