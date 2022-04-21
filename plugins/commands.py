import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import pyrogram
from config import Config 
from pyrogram import Client, Filters, InlineKeyboardButton, InlineKeyboardMarkup
from translation import Translation
from Tools.Download import download
#from Tools import fsub


@Client.on_message(Filters.private & Filters.command(["start"]))
async def start(c, m):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.START.format(m.from_user.first_name),
                         reply_to_message_id=m.message_id,
                         reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Updates Channel", url="t.me/xz_bots"), InlineKeyboardButton("Support", url="t.me/xz_supportbot")]]))
    logger.info(f"{m.from_user.first_name} used start command")



@Client.on_message(Filters.private & Filters.command(["help"]))
async def help(c, m):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.HELP,
                         reply_to_message_id=m.message_id,
                         parse_mode="markdown")


@Client.on_message(Filters.private & Filters.command(["about"]))
async def about(c, m):
    await c.send_message(chat_id=m.chat.id,
                         text=Translation.ABOUT,
                         disable_web_page_preview=True,
                         reply_to_message_id=m.message_id,
                         parse_mode="markdown")

@Client.on_message(Filters.private & Filters.command(["converttovideo"]))
async def video(c, m):
    if m.reply_to_message is not None:
        await download(c, m)
    else:
        await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)

@Client.on_message(Filters.private & Filters.command(["converttofile"]))
async def file(c, m):
  if m.reply_to_message is not None:
        await download(c, m)
    else:
        await c.send_message(chat_id=m.chat.id, text=Translation.REPLY_TEXT)
