import requests
import Xvirus
from colorama import Fore

from util.plugins.common import print_slow, getheaders, proxy

def HouseChanger(token, _type):
    house = {
        1: "Hype Squad Bravery",
        2: "Hype Squad Brilliance",
        3: "Hype Squad Balance",
    }
    #change hypesquad
    hypesqad_req = {'house_id': _type}
    requests.post('https://discord.com/api/v9/hypesquad/online', headers=getheaders(token), json=hypesqad_req)
    print_slow(f"\n{Fore.GREEN}Hypesquad changed to {Fore.WHITE}{house[_type]}{Fore.GREEN} ")
    print("Enter anything to continue. . . ", end="")
    input()
    Xvirus.main()

def StatusChanger(token, Status):
    #change status 
    custom_status = {"custom_status": {"text": Status}} #{"text": Status, "emoji_name": "☢"} if you want to add an emoji to the status
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_status)
        print_slow(f"\n{Fore.GREEN}Status changed to {Fore.WHITE}{Status}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Error:\n{e}\nOccurred while trying to change the status :/")
    print("Enter anything to continue. . . ", end="")
    input()
    Xvirus.main()

def BioChanger(token, bio):
    #change bio
    custom_bio = {"bio": str(bio)}
    try:
        requests.patch("https://discord.com/api/v9/users/@me", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_bio)
        print_slow(f"\n{Fore.GREEN}Bio changed to {Fore.WHITE}{bio}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Error:\n{e}\nOccurred while trying to change the status :/")
    print("Enter anything to continue. . . ", end="")
    input()
    Xvirus.main()
