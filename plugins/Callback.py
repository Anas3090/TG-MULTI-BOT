from pyrogram import Client, filters, __version__
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton                              
from pyrogram.types import CallbackQuery
import asyncio


@Client.on_callback_query()
async def callback(bot, msg):
   data = msg.data
   if data == "help":
       await msg.message.edit(       
           text="""CLICK THE BELOW BUTTONS TO KNOW MY COMMANDS.""",       
           reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("LOGO MAKER", callback_data="logo"),
                  InlineKeyboardButton("PHOTO EDIT", callback_data="editor")
                  ],[
                  InlineKeyboardButton("CARBON", callback_data="carbon"),
                  InlineKeyboardButton("CHANNEL ID", callback_data="chid")
                  ],[
                  InlineKeyboardButton("TELEGRAPH", callback_data="tgraph"),
                  InlineKeyboardButton("FUN GAMES", callback_data="fun")
                  ],[
                  InlineKeyboardButton("PASTE CODE", callback_data="paste"),
                  InlineKeyboardButton("FONT STYLE", callback_data="fun")
                  ],[
                  InlineKeyboardButton("❤️‍🩹 ABOUT", callback_data="about"),
                  InlineKeyboardButton("❤️‍🩹 DEVS", callback_data="devs")
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start")
                  ]]
                  )
           )
   elif data == "about":
         await msg.message.edit(
             text=f""" 
╔════❰ 𝙼𝚄𝙻𝚃𝙸 𝙱𝙾𝚃 ❱═❍
║╭━━━━━━━━━━━━━━━➣
║┣⪼🤖ᴍʏ ɴᴀᴍᴇ : {bot.mention}
║┣⪼👦ᴅᴇᴠ 1 : <a href=https://t.me/about_jeol>ᴊᴇᴏʟ</a>
║┣⪼👨‍💻ᴅᴇᴠ 2 : <a href=https://t.me/mr_MKN>ᴍʀ.ᴍᴋɴ ᴛɢ</a>
║┣⪼❣️sᴏᴜʀᴄᴇ ᴄᴏᴅ : <a href=https://github.com/Jeolpaul/TG-MULTI-BOT>ᴛɢ-ᴍᴜʟᴛɪ-ʙᴏᴛ</a>
║┣⪼📡ʜᴏsᴛᴇᴅ ᴏɴ : <a href=https://dashboard.heroku.com>ʜᴇʀᴏᴋᴜ</a>
║┣⪼🗣️ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>ᴘʏᴛʜᴏɴ3</a>
║┣⪼📚ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>ᴘʏʀᴏɢʀᴀᴍ</a> 
║┣⪼🗒️ᴠᴇʀsɪᴏɴ : Pyrogram v{__version__}  
║╰━━━━━━━━━━━━━━━➣
╚══════════════════❍ """,
              disable_web_page_preview = True,
              reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
         )        
   elif data == "start":
         await msg.message.edit(
             text=f"Hello {msg.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",          
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("✨️ Support", url="https://t.me/BETA_SUPPORT"),
                 InlineKeyboardButton("📢 Updates", url="https://t.me/Beta_BoTZ")
                 ],[            
                 InlineKeyboardButton("ℹ️ Help", callback_data="help"),
                 InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")
                  ]]
                  )
         )
   elif data == "devs":
         await msg.message.edit(
             text=f"These Are My Developers",
             reply_markup=InlineKeyboardMarkup( [[
                  InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 1", user_id=5172114510),
                  InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 2", user_id=900873119)
                  ],[
                  InlineKeyboardButton("❣️ 𝐒𝐎𝐔𝐑𝐂𝐄 𝐂𝐎𝐃𝐄 ❣️", url="https://github.com/Jeolpaul/TG-MULTI-BOT"),
                  ],[
                  InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                  InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                  ]]
                  )
             )
   elif data == "fun":
         await msg.message.edit(
             text=f"""<b><u>JUST TEST THIS COMMANDS 😉</u></b>

◉ /runs         
◉ /ikka      
◉ /dice     
◉ /arrow    
◉ /goal    
◉ /luck    
◉ /throw     
◉ /bowling  
◉ /tenpins    
""",      
             reply_markup=InlineKeyboardMarkup( [[
                 InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                 InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                 ]]
                 )
             )
   elif data == "botz":
         await msg.message.edit(
             text="🤖 This is My botz 😁",
                 reply_markup=InlineKeyboardMarkup( [[
                     InlineKeyboardButton("ℹ️ OUR OTHER BOTZ", url="https://t.me/BETA_BOTZ/86"),   
                     InlineKeyboardButton("↩️ 𝐁𝐀𝐂𝐊", callback_data="start"),
                     InlineKeyboardButton("🔒 𝐂𝐋𝐎𝐒𝐄", callback_data="close")
                     ]]
                     )
                 )
   elif data == "close":
        await msg.message.delete()
        try:
            await msg.message.reply_to_message.delete()
        except:
            pass
























