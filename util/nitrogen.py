import time
import os
import random
import string
import ctypes
import requests
from discord_webhook import DiscordWebhook
from colorama import Fore


class NitroGen:
    def __init__(self):
        self.fileName = "temp/NitroCodes.txt"

    def main(self):
        print("Input How Many Codes to Generate and Check")
        num = int(input("Number of generation: "))
        print("\nDo you wish to use a discord webhook? - [If so type it here or press enter to ignore]")
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
                    k=16
                ))
                url = f"https://discord.gift/{code}"

                result = self.quickChecker(url, webhook)

                if result:
                    valid.append(url)
                else:
                    invalid += 1
            except Exception as e:
                print(f"Error : {url} ")

            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"Nitro Generator and Checker - {len(valid)} Valid | {invalid} Invalid - Made by Xvirus"
                )
                print("")

        print(f"""
Results:
    Valid: {len(valid)}
    Invalid: {invalid}
    Valid Codes: {', '.join(valid)}
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
                    k=16
                ))

                file.write(f"https://discord.gift/{code}\n")

            print(f"Genned {amount} codes | Time taken: {round(time.time() - start, 5)}s\n")

    def fileChecker(self, notify=None):
        valid = []
        invalid = 0
        with open(self.fileName, "r", encoding="utf-8") as file:
            for line in file.readlines():
                nitro = line.strip("\n")

                url = f"https://discord.com/api/v10/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"

                response = requests.get(url)

                if response.status_code == 200:
                    print(f"{Fore.BLUE}VALID NITRO:{Fore.GREEN} {nitro}")
                    valid.append(nitro)

                    if notify is not None:
                        DiscordWebhook(
                            url=notify,
                            content=f"@everyone | A valid Nitro has been found => {nitro}"
                        ).execute()
                    else:
                        break
                else:
                    print(f"{Fore.BLUE}INVALID NITRO:{Fore.RED} {nitro}")
                    invalid += 1

        return {"valid": valid, "invalid": invalid}

    def quickChecker(self, nitro, notify=None):
        url = f"https://discord.com/api/v10/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f"{Fore.BLUE}VALID NITRO:{Fore.GREEN} {nitro}", flush=True, end="" if os.name == 'nt' else "\n")
            with open("temp/NitroCodes.txt", "w") as file:
                file.write(nitro)

            if notify is not None:
                DiscordWebhook(
                    url=notify,
                    content=f"@everyone | A valid Nitro has been found => {nitro}"
                ).execute()

            return True
        else:
            print(f"{Fore.BLUE}INVALID NITRO{Fore.RED} {nitro}", flush=True, end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()
