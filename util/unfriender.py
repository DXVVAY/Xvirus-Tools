import json

import requests
from colorama import Fore

from util.plugins.common import *


def UnFriender():
    token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
    validateToken(token)
    friendIds = requests.get("https://discord.com/api/v10/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    for friend in friendIds:
        try:
            requests.delete(f'https://discord.com/api/v10/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            print(f"{Fore.GREEN}Removed friend: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
