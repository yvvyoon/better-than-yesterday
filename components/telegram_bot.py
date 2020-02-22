import telegram


TELEGRAM_TOKEN = 'Nope'

bot = telegram.Bot(token=TELEGRAM_TOKEN)
updates = bot.get_updates()
chat_id = updates[-1].message.chat_id
latitude = 37.499129
longitude = 127.037126

bot.send_message(chat_id=chat_id, text='파스타프ㅏ스타파스타')
# bot.send_location(chat_id=chat_id, latitude=latitude, longitude=longitude)

for update in updates:
    print(update.message)
