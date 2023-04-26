import datetime
import time

import requests
from colorama import Fore

def changeVanity(code, server, token, delay):
    response = requests.patch(
        f"https://discord.com/api/v9/guilds/{server}/vanity-url",
        headers={"authorization": token},
        json={"code": code},
    )
    if response.status_code == 200:
        print(
            f"{Fore.GREEN}Updated invite successfully, your server can now be accessed by 'discord.gg/{code}'. {Fore.RESET}"
        )
        return True
    else:
        print(f"{Fore.LIGHTRED_EX} Failed to update vanity url.")
        return False


def checkVanity(url):
    response = requests.get(f"https://discord.com/api/v9/invites/{url}")
    if response.status_code == 404:
        return True
    else:
        print ("")
        print(f"{Fore.LIGHTRED_EX}Vanity is still in use. {Fore.RESET}")
        print ("")
    return False



def snipe():
    token = input(f"{Fore.WHITE}Token: {Fore.RESET}")
    code = input(f"{Fore.WHITE}Vanity code to snipe: {Fore.RESET}")
    serverId = input(f"{Fore.WHITE}ServerID to apply vanity to: {Fore.RESET}")
    delay = int(input(f"{Fore.WHITE}Delay between checks (seconds): {Fore.RESET}"))

    try:
        success = False
        while not success:
            time.sleep(delay)
            success = checkVanity(code)

            curTime = datetime.datetime.now().strftime("%X")
            print(f"{Fore.WHITE}[] Last checked at {curTime} {Fore.RESET}", end="", flush=True)

        changeVanity(code, serverId, token)

    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    snipe()