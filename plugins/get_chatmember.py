import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import os
import time

# the secret configuration specific things
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

import pyrogram
logging.getLogger("pyrogram").setLevel(logging.WARNING)
from pyrogram import Client, Filters, ChatPermissions
from pyrogram import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant, UserBannedInChannel
  
try:
   chat= await bot.get_chat_member(channel_username,chat_id)
   if chat.status=='kicked':
      if edit_message:
               await reply ('you are banned')
        return False
      else:
       return True
try:
        await bot.get_chat_member("@TroJanzHEX", update.chat.id)
        
    except UserNotParticipant:
        await update.reply_text("You Need To Join Our Channel to perform that operatioN🤓\n\n@TroJanzHEX",
                                reply_markup=InlineKeyboardMarkup(
                                    [[InlineKeyboardButton(text="❤️Join Channel❤️",
                                                                       url="https://t.me/TroJanzHEX")]]))
        return
        
    except UserBannedInChannel:
        await update.reply_text("Sorry, You're BANNED")
        return
  
