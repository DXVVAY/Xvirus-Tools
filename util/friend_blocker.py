import requests
from colorama import Fore

from util.plugins.common import *


def Block(token, friends):
    #get all friends
    count = 0
    for friend in friends:
        try:
            #block all friends they have
            requests.put(
                f'https://discord.com/api/v10/users/@me/relationships/'+friend['id'], proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"type": 2})
            count += 1
            print(f"{Fore.BLUE}blocked: {Fore.WHITE}"+friend['user']['username']+"#"+friend['user']['discriminator']+Fore.RESET)
        except Exception as e:
            print(f"The following error has been encountered and is being ignored: {e}")


def BlockAll():
    if __name__ == '__main__':
        token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        friendIds = requests.get("https://discord.com/api/v10/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=Block, args=(token, friend))
            t.start()
            processes.append(t)

BlockAll()
