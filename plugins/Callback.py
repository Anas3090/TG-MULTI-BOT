from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "commands":
       await msg.message.edit(       
           text="""HEY HERE YOU CAN FIND THE BASIC COMMANDS OF MINE.IF YOU DON'T KNOW HOW TO USE COMMAND JOIN SUPPORT GROUP AND ASK.

<b><u>COMMANDS</u></b>

◉ /start - check bot alive
◉ /help - get help
◉ /id - your tg id & info
◉ /stickerid - Reply To Any Sticker to get sticker id
◉ /dice - just fun 😉
◉ /bots - list of my bots
""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("back", callback_data="start"),
                  InlineKeyboardButton("close", callback_data="close")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
╔════❰ 𝙼𝚄𝙻𝚃𝙸 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {client.mention}
║┣⪼👦ᴅᴇᴠ 1 : <a href=https://t.me/JP_Jeol>ᴊᴇᴏʟᴘᴀᴜʟ</a>
║┣⪼👨‍💻ᴅᴇᴠ 2 : <a href=https://t.me/mr_MKN>ᴍʀ.ᴍᴋɴ ᴛɢ</a>
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : <a href=https://dashboard.heroku.com>ʜᴇʀᴏᴋᴜ</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ3</a>
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : 1.0.3  
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("back", callback_data="start"),
                  InlineKeyboardButton("close", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻 How are you Iam The official BETA BOT Type /bots to see our bot list",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("Support", url="https://t.me/BETA_BOTSUPPORT"),
                     InlineKeyboardButton("Updates", url="https://t.me/BETA_UPDATES")
                     ],[
                     InlineKeyboardButton("Developer", url="https://t.me/JP_Jeol"),
                     InlineKeyboardButton("commands", callback_data="commands"),
                     InlineKeyboardButton("about", callback_data="about")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























