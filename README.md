# 🇷🇺 RusKaz Learner Bot

AI-powered Telegram bot for helping Kazakh-speaking children learn Russian language through translation, spelling correction, and interactive exercises.

---

## ✨ Features

- 🇰🇿 ➜ 🇷🇺 Kazakh to Russian translation
- ✍ Russian spelling correction
- 🧠 AI-generated explanations
- 📘 Interactive exercises
- ⭐ XP & gamification system
- 👤 User profiles
- 🤖 Powered by Groq LLM API
- 💾 SQLite database
- ⚡ Built with Aiogram 3

---

## 🛠 Tech Stack

- Python
- Aiogram 3
- SQLite + aiosqlite
- Groq API
- httpx
- FSM (Finite State Machine)

---

## 📂 Project Structure

```text
project/
│
├── handlers/
│   ├── start.py
│   ├── chat.py
│   └── profile.py
│
├── services/
│   ├── ai.py
│   └── db.py
│
├── keyboards/
│   └── menu.py
│
├── database.db
├── .env
├── main.py
└── README.md
```

---

## ⚙ Installation

### 1. Clone repository

```bash
git clone https://github.com/yourusername/ruskaz-learner-bot.git

cd ruskaz-learner-bot
```

---

### 2. Create virtual environment

```bash
python -m venv .venv
```

Activate:

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / MacOS

```bash
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create `.env` file:

```env
BOT_TOKEN=your_telegram_bot_token
GROQ_API_KEY=your_groq_api_key
```

---

## ▶ Run Bot

```bash
python main.py
```

---

## 🤖 Bot Functionalities

### 🇷🇺 Translation Mode

User sends Kazakh sentence:

```text
мен футбол ойнаймын
```

Bot responds:

```text
🇷🇺 Translation:
Я играю в футбол

📖 Explanation:
Я = мен
играю = ойнаймын

✏ Exercise:
Translate:
"Мен мектепке барамын"
```

---

### ✍ Spelling Mode

User sends:

```text
Я ходить школа
```

Bot responds:

```text
❌ Error

✅ Correct:
Я хожу в школу

📖 Explanation:
"ходить" → "хожу"

✏ Exercise:
Я ___ домой
```

---

## ⭐ Gamification

Users receive XP after completing exercises.

Example:

```text
⭐ XP: 45
🏆 Level: Beginner
```

---

## 🧠 AI Integration

The bot uses Groq API with Llama models for:

- Translation
- Grammar correction
- Exercise generation
- Educational explanations

---

## 🎯 Purpose

This project was created to help Kazakh-speaking children from Kazakhstan improve their Russian language skills in an interactive and engaging way.

---

## 📸 Screenshots

Add screenshots here:

```text
screenshots/
```

Example:

```markdown
![Main Menu](screenshots/menu.png)
```

---

## 🚀 Future Improvements

- Voice support
- Leaderboards
- Daily streaks
- Web dashboard
- Adaptive learning system
- Vocabulary trainer

---

## 👨‍💻 Author

Developed by Aldiyar Tirrek.

---

## 📄 License

MIT License
