import requests
import Xvirus

from time import sleep
from colorama import Fore

from util.plugins.common import print_slow, proxy

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
    Xvirus.main()