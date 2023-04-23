import requests

from colorama import Fore

from util.plugins.common import getheaders, proxy, random_chinese

def SpamServers(token, icon, name=None):
    if name:
        for i in range(4):
            try:
                #Create all the servers named whatever you want
                payload = {'name': f'{name}', 'region': 'europe', 'icon': icon, 'channels': None}
                requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
                print(f"{Fore.BLUE}Created {name}.{Fore.RESET}")
            except Exception as e:
                print(f"The following exception has been encountered and is being ignored: {e}")
    for i in range(4):
        server_name = random_chinese(5,12)
        try:
            #Create all the servers named whatever you want
            payload = {'name': f'{server_name}', 'region': 'europe', 'icon': icon , 'channels': None}
            requests.post('https://discord.com/api/v7/guilds', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=payload)
            print(f"{Fore.BLUE}Created {server_name}.{Fore.RESET}")
        except Exception as e:
            print(f"The following exception has been encountered and is being ignored: {e}")