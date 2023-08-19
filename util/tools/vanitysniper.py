import datetime
import os
import time

import requests
from colorama import Fore

from util.plugins.common import *

os.system('cls')

def change_vanity(code: str, server_id: str, token: str) -> bool:
    response = requests.patch(
        f"https://discord.com/api/v9/guilds/{server_id}/vanity-url",
        headers={"authorization": token},
        json={"code": code},
    )
    if response.ok:
        print(f"{Fore.BLUE} <*> Updated invite successfully, your server can now be accessed by 'discord.gg/{code}'. ")
        return True
    else:
        print(f"{Fore.LIGHTRED_EX} <!> Failed to update vanity url. Status code: {response.status_code}")
        return False


def check_vanity(code: str) -> bool:
    response = requests.get(f"https://discord.com/api/v9/invites/{code}")
    if response.status_code == 404:
        return True
    else:
        print(f"{Fore.LIGHTRED_EX} <*> Vanity is still in use.")
        return False


def snipe() -> None:
    XTitle("Vanity Sniper")
    token = input(f"{Fore.RED} <~> Token: {Fore.BLUE}")
    code = input(f"{Fore.WHITE} <~> Vanity code to snipe: ")
    server_id = input(f"{Fore.WHITE} <~> Server ID to apply vanity to: ")
    delay = int(input(f"{Fore.WHITE} <~> Delay between checks (seconds): "))

    try:
        while not check_vanity(code):
            time.sleep(delay)
            cur_time = datetime.datetime.now().strftime("%X")
            print(f"{Fore.WHITE} <*> Last checked at {cur_time} ", end="", flush=True)

        change_vanity(code, server_id, token)

    except KeyboardInterrupt:
        pass

