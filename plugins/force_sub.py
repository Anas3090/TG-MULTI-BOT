from pyrogram import Client, filters 
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from helper.utils import not_subscribed


@Client.on_message(filters.private & filters.create(not_subscribed))
async def is_not_subscribed(client, message):
    await message.reply_text(
       text="**⚠️Sorry bro,You didn't Joined Our Updates Channel Join now and start again🙏**",
       reply_markup=InlineKeyboardMarkup( [[
           InlineKeyboardButton(text="📢𝙹𝚘𝚒𝚗 𝙼𝚢 𝚄𝚙𝚍𝚊𝚝𝚎 𝙲𝚑𝚊𝚗𝚗𝚎𝚕📢", url=client.invitelink)
           ],[
           InlineKeyboardButton("🔄 𝚃𝚛𝚢 𝙰𝚐𝚊𝚒𝚗 🔄", url=f"https://t.me/{client.username}?start=start")                             
           ]]
           )
       )






