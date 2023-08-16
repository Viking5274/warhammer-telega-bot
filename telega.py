import os

from telethon import events
from telethon.sync import TelegramClient
from help import MyBigLlama
from dotenv import load_dotenv
import logging

logging.basicConfig(filename='warhammer.log', encoding='utf-8', level=logging.DEBUG)
load_dotenv()
api_id = int(os.getenv("BOT_API_ID"))
api_hash = os.getenv("BOT_API_HASH")
bot_token = os.getenv("BOT_TOKEN")

# We have to manually call "start" if we want an explicit bot token
bot = TelegramClient("bot", api_id, api_hash).start(bot_token=bot_token)
lama = MyBigLlama()


@bot.on(events.NewMessage)
async def my_event_handler(event):
    logging.info(f"SENDER IS: {event.sender.id, event.sender.username}")
    logging.info(event.raw_text)
    answer = lama.send_question(event.raw_text)

    logging.info(answer)
    await event.reply(str(answer))


bot.start()
bot.run_until_disconnected()
