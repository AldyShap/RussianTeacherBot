from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from services.db import get_xp

router = Router()

@router.message(lambda msg: msg.text == "👤 Профиль")
async def profile(message: Message):

    xp = await get_xp(message.from_user.id)

    text = f"""
👤 Ваш профиль

⭐ XP: {xp}

🏆 Уровень: Beginner
"""

    await message.answer(text)