from concurrent.futures import ThreadPoolExecutor

import requests
from colorama import Fore

from util.plugins.common import *


def massdmconfig(token, channel_id, content):
    try:
        requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages',
                      headers=getheaders(token),
                      data={"content": content})
        print(f"{Fore.RED}Messaged {Fore.BLUE}ID: {channel_id}{Fore.RESET}")
    except Exception as e:
        print(f"The following error has been encountered and is being ignored: {e}")


def massdm():
    XTitle("Mass DM")
    token = input(f"{Fore.RED} <~> Token: {Fore.BLUE}")
    validateToken(token)
    message = input(f"{Fore.RED} <~> Message that will be sent to every friend: {Fore.BLUE}")
    
    headers = getheaders(token)
    channelIds = requests.get("https://discord.com/api/v9/users/@me/channels", headers=getheaders(token)).json()
    
    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(massdmconfig, token, channel['id'], message) for channel in channelIds]

    print("All messages sent!")
