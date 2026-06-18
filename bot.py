   import telebot
from groq import Groq

 import telebot
from groq import Groq
import os

TOKEN = os.getenv("TOKEN")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
# ===== ПОДКЛЮЧЕНИЕ =====
client = Groq(api_key=GROQ_API_KEY)
bot = telebot.TeleBot(TOKEN)

# ===== КОМАНДА СТАРТ =====
@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, "🧠 Бот без цензуры (Groq)")

# ===== ОТВЕТЫ =====
@bot.message_handler(func=lambda m: True)
def chat(m):
    try:
        completion = client.chat.completions.create(
            messages=[{"role": "user", "content": m.text}],
            model="llama3-8b-8192"
        )
        bot.reply_to(m, completion.choices[0].message.content[:4000])
    except Exception as e:
        bot.reply_to(m, f"❌ Ошибка: {e}")

# ===== ЗАПУСК =====
print("✅ Бот запущен")
bot.infinity_polling()