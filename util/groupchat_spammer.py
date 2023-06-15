import requests
import random
import Xvirus

from time import sleep
from colorama import Fore

from util.plugins.common import print_slow, setTitle, getheaders, proxy

def selector(token, users):
    while True:
        try:
            response = requests.post(f'https://discord.com/api/v10/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Created groupchat")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"{Fore.RED}Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Xvirus.main()

def randomizer(token, ID):
    while True:
        users = random.sample(ID, 2)
        try:
            response = requests.post(f'https://discord.com/api/v10/users/@me/channels', proxies={"http": f'{proxy()}'}, headers=getheaders(token), json={"recipients": users})

            if response.status_code == 204 or response.status_code == 200:
                print(f"{Fore.RED}Created groupchat")
            elif response.status_code == 429:
                print(f"{Fore.YELLOW}Rate limited ({response.json()['retry_after']}ms)")
            else:
                print(f"{Fore.RED}Error: {response.status_code}")
        except Exception:
            pass
        except KeyboardInterrupt:
            break
    Xvirus.main()


def GcSpammer(token):
    print(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] Do you want to choose users yourself to groupchat spam or do you want to select randoms?')
    sleep(1)
    print(f'''
    {Fore.RED}[1] choose users yourself
    {Fore.RED}[2] randomize the users
                        ''')
    secondchoice = int(input(
        f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Second Choice: {Fore.RED}'))

    if secondchoice not in [1, 2]:
        print(f'[{Fore.RED}Error] : Invalid Second Choice')
        sleep(1)
        Xvirus.main()

    #if they choose to import the users manually
    if secondchoice == 1:
        setTitle(f"Creating groupchats")
        #if they choose specific users
        recipients = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Input the users you want to create a groupchat with (separate by , id,id2,id3): {Fore.RED}')
        user = recipients.split(',')
        if "," not in recipients:
            print(f"\n{Fore.RED}You didn't have any commas (,) format is id,id2,id3")
            sleep(3)
            Xvirus.main()
        print_slow("\"ctrl + c\" at anytime to stop\n")
        sleep(1.5)
        selector(token, user)

    #if they choose to randomize the selection
    elif secondchoice == 2:
        setTitle(f"Creating groupchats")
        IDs = []
        #Get all users to spam groupchats with
        friendIds = requests.get("https://discord.com/api/v10/users/@me/relationships", proxies={"http": f'http://{proxy()}'}, headers=getheaders(token)).json()
        for friend in friendIds:
            IDs.append(friend['id'])
        print_slow("\"ctrl + c\" at anytime to stop\n")
        sleep(1.5)
        randomizer(token, IDs)