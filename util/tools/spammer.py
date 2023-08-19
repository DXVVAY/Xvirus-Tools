import asyncio
import threading

import discord
from colorama import Fore
from discord.ext import commands

from util.plugins.common import *


def selfbotspammer():
    XTitle("Selfbot Spammer")
    token = input(f"{Fore.RED} <~> Token: {Fore.BLUE}")
    CheckToken(token)
    print("\n <*> Write '!spam (message) (Number)' in one of your DMs to delete your messages")

    intents = discord.Intents.all()

    bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)
    bot.remove_command("help")

    @bot.event
    async def on_ready():
        print(" <*> Bot is ready")

    @bot.command()
    async def clear(ctx, limit: int = None):
        passed = 0
        failed = 0
        async for msg in ctx.message.channel.history(limit=limit):
            if msg.author.id == ctx.bot.user.id:
                try:
                    await msg.delete()
                    passed += 1
                except:
                    failed += 1
        print(f"\n <!> Removed {passed} messages with {failed} fails")
        

    async def spam_task(ctx, text: str, times: int):
        await ctx.message.delete()
        for _ in range(times):
            try:
                await ctx.send(text)
            except discord.HTTPException:
                print(" <!> Rate limited.")
                pass

    @bot.command()
    async def spam(ctx, text: str, times: int):
        threads = []
        for _ in range(times):
            thread = threading.Thread(target=asyncio.run, args=(spam_task(ctx, text, 1),))
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()

    bot.run(token)
