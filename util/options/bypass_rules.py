# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(guild_id, token):
    session = Client.get_session(token)
    rules = session.get(f"https://discord.com/api/v9/guilds/{guild_id}/member-verification?with_guild=false").json()
    result = session.put(f"https://discord.com/api/v9/guilds/{guild_id}/requests/@me", json=rules)
    if result.status_code == 201:
        Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def bypass_rules():
    Output.set_title(f"Rules Bypass")
    guild_id = utility.ask("Guild ID")
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[guild_id])
