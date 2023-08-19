import threading

import discord
from colorama import Fore
from discord.ext import commands

from util.plugins.common import *


def dmclearer():
    XTitle("Dm Clearer")
    token = input(f"{Fore.RED} <~> Token: {Fore.BLUE}")
    CheckToken(token)
    print("\n <*> Write '!clear' in one of your DMs to delete your messages")

    intents = discord.Intents.all()
    bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        print(" <*> Bot is ready")

    def delete_messages(ctx, limit):
        passed = 0
        failed = 0
        for msg in ctx.message.channel.history(limit=limit):
            if msg.author.id == ctx.bot.user.id:
                try:
                    msg.delete()
                    passed += 1
                except:
                    failed += 1
        print(f"\n <*> Removed {passed} messages with {failed} fails")
        

    @bot.command()
    async def clear(ctx, limit: int = None):
        t = threading.Thread(target=delete_messages, args=(ctx, limit))
        t.start()

    bot.run(token, bot=False)