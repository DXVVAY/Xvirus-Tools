# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(bio, token):
    session = Client.get_session(token)
    result = session.patch(f"https://discord.com/api/v9/users/@me", json={"bio": bio})
    if result.status_code == 200:
        Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def token_bio_changer():
    Output.set_title(f"Bio Changer")
    bio = utility.ask("Bio")
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[bio])
