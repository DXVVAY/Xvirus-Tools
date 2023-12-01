# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(house, token):
    session = Client.get_session(token)
    result = session.post(f"https://discord.com/api/v9/hypesquad/online", json={'house_id': house})
    if result.status_code == 204:
        Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def hypesquad_changer():
    Output.set_title(f"Hypesquad Changer")
    print(f'''
        {Fore.MAGENTA}[1] HypeSquad Bravery
        {Fore.LIGHTRED_EX}[2] HypeSquad Brilliance
        {Fore.LIGHTGREEN_EX}[3] HypeSquad Balance
    ''')
    house = utility.ask("House")
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[house])
