import os

import telegram
from dotenv import load_dotenv

import location_getter

load_dotenv(verbose=True)

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

bot = telegram.Bot(token=TELEGRAM_TOKEN)
updates = bot.get_updates()
chat_id = updates[-1].message.chat_id
latitude = location_getter.latitude
longitude = location_getter.longitude

bot.send_message(chat_id=chat_id, text='파스타프ㅏ스타파스타')
# bot.send_location(chat_id=chat_id, latitude=latitude, longitude=longitude)

# for update in updates:
#     print(update.message)
