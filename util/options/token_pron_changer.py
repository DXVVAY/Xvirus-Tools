# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(pronouns, token):
    session = Client.get_session(token)
    result = session.patch(f"https://discord.com/api/v9/users/%40me/profile", json={"pronouns": pronouns})
    if result.status_code == 200:
        Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(token, result.text, result.status_code)

def token_pron_changer():
    Output.set_title(f"Pronouns Changer")
    custom = utility.ask("Random Pronouns (y/n)")
    if custom == "y":
        get = requests.get('https://cloud.xvirus.lol/randompronounce.txt')
        if get.status_code == 200:
            pronouns = get.text.splitlines()
        else:
            Output("bad").notime(f"Failed to fetch pronounses from {url} ({get.status_code})")
            pronouns = utility.ask("pronouns")
    else:
        pronouns = utility.ask("pronouns")
    max_threads = utility.ask("Thread Count")
    g = random.choice(pronouns)
    utility.run_threads(max_threads=max_threads, func=send, args=[g])
