from pyrogram import Client
from variables import *
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)                

class App(Client):

    def __init__(self):
        super().__init__(
            "tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            plugins={"root": "plugins"},
        )

    async def start(self):
       await super().start()
       me = await self.get_me()
       self.id = me.id
       self.name = me.first_name
       self.mention = me.mention
       self.username = me.username
       logging.info(f"{me.first_name} 𝘪𝘴 𝘴𝘵𝘢𝘳𝘵𝘦𝘥 ... ⚡️")                           

      
bot = App()
bot.run()


        










