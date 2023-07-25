import multiprocessing

import requests
from colorama import Fore

from util.plugins.common import *


def Leaver():
    token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
    validateToken(token)
    if token.startswith("mfa."):
        print(f'{Fore.RED}[Error] : Just a heads-up, Xvirus won\'t be able to delete the servers since the account has 2FA enabled')

    guilds = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=getheaders(token)).json()
    for guild in guilds:
        try:
            response = requests.delete(f'https://discord.com/api/v10/users/@me/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.BLUE}Left guild: {Fore.WHITE}"+guild['name']+Fore.RESET)
            elif response.status_code == 400:
                requests.delete(f'https://discord.com/api/v10/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
                print(f'{Fore.RED}Deleted guild: {Fore.WHITE}'+guild['name']+Fore.RESET)
            else:
                print(f"The following error has been encountered and is being ignored: {response.status_code}")
                pass
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")
