import time
from pypresence import Presence
from colorama import Fore
from util.plugins.common import *

client_id = '1138850967522132119'

RPC = Presence(client_id)

rpc_enabled = False

details = "Using Xvirus"
state = "The Most Advanced Multi Tool"
large_image = "icon"
small_image = "icon"
start_time = int(time.time())

def toggle_rpc():
    global rpc_enabled

    if rpc_enabled:
        try:
            RPC.close()
        except:
            pass

        print(f" {Fore.BLUE}<*> Custom Discord RPC turned {Fore.RED}OFF{Fore.RESET}")
        sleep(1.5)
    else:
        try:
            RPC.connect()
            RPC.update(
                details=details,
                state=state,
                large_image=large_image,
                small_image=small_image,
                start=start_time,
                buttons=[
                    {"label": "Discord", "url": "https://discord.gg/xvirus"},
                    {"label": "Website", "url": "https://xvirus.xyz"}
                ]
            )
        except:
            pass  

        print(f" {Fore.RED}<*> Custom Discord RPC turned {Fore.BLUE}ON{Fore.RESET}")
        sleep(1.5)

    rpc_enabled = not rpc_enabled

