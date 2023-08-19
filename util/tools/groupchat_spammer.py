import random
import threading
from time import sleep

import requests
from colorama import Fore

from util.plugins.common import *


def create_group_chat(token, users):
    while True:
        try:
            response = requests.post(f'https://discord.com/api/v9/users/@me/channels',
                                     proxies={"http": f'{proxy()}'},
                                     headers=getheaders(token),
                                     json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED} <*> Created group chat")
            elif response.status_code == 429:
                print(f"{Fore.BLUE} <!> Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"{Fore.RED} <!> Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break


def selector(token, users):
    threads = []
    for user in users:
        thread = threading.Thread(target=create_group_chat, args=(token, [user]))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


def randomizer(token, IDs):
    threads = []
    while True:
        users = random.sample(IDs, 2)
        thread = threading.Thread(target=create_group_chat, args=(token, users))
        threads.append(thread)
        thread.start()

        if len(threads) >= 50:
            for thread in threads:
                thread.join()
            threads = []


def GcSpammer(token):
    print(f'{Fore.RED} <~> Do you want to choose users yourself to groupchat spam or do you want to select randoms?')
    sleep(1)
    print(f'''
    {Fore.RED}[1] choose users yourself
    {Fore.RED}[2] randomize the users
                        ''')
    secondchoice = int(input(f'{Fore.RED} <~> Second Choice: {Fore.BLUE}'))

    if secondchoice not in [1, 2]:
        print(f'{Fore.RED} <!> Invalid Second Choice')
        sleep(1)

    if secondchoice == 1:
        XTitle(f"Creating group chats")
        recipients = input(f'{Fore.RED} <~> Input the users you want to create a groupchat with (separate by , id,id2,id3): {Fore.BLUE}')
        users = recipients.split(',')
        if "," not in recipients:
            print(f"\n{Fore.RED} <!> You didn't have any commas (,) format is id,id2,id3")
            sleep(3)
        print_slow("\"ctrl + c\" at any time to stop\n")
        sleep(1.5)
        selector(token, users)
    elif secondchoice == 2:
        XTitle(f"Creating group chats")
        IDs = []
        friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships",
                                 proxies={"http": f'http://{proxy()}'},
                                 headers=getheaders(token)).json()
        for friend in friendIds:
            IDs.append(friend['id'])
        print_slow("\"ctrl + c\" at any time to stop\n")
        sleep(1.5)
        randomizer(token, IDs)


def groupspammer():
    XTitle("Groupchat Spammer")
    token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
    CheckToken(token)
    GcSpammer(token)
