from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

@Client.on_message(filters.command("repo") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**ʜɪ" ɪ ᴄᴀɴ ᴡᴏʀᴋ ɴᴏᴡ ᴅᴏɴ'ᴛ ᴡᴏʀʀʏ ᴀʙᴏᴜᴛ ᴍᴇ।**""",
      reply_markup=InlineKeyboardMarkup(
                       [[
                          InlineKeyboardButton(
                             "⚡ ꜱᴜᴘᴘᴏʀᴛ", url="https://t.me/ShubhamMusics")
                       ],[
                          InlineKeyboardButton(
                             "ʀᴇᴘᴏ ☑️", url="https://github.com/Itsunknown-12/Zaid-Robot-Music")
                       ]]
                    ))
