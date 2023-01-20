import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", " 5907950604:AAEz4DBbCBpbCOGup7GD2PGn3XCX1YkVzx0")

API_ID = int(os.environ.get("API_ID", "11508650"))

API_HASH = os.environ.get("API_HASH", "d4053a01b1c02f705c45a1e30496d11e")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
