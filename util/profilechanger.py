import requests
from time import sleep
from colorama import Fore

from util.plugins.common import *


def HouseChanger(token, _type):
    house = {
        1: "Hype Squad Bravery",
        2: "Hype Squad Brilliance",
        3: "Hype Squad Balance",
    }
    # Change HypeSquad
    hypesquad_req = {'house_id': _type}
    requests.post('https://discord.com/api/v10/hypesquad/online', headers=getheaders(token), json=hypesquad_req)
    print(f"\n{Fore.GREEN}Hypesquad changed to {Fore.WHITE}{house[_type]}{Fore.GREEN}\n")
    input("Enter anything to continue. . . ")

def StatusChanger(token, Status):
    # Change status
    custom_status = {"custom_status": {"text": Status}}
    try:
        requests.patch("https://discord.com/api/v10/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_status)
        print(f"\n{Fore.GREEN}Status changed to {Fore.WHITE}{Status}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Error:\n{e}\nOccurred while trying to change the status :/")
    input("Enter anything to continue. . . ")

def BioChanger(token, bio):
    # Change bio
    custom_bio = {"bio": str(bio)}
    try:
        requests.patch("https://discord.com/api/v10/users/@me", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_bio)
        print(f"\n{Fore.GREEN}Bio changed to {Fore.WHITE}{bio}{Fore.GREEN} ")
    except Exception as e:
        print(f"{Fore.RED}Error:\n{e}\nOccurred while trying to change the status :/")
    input("Enter anything to continue. . . ")


def ProfileChanger():
    token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
    print(f'''
        [{Fore.RED}1] Status changer
        [{Fore.RED}2] Bio changer
        [{Fore.RED}3] HypeSquad changer    
    ''')
    secondchoice = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Setting: {Fore.RED}')
    if secondchoice not in ["1", "2", "3"]:
        print(f'[{Fore.RED}Error] : Invalid choice')
        sleep(1)
    if secondchoice == "1":
        status = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Custom Status: {Fore.RED}')
        StatusChanger(token, status)

    if secondchoice == "2":
        bio = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Custom bio: {Fore.RED}')
        BioChanger(token, bio)

    if secondchoice == "3":
        print(f'''
        {Fore.MAGENTA}[1]{Fore.MAGENTA} HypeSquad Bravery
        {Fore.RED}[2]{Fore.LIGHTRED_EX} HypeSquad Brilliance
        {Fore.LIGHTGREEN_EX}[3]{Fore.LIGHTGREEN_EX} HypeSquad Balance
        ''')
        thirdchoice = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Hypesquad: {Fore.RED}')
        if thirdchoice not in ["1", "2", "3"]:
            print(f'[{Fore.RED}Error] : Invalid choice')
            sleep(1)
        if thirdchoice == "1":
            HouseChanger(token, 1)
        if thirdchoice == "2":
            HouseChanger(token, 2)
        if thirdchoice == "3":
            HouseChanger(token, 3)

