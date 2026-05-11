from aiogram import Router
from aiogram.types import Message

from services.ai import generate
from services.db import (
    add_xp,
    get_xp,
    save_message
)

from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext

from services.ai import (
    translation_lesson,
    check_translation_practice,
    spelling_lesson,
    check_practice
)

class UserState(StatesGroup):

    spelling_input = State()
    spelling_practice = State()

    translate_input = State()
    translate_practice = State()

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


# ------------------------------------------ TRANSLATE --------------------------------------------------
@router.message(lambda msg: msg.text == "🇷🇺 Перевод")
async def translate_start(
    message: Message,
    state: FSMContext
):

    await state.set_state(
        UserState.translate_input
    )

    await message.answer(
        "🇰🇿 Напиши предложение на казахском"
    )

@router.message(UserState.translate_input)
async def translate_handler(
    message: Message,
    state: FSMContext
):

    await message.bot.send_chat_action(
        message.chat.id,
        "typing"
    )

    answer = await translation_lesson(
        message.text
    )

    await state.set_state(
        UserState.translate_practice
    )

    await message.answer(answer)

@router.message(UserState.translate_practice)
async def translate_practice(
    message: Message
):

    await message.bot.send_chat_action(
        message.chat.id,
        "typing"
    )

    answer = await check_translation_practice(
        message.text
    )

    await message.answer(answer)

# ---------------------------------------------- SPELLING ------------------------------------------------
@router.message(lambda msg: msg.text == "✍ Правописание")
async def spelling_start(
    message: Message,
    state: FSMContext
):

    await state.set_state(
        UserState.spelling_input
    )

    await message.answer(
        "✍ Напиши предложение на русском"
    )

@router.message(UserState.spelling_input)
async def spelling_check(
    message: Message,
    state: FSMContext
):

    await message.bot.send_chat_action(
        message.chat.id,
        "typing"
    )

    answer = await spelling_lesson(
        message.text
    )

    await state.set_state(
        UserState.spelling_practice
    )

    await message.answer(answer)

@router.message(UserState.spelling_practice)
async def practice_check(
    message: Message
):

    await message.bot.send_chat_action(
        message.chat.id,
        "typing"
    )

    answer = await check_practice(
        message.text
    )

    await message.answer(answer)


@router.message()
async def fallback(message: Message):

    await message.answer(
        "Выбери режим через кнопки 👇"
    ) 