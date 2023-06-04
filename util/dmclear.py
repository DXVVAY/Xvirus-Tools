import discord
from discord.ext import commands
from util.plugins.common import *

print("Enter your token:")
token = input("Token: ")
validateToken(token)
print("\nWrite '!clear' in one of your DMs to delete your messages")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", self_bot=True, intents=intents)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot is ready")


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
    print(f"\nRemoved {passed} messages with {failed} fails")
    input("\nPress ENTER to exit")
    main()


bot.run(token, bot=False)
