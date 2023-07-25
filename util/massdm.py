import requests
from colorama import Fore
import multiprocessing
from util.plugins.common import *

def massdm():
    def send_message(channel_id, token, message):
        for channel in channel_id:
            for user in [x["username"] + "#" + x["discriminator"] for x in channel["recipients"]]:
                try:
                    setTitle(f"Messaging " + user)
                    requests.post(f'https://discord.com/api/v10/channels/{channel["id"]}/messages',
                                  proxies={"http": f'{proxy()}'},
                                  headers=getheaders(token),
                                  data={"content": f"{message}"})
                    print(f"{Fore.RED}Messaged: {Fore.WHITE}" + user + Fore.RESET)
                except Exception as e:
                    print(f"The following error has been encountered and is being ignored: {e}")

    token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
    validateToken(token)
    message = str(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message that will be sent to every friend: {Fore.RED}'))

    channelIds = requests.get("https://discord.com/api/v10/users/@me/channels", headers=getheaders(token)).json()

    processes = []
    for channel in [channelIds[i:i + 3] for i in range(0, len(channelIds), 3)]:
        t = multiprocessing.Process(target=send_message, args=(channel, token, message))
        t.start()
        processes.append(t)

    for process in processes:
        process.join()