# Imteyaz
# Radio Player
# Join @King_fighter_Bot_support

from os import environ
from config import Config

# import logging
from pyrogram import Client, idle

API_ID=Config.API_ID
API_HASH=Config.API_HASH
SESSION=Config.SESSION
CHAT_NAME=Config.CHAT_NAME
ADMIN=Config.ADMIN

PLUGINS = dict(
    root="plugins",
    include=[
        "radio",
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED. JOIN @King_fighter_Bot_support')
idle()
app.stop()
print('\n>>> USERBOT STOPPED. JOIN @King_fighter_Bot_support')
