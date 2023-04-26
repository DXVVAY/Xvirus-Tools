import datetime
import time
import requests
import os
from colorama import Fore

os.system('cls')

def change_vanity(code: str, server_id: str, token: str) -> bool:
    response = requests.patch(
        f"https://discord.com/api/v9/guilds/{server_id}/vanity-url",
        headers={"authorization": token},
        json={"code": code},
    )
    if response.ok:
        print(f"{Fore.GREEN}Updated invite successfully, your server can now be accessed by 'discord.gg/{code}'. {Fore.RESET}")
        return True
    else:
        print(f"{Fore.LIGHTRED_EX}Failed to update vanity url. Status code: {response.status_code}{Fore.RESET}")
        return False


def check_vanity(code: str) -> bool:
    response = requests.get(f"https://discord.com/api/v9/invites/{code}")
    if response.status_code == 404:
        return True
    else:
        print(f"{Fore.LIGHTRED_EX}Vanity is still in use.{Fore.RESET}")
        return False


def snipe() -> None:
    token = input(f"{Fore.WHITE}Token: {Fore.RESET}")
    code = input(f"{Fore.WHITE}Vanity code to snipe: {Fore.RESET}")
    server_id = input(f"{Fore.WHITE}Server ID to apply vanity to: {Fore.RESET}")
    delay = int(input(f"{Fore.WHITE}Delay between checks (seconds): {Fore.RESET}"))

    try:
        while not check_vanity(code):
            time.sleep(delay)
            cur_time = datetime.datetime.now().strftime("%X")
            print(f"{Fore.WHITE}[] Last checked at {cur_time} {Fore.RESET}", end="", flush=True)

        change_vanity(code, server_id, token)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    snipe()
