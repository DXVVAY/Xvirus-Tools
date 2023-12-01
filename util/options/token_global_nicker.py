# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(nick, token):
    session = Client.get_session(token)
    result = session.patch(f"https://discord.com/api/v9/users/@me", json={'global_name': nick})
    if result.status_code == 200:
        Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def global_nicker():
    Output.set_title(f"Global Nicker")
    nick = utility.ask("Nick Name")
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[nick])
