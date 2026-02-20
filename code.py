import asyncio
import random
import os
from datetime import datetime
from telegram import Bot
from dotenv import load_dotenv
import pytz

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
CHAT_IDS = [int(x) for x in os.getenv("CHAT_IDS").split(",")]

START_HOUR = 8
END_HOUR = 12

messages = [
    "Kruti Baby Pani Pilo 💧",
    "Hydration time kruti flower 🥤",
    "Doctor Arnav says drink water Kruti  😌",
    "Water break my Queen kruti 👑💧"
]

ist = pytz.timezone("Asia/Kolkata")

async def send_reminder():
    bot = Bot(token=TOKEN)

    while True:
        now = datetime.now(ist)
        current_hour = now.hour

        if START_HOUR <= current_hour < END_HOUR:
            msg = random.choice(messages)

            for chat_id in CHAT_IDS:
                try:
                    await bot.send_message(chat_id=chat_id, text=msg)
                    print(f"Sent to {chat_id}: {msg}")
                except Exception as e:
                    print(f"Error sending to {chat_id}: {e}")

            await asyncio.sleep(1800)  # 30 minutes
        else:
            print("Outside working hours. Sleeping 10 mins...")
            await asyncio.sleep(600)

asyncio.run(send_reminder())
