# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(guild_id, token):
    session = Client.get_session(token)
    result = session.delete(f"https://discord.com/api/v9/users/@me/guilds/{guild_id}", json={"session_id": utility.rand_str(32)})
    if result.status_code == 204:
        Output("good", token).log(f"Left -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def token_leaver():
    Output.set_title(f"Token Leaver")
    guild_id = utility.ask("Guild ID")
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[guild_id])
