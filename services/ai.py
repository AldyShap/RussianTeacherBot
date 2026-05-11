import httpx
import os

from dotenv import load_dotenv

load_dotenv()

async def generate(prompt: str):

    async with httpx.AsyncClient() as client:

        response = await client.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {os.getenv('GROQ_API_KEY')}",
                "Content-Type": "application/json"
            },
            json={
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {
                        "role": "system",
                        "content": """
Ты учитель русского языка для казахских детей.
Объясняй просто.
"""
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            }
        )

        data = response.json()

        if "choices" not in data:
            return "❌ AI Error"

        return data["choices"][0]["message"]["content"]


async def translation_lesson(text: str):

    prompt = f"""
Ты обучаешь казахских детей русскому языку.

Ребенок написал:
{text}

Твоя задача:
1. Перевести на русский
2. Объяснить очень просто
3. Дать маленькое упражнение

Формат:

🇷🇺 Перевод:
...

📖 Объяснение:
...

✏ Упражнение:
...
"""

    return await generate(prompt)

async def check_translation_practice(text: str):

    prompt = f"""
Ребенок выполняет упражнение по переводу. Он написал текст на казахском/русском твоя задача перевести и проверить

Ответ:
{text}

Если правильно:
- Похвали путем типо "отличная работа" тд
- переведи и обясни

Если ошибка:
- исправь
- объясни коротко


Очень коротко.
"""

    return await generate(prompt)


async def spelling_lesson(text: str):

    prompt = f"""
Ты проверяешь русский текст ребенка.

Текст:
{text}

Твоя задача:
1. Найти ошибки
2. Исправить
3. Объяснить очень просто
4. Дать короткое упражнение

Формат:

✅ Правильно:
...

📖 Объяснение:
...

✏ Упражнение:
...
"""

    return await generate(prompt)


async def check_practice(answer: str):

    prompt = f"""
Ребенок выполняет упражнение по русскому языку. 

Ответ:
{answer}

Если правильно:
- похвали
- обясни кратко почему так

Если ошибка:
- мягко исправь
- дай немного упражнений

Очень коротко.
"""

    return await generate(prompt)