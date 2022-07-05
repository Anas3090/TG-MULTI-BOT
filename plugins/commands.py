from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import insert, getid
from variables import STAT_STICK, PICS, ADMIN, DELAY
import asyncio
import random


@Client.on_message(filters.private & filters.command("start"))
async def start_message(bot, message):
    insert(int(message.chat.id))
    await message.reply_chat_action("Typing")
    await asyncio.sleep(DELAY)
    m=await message.reply_sticker(STAT_STICK)
    await asyncio.sleep(DELAY)
    await m.delete()             
    await message.reply_photo(
        photo=random.choice(PICS),
        caption=f"Hello {message.from_user.mention}👋🏻\nI'am A Multi use Bot with many usefull features.\neg:- Telegarph, Channel ID, User ID, Fun, Group Id etc...\nYou can see My commands by below button... \n\n◉ send channel last message with forwerd tag to get the channel id 💯",               
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("❣️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓", url="https://t.me/BETA_BOTSUPPORT"),
            InlineKeyboardButton("📢 𝐔𝐏𝐃𝐀𝐓𝐄𝐒", url="https://t.me/Beta_Bot_Updates")
            ],[            
            InlineKeyboardButton("ℹ️ 𝐇𝐄𝐋𝐏", callback_data="help"),
            InlineKeyboardButton("😉 𝐅𝐔𝐍", callback_data="fun")
            ],[
            InlineKeyboardButton("👨‍💻 𝐃𝐄𝐕𝐒 👨‍💻 ", callback_data="devs"),
            InlineKeyboardButton("🤖 𝐀𝐁𝐎𝐔𝐓", callback_data="about")
            ]]
            )
        )


         
@Client.on_message(filters.command("id"))
async def id_message(bot, message):
    await message.reply_text(
    text = f"""<i>
<u>👁️‍🗨️YOUR DETAILS</u>

○ ID : <code>{message.from_user.id}</code>
○ First Name : <code>{message.from_user.first_name}<code>
○ UserName : @{message.from_user.username}
○ link : <code>https://t.me/{message.from_user.username}</code>

Thank You For Using Me❣️</i>""")


@Client.on_message(filters.command(["stickerid"]))
async def stickerid(bot, message):   
    if message.reply_to_message.sticker:
       await message.reply(f"**Sticker ID is**  \n `{message.reply_to_message.sticker.file_id}` \n \n ** Unique ID is ** \n\n`{message.reply_to_message.sticker.file_unique_id}`", quote=True)
    else: 
       await message.reply("Oops !! Not a sticker file")


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["broadcast"]))
async def broadcast(bot, message):
 if (message.reply_to_message):
   ms = await message.reply_text("Geting All ids from database ...........")
   ids = getid()
   tot = len(ids)
   await ms.edit(f"Starting Broadcast .... \n Sending Message To {tot} Users")
   for id in ids:
     try:
     	await message.reply_to_message.copy(id)
     except:
     	pass


@Client.on_message(filters.private & filters.user(ADMIN) & filters.command(["users"]))
async def get_users(bot, message):    
    msg = await bot.send_message(chat_id=message.chat.id, text="<b>Processing ...</b>")
    ids = getid()
    tot = len(ids)
    await msg.edit(f"Total uses = {tot}")




