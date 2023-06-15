import time
import os
import random
import string
import ctypes
import requests
from discord_webhook import DiscordWebhook
from colorama import *


class ServerLinkGen:
    def __init__(self):
        self.fileName = "temp/ServerLinks.txt"

    def main(self):
        print("Input How Many Codes to Generate and Check")
        num = int(input("Number of generations: "))
        print("\nDo you wish to use a discord webhook? - [If so, type it here or press enter to ignore]")
        url = input("WebHook: ")
        time.sleep(1)
        os.system('cls' if os.name == 'nt' else 'clear')
        webhook = url if url != "" else None
        valid = []
        invalid = 0

        for i in range(num):
            try:
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k=7
                ))
                url = f"https://discord.gg/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f"Error: {url}")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Server Link Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Xvirus"
                )
                print("")

        print(f"""
Results:
    Valid: {len(valid)}
    Invalid: {invalid}
    Valid Server Links: {', '.join(valid)}
        """)

        input("Press Enter To Exit!")
        self.main()

    def generator(self, amount):
        with open(self.fileName, "w", encoding="utf-8") as file:
            print("Wait, Generating for you")

            start = time.time()

            for i in range(amount):
                code = "".join(random.choices(
                    string.ascii_uppercase + string.digits + string.ascii_lowercase,
                    k=7
                ))

                file.write(f"https://discord.gg/{code}\n")

            print(f"Genned {amount} server links | Time taken: {round(time.time() - start, 5)}s\n")

    def fileChecker(self, notify=None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                server_link = line.strip("\n")

                url = f"https://discord.com/api/v9/invites/{server_link}"

                response = requests.get(url)

                if response.status_code == 200:
                    print(f"{Fore.BLUE}VALID SERVER LINK:{Fore.GREEN} {server_link}")
                    valid.append(server_link)

                    if notify is not None:
                        DiscordWebhook(
                            url=notify,
                            content=f"@everyone | A valid server link has been found => {server_link}"
                        ).execute()
                    else:
                        break
                else:
                    print(f"{Fore.BLUE}INVALID SERVER LINK:{Fore.RED} {server_link}")
                    invalid += 1

        return {"valid": valid, "invalid": invalid}

    def quickChecker(self, server_link, notify=None):
        url = f"https://discord.com/api/v9/invites/{server_link}"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{Fore.BLUE}VALID SERVER LINK:{Fore.GREEN} {server_link}", flush=True, end="" if os.name == 'nt' else "\n")
            with open("temp/ServerLinks.txt", "w") as file:
                file.write(server_link)

            if notify is not None:
                DiscordWebhook(
                    url=notify,
                    content=f"@everyone | A valid server link has been found => {server_link}"
                ).execute()

            return True
        else:
            print(f"{Fore.BLUE}INVALID SERVER LINK:{Fore.RED} {server_link}", flush=True, end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = ServerLinkGen()
    Gen.main()
