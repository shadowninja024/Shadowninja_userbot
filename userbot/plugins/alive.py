"""Check if userbot alive. If you change these, you become the gayest gay such that even the gay world will disown you."""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from platform import uname
from userbot import ALIVE_NAME
from userbot.utils import admin_cmd


DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Set ALIVE_NAME in config vars in Heroku"

#@command(outgoing=True, pattern="^.alive$")
@borg.on(admin_cmd(pattern=r"alive"))
async def amireallyalive(alive):
    """ For .alive command, check if the bot is running.  """
    await alive.edit("`I'm Fucking alive Moron ^.^ \nYour bot is running\n\nTelethon version: 6.9.0\nPython: 3.7.3\n\n`"
                     f"`My peru owner`: {DEFAULTUSER}\n\n"
                     "`Telethon version: 6.9.0\nPython: 3.7.3\nfork by:` @Shadow_ninja_legit\n"
                     "`Database Status: Databases functioning normally!\n\nAlways with you, my master!\n`"
                     "[Deploy this userbot Now](https://github.com/shadowninja024/Shadowninja_userbot)\n\n"
                     "[Bot Creator](http://t.me/Shadow_ninja_legit)")
