import threading
import time

import requests
from colorama import Fore
from util.plugins.common import *

def check_token(token, valid_tokens, invalid_tokens, locked_tokens, lock):
    headers = {'authorization': token}
    try:
        response = requests.get('https://discord.com/api/v10/users/@me/library', headers=headers)
        if response.status_code == 200:
            with lock:
                valid_tokens.append(token)
            print(f"{Fore.GREEN}[Valid]{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
        elif response.status_code == 401 or response.status_code == 403:
            with lock:
                locked_tokens.append(token)
            print(f"{Fore.LIGHTBLACK_EX}[Locked]{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
        elif response.status_code == 404:
            with lock:
                invalid_tokens.append(token)
            print(f"{Fore.RED}[Invalid]{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
        else:
            print(f"{Fore.LIGHTRED_EX}[Error]{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
    except:
        with lock:
            locked_tokens.append(token)
        print(f"{Fore.LIGHTBLACK_EX}[Locked]{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} (Error)")
    time.sleep(1)

def tokenchecker():
    path = input("Enter the path to the tokens file: ")
    with open(path, 'r') as f:
        tokens = [line.strip() for line in f.readlines()]

    valid_tokens = []
    invalid_tokens = []
    locked_tokens = []
    lock = threading.Lock()
    threads = []

    for token in tokens:
        t = threading.Thread(target=check_token, args=(token, valid_tokens, invalid_tokens, locked_tokens, lock))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n")
    input(f"{Fore.GREEN}Valid: {len(valid_tokens)}{Fore.RED}\nInvalid: {len(invalid_tokens)}{Fore.LIGHTBLACK_EX}\nLocked: {len(locked_tokens)} ")

    with open(path, 'w') as f:
        for token in valid_tokens:
            f.write(token + "\n")

