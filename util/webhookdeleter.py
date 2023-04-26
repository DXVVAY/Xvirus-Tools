import requests
from colorama import Fore
hook = input(f"{Fore.WHITE}Webhook URL: {Fore.RESET}")

def delete(webhook):
    requests.delete(webhook)
    check = requests.get(webhook)
    if check.status_code == 404:
        print(f"{Fore.GREEN} \n [STATUS] WEBHOOK DELETED")
        {Fore.RESET}
    elif check.status_code == 200:
        print("{Fore.RED} \n [STATUS] FAILED TO DELETE WEBHOOK")
{Fore.RESET}
value = 1
if value == 1:
    delete(hook)

