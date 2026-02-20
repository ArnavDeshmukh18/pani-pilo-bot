import os
import random
from datetime import datetime
from telegram import Bot
import pytz

TOKEN = os.environ["BOT_TOKEN"]
CHAT_IDS = [int(x) for x in os.environ["CHAT_IDS"].split(",")]

START_HOUR = 8
END_HOUR = 12

messages = [
    "Kruti Baby Pani Pilo 💧",
    "Hydration time kruti flower 🥤",
    "Doctor Arnav says drink water Kruti  😌",
    "Water break my Queen kruti 👑💧"
]

ist = pytz.timezone("Asia/Kolkata")
now = datetime.now(ist)

TEST_MODE = os.environ.get("TEST_MODE", "false").lower() == "true"

if TEST_MODE or (START_HOUR <= now.hour < END_HOUR):
    bot = Bot(token=TOKEN)
    msg = random.choice(messages)

    for chat_id in CHAT_IDS:
        bot.send_message(chat_id=chat_id, text=msg)

    print("Message sent:", msg)
else:
    print("Outside working hours. No message sent.")
