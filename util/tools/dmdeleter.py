import threading

import requests
from colorama import Fore

from util.plugins.common import *


def dmdeleter(channel_id, token):
    try:
        requests.delete(f'https://discord.com/api/v9/channels/{channel_id}', proxies={"http": f'{proxy()}'},
                        headers=getheaders(token))
        print(f"{Fore.RED} <*> Deleted DM: {Fore.WHITE}{channel_id}{Fore.RESET}")
    except Exception as e:
        print(f" <!> The following error has been encountered and is being ignored: {e}")


def deletedms():
    XTitle("Dm Deleter")
    token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
    CheckToken(token)
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()

    threads = []
    for channel_id in [channel['id'] for channel in channelIds]:
        t = threading.Thread(target=dmdeleter, args=(channel_id, token))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()