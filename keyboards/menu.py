from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(
                text="🇷🇺 Перевод"
            ),
            KeyboardButton(
                text="✍ Правописание"
            )
        ],
        [
            KeyboardButton(
                text="👤 Профиль"
            )
        ]
    ],
    resize_keyboard=True
)