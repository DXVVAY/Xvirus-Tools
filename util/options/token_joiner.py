# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(invite, token):
    session = Client.get_session(token)
    result = session.post(f"https://discord.com/api/v9/invites/{invite}", json={"session_id": utility.rand_str(32)})
    if result.status_code == 200:
        Output("good", token).log(f"Joined {Fore.LIGHTBLACK_EX}{invite} {Fore.GREEN}-> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def token_joiner():
    Output.set_title(f"Token Joiner")
    invite = utility.ask("Invite")
    invite = invite.split("/")[-1]
    max_threads = utility.ask("Thread Count")

    server_name = utility.get_server_name(invite)
    if server_name is not None:
        Output("info").notime(f"Joining {Fore.RED}{server_name}")
    utility.run_threads(max_threads=max_threads, func=send, args=[invite])
