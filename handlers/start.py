from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart

from services.db import add_user
from keyboards.menu import menu

router = Router()

@router.message(CommandStart())
async def start(message: Message):

    await add_user(message.from_user.id)

    text = """
👋 Привет!

🇷🇺 Я AI-учитель русского языка.

Выбери режим 👇
"""

    await message.answer(
        text,
        reply_markup=menu
    )