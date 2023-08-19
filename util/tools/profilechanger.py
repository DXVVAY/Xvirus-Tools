from time import sleep

import requests
from colorama import Fore

from util.plugins.common import *

def pronounceChanger(token, pronounce):
    pronounce_req = {"pronouns": pronounce}
    requests.patch('https://discord.com/api/v9/users/%40me/profile', headers=getheaders(token), json=pronounce_req)
    print(f" {Fore.RED}<*> Pronounce changed to {Fore.RED}{pronounce}{Fore.RED}\n")
    

def displaynameChanger(token, name):
    displayname_req = {'global_name': name}
    requests.patch('https://discord.com/api/v9/users/@me', headers=getheaders(token), json=displayname_req)
    print(f"\n {Fore.RED} <*> Display name changed to {Fore.BLUE}{name}{Fore.RED}\n")
    

def HouseChanger(token, _type):
    house = {
        1: "Hype Squad Bravery",
        2: "Hype Squad Brilliance",
        3: "Hype Squad Balance",
    }
    hypesquad_req = {'house_id': _type}
    requests.post('https://discord.com/api/v9/hypesquad/online', headers=getheaders(token), json=hypesquad_req)
    print(f"\n {Fore.RED}<*> Hypesquad changed to {Fore.BLUE}{house[_type]}{Fore.RED}\n")
    

def StatusChanger(token, Status):
    custom_status = {"custom_status": {"text": Status}}
    try:
        requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_status)
        print(f"\n {Fore.RED}<*> Status changed to {Fore.BLUE}{Status}{Fore.RED} ")
    except Exception as e:
        print(f" {Fore.RED}<!> Error:\n{e}\nOccurred while trying to change the status :/")
    

def BioChanger(token, bio):
    custom_bio = {"bio": str(bio)}
    try:
        requests.patch("https://discord.com/api/v9/users/@me", proxies={"http": f'{proxy()}'}, headers=getheaders(token), json=custom_bio)
        print(f"\n {Fore.RED}<*> Bio changed to {Fore.BLUE}{bio}{Fore.RED} ")
    except Exception as e:
        print(f" {Fore.RED}<!> Error:\n{e}\nOccurred while trying to change the status :/")
    


def ProfileChanger():
    XTitle("Token Profile Changer")
    token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
    CheckToken(token)
    print(f'''
        [1] Status changer
        [2] Bio changer
        [3] HypeSquad changer   
        [4] Display name changer
        [5] Pronounce Changer
    ''')
    secondchoice = input(f'{Fore.RED} <~> Setting: {Fore.BLUE}')
    if secondchoice not in ["1", "2", "3", "4", "5"]:
        print(f' {Fore.RED}<!> Invalid choice')
        sleep(1)
    if secondchoice == "1":
        status = input(f'{Fore.RED} <~> Custom Status: {Fore.BLUE}')
        StatusChanger(token, status)

    if secondchoice == "2":
        bio = input(f'{Fore.RED} <~> Custom bio: {Fore.BLUE}')
        BioChanger(token, bio)

    if secondchoice == "3":
        print(f'''
        {Fore.MAGENTA}[1]{Fore.MAGENTA} HypeSquad Bravery
        {Fore.RED}[2]{Fore.LIGHTRED_EX} HypeSquad Brilliance
        {Fore.LIGHTGREEN_EX}[3]{Fore.LIGHTGREEN_EX} HypeSquad Balance
        ''')
        thirdchoice = input(f'{Fore.RED} <~> Hypesquad: {Fore.BLUE}')
        if thirdchoice not in ["1", "2", "3"]:
            print(f' {Fore.RED}<!> Invalid choice')
            sleep(1)
        if thirdchoice == "1":
            HouseChanger(token, 1)
        if thirdchoice == "2":
            HouseChanger(token, 2)
        if thirdchoice == "3":
            HouseChanger(token, 3)

    if secondchoice == "4":
        name = input(f"{Fore.RED} <~> Custom DisplayName: {Fore.BLUE}")
        displaynameChanger(token, name)

    if secondchoice == "5":
        pronounce = input(f"{Fore.RED} <~> Custom Pronounce: {Fore.BLUE}")
        pronounceChanger(token, pronounce)