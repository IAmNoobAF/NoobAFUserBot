"""Check if userbot alive."""
#IMG CREDITS: @IAm_AlanWalker
import asyncio
from telethon import events
from uniborg.util import admin_cmd
from userbot import ALIVE_NAME
from telethon.tl.types import ChannelParticipantsAdmins
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"
PM_IMG = "https://telegra.ph/IAm-AlanWalker-08-08"
pm_caption = "`IAm AlanWalker's UserBot Is:` **Alive!**\n\n"
pm_caption += "**SYSTEM STATUS**\n"
pm_caption += "`TELETHON VERSION:` **15.5.0**\n`Python:` **8.6.5**\n"
pm_caption += "`DATABASE STATUS:` **Functional**\n"
pm_caption += "**Current Branch** : `Master Branch`\n"
pm_caption += "**IAm AlanWalker OS** : `5.15`\n"
pm_caption += "**Current Sat** : `IAm AlanWalkerSat-5.75`\n"
pm_caption += f"**My Boss** : {DEFAULTUSER} \n"
pm_caption += "**Heroku Database** : `AWS - Working Properly, Everything Is Perfect My Master.`\n\n"
pm_caption += "**License** : Standard Licence Suggested By [IAm AlanWalker](https://t.me/IAm_AlanWalker) .\n"
pm_caption += "Copyright : By [IAm AlanWalker](https://t.me/IAm_AlanWalker) .\n"
pm_caption += "All Rights Reserved © IAm AlanWalker."
#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    chat = await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG,caption=pm_caption)
    await alive.delete() 
    
