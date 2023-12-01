# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(channel_id, token):
    session = Client.get_session(token)
    while True:
        result = session.post(f"https://discord.com/api/v9/channels/{channel_id}/typing")
        if result.status_code == 204:
            Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
        elif result.status_code == 429:
            pass
        else:
            Output.error_logger(token, result.text, result.status_code)

def token_typer():
    Output.set_title(f"Token Fake Typer")
    channel_id = utility.ask("Channel ID")
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[channel_id])
