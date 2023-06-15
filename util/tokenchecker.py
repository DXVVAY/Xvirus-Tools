import requests
import threading
import time
from colorama import Fore

def tokenchecker():

    def check_token(token, valid_tokens, invalid_tokens, locked_tokens):
        try:
            response = requests.get('https://discord.com/api/v9/users/@me/library', headers={"authorization": token,"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36","x-discord-locale": "de-DE"})
            if response.status_code == 200:
                with lock:
                    valid_tokens.append(token)
                print(f"({Fore.GREEN}+){Fore.LIGHTGREEN_EX} [VALID] {Fore.LIGHTBLACK_EX}{token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
            elif response.status_code == 401 or response.status_code == 403:
                with lock:
                    locked_tokens.append(token)
                print(f"({Fore.YELLOW}~){Fore.LIGHTYELLOW_EX} [LOCKED] {Fore.LIGHTBLACK_EX}{token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
            elif response.status_code == 404:
                with lock:
                    invalid_tokens.append(token)
                print(f"({Fore.RED}-){Fore.LIGHTRED_EX} [INVALID] {Fore.LIGHTBLACK_EX}{token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
            else:
                print(f"({Fore.RED}-){Fore.LIGHTRED_EX} [ERROR] {Fore.LIGHTBLACK_EX}{token}{Fore.LIGHTBLACK_EX} ({response.status_code})")
        except:
            with lock:
                locked_tokens.append(token)
            print(f"({Fore.YELLOW}~){Fore.LIGHTYELLOW_EX} [LOCKED] {Fore.LIGHTBLACK_EX}{token} (Error)")
        time.sleep(1)

    path = input("Enter the path to the tokens file: ")
    with open(path, 'r') as f:
        tokens = [line.strip() for line in f.readlines()]

    valid_tokens = []
    invalid_tokens = []
    locked_tokens = []
    lock = threading.Lock()
    threads = []

    for token in tokens:
        t = threading.Thread(target=check_token, args=(token, valid_tokens, invalid_tokens, locked_tokens))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("\n")
    input(f"        {Fore.LIGHTGREEN_EX}Valid: {len(valid_tokens)}    |   {Fore.LIGHTRED_EX}Invalid: {len(invalid_tokens)}   |   {Fore.YELLOW}Locked: {len(locked_tokens)} "+ "\n" * 3)

    with open(path, 'w') as f:
        for token in valid_tokens:
            f.write(token + "\n")

tokenchecker()           
