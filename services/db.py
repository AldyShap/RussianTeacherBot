import aiosqlite

DB_NAME = "database.db"

async def init_db():

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute("""
        CREATE TABLE IF NOT EXISTS users (
            telegram_id INTEGER PRIMARY KEY,
            xp INTEGER DEFAULT 0
        )
        """)

        await db.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER,
            role TEXT,
            content TEXT
        )
        """)

        await db.commit()


async def add_user(telegram_id: int):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            "INSERT OR IGNORE INTO users (telegram_id) VALUES (?)",
            (telegram_id,)
        )

        await db.commit()


async def add_xp(telegram_id: int, amount: int):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            "UPDATE users SET xp = xp + ? WHERE telegram_id = ?",
            (amount, telegram_id)
        )

        await db.commit()


async def get_xp(telegram_id: int):

    async with aiosqlite.connect(DB_NAME) as db:

        cursor = await db.execute(
            "SELECT xp FROM users WHERE telegram_id = ?",
            (telegram_id,)
        )

        result = await cursor.fetchone()

        return result[0] if result else 0


async def save_message(telegram_id: int, role: str, content: str):

    async with aiosqlite.connect(DB_NAME) as db:

        await db.execute(
            """
            INSERT INTO messages
            (telegram_id, role, content)
            VALUES (?, ?, ?)
            """,
            (telegram_id, role, content)
        )

        await db.commit()