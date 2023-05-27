from websocket import *
import json
import sys
import random
import threading
import time
from colorama import Fore
from util.plugins.common import *


def tokenonliner():
    config = {
        "details": "Description",
        "state": "https://xvirus.xyz/",
        "name": f"Xvirus",
    }

    class Onliner:
        def __init__(self, token) -> None:
            self.token    = token
            self.statuses = ["online", "idle", "dnd"]

        def __online__(self):
            ws = websocket.WebSocket()
            ws.connect("wss://gateway.discord.gg/?encoding=json&v=9")
            response = ws.recv()
            event = json.loads(response)
            heartbeat_interval = int(event["d"]["heartbeat_interval"]) / 1000
            ws.send(
                json.dumps(
                    {
                        "op": 2,
                        "d": {
                            "token": self.token,
                            "properties": {
                                "$os": sys.platform,
                                "$browser": "RTB",
                                "$device": f"{sys.platform} Device",
                            },
                            "presence": {
                                "game": {
                                    "name": config["name"],
                                    "type": 0,
                                    "details": config["details"],
                                    "state": config["state"],
                                },
                                "status": random.choice(self.statuses),
                                "since": 0,
                                "activities": [],
                                "afk": False,
                            },
                        },
                        "s": None,
                        "t": None,
                    }
                )
            )
            b = Fore.BLUE
            print(f"{Fore.RED}[ONLINE] Token {Fore.BLUE}{self.token} {Fore.RED}is online.")

            while True:
                heartbeatJSON = {
                    "op": 1,
                    "token": self.token,
                    "d": "null"
                }
                ws.send(json.dumps(heartbeatJSON))
                time.sleep(heartbeat_interval)

    token = input("Enter your token: ")
    threading.Thread(target=Onliner(token).__online__).start()
    time.sleep(4)
    input(f"Press ENTER to go Back!")
    main()


tokenonliner()
