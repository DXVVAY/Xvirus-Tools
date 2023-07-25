import requests
from colorama import Fore
import multiprocessing

from util.plugins.common import *


def dmdeleter(channel_id, token):
    try:
        requests.delete(f'https://discord.com/api/v10/channels/{channel_id}', proxies={"http": f'{proxy()}'},
                        headers=getheaders(token))
        print(f"{Fore.RED}Deleted DM: {Fore.WHITE}{channel_id}{Fore.RESET}")
    except Exception as e:
        print(f"The following error has been encountered and is being ignored: {e}")

def deletedms():
    token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
    validateToken(token)
    channelIds = requests.get("https://discord.com/api/v10/users/@me/channels", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()

    processes = []
    for channel_id in [channel['id'] for channel in channelIds]:
        t = multiprocessing.Process(target=dmdeleter, args=(channel_id, token))
        t.start()
        processes.append(t)

    for process in processes:
        process.join()