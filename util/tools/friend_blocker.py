import threading

import requests
from colorama import Fore

from util.plugins.common import *


def Block(token, friends):
    count = 0
    for friend in friends:
        try:
            requests.put(
                f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"type": 2})
            count += 1
            print(f"{Fore.BLUE} <*> blocked: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f" <!> The following error has been encountered and is being ignored: {e}")


def BlockAll():
    XTitle("Friend Blocker")
    token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
    CheckToken(token)
    threads = []
    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
        t = threading.Thread(target=Block, args=(token, friend))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()