from time import sleep

import requests
from colorama import Fore

from util.plugins.common import *


def WebhookSpammer(WebHook, Message):
    print_slow("\"ctrl + c\" at anytime to stop\n")
    sleep(1.5)
    #spam the webhook with the message 
    while True:
        response = requests.post(
            WebHook,
            proxies={"http": f'{proxy()}'},
            json = {"content" : Message},
            params = {'wait' : True}
        )
        try:
            #check if the status got sent or if it got rate limited
            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.GREEN}Message sent")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms)")
                #if we got ratelimited, pause untill the rate limit is over
                sleep(response.json()["retry_after"] / 1000)
            else:
                print(f"{Fore.RED}Error : {response.status_code}")

            sleep(.01)
        except KeyboardInterrupt:
            break

    print_slow(f'{Fore.RED}Spammed Webhook Successfully! ')
    print("Enter anything to continue. . . ", end="")
    input()

def webhooktool():
    print(f'''
    {Fore.RED}[1] Webhook Deleter
    {Fore.RED}[2] Webhook Spammer    
                        ''')
    secondchoice = int(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Second Choice: {Fore.RED}'))
    if secondchoice not in [1, 2]:
        print(f'[{Fore.RED}Error] : Invalid Second Choice')
        sleep(1)
        main()
    if secondchoice == 1:
        WebHook = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Webhook: {Fore.RED}')
        validateWebhook(WebHook)
        try:
            requests.delete(WebHook)
            print(f'\n{Fore.GREEN}Webhook Successfully Deleted!\n')
        except Exception as e:
            print(f'{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook')

        input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Enter anything to continue. . . {Fore.RED}')
        main()
    if secondchoice == 2:
        WebHook = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Webhook: {Fore.RED}')
        validateWebhook(WebHook)
        Message = str(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message: {Fore.RED}'))
        WebhookSpammer(WebHook, Message)