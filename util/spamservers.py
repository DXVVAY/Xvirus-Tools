import os
import base64
import multiprocessing
import requests
import random
from colorama import Fore
from util.plugins.common import *

def create_servers(token, icon=None, name=None):
    try:
        payload = {
            'name': name,
            'region': 'europe',
            'icon': icon,
            'channels': None
        }
        response = requests.post(
            'https://discord.com/api/v10/guilds',
            headers=get_headers(token),
            json=payload
        )
        if response.status_code == 201:
            print(f"{Fore.BLUE}Created server: {name}.{Fore.RESET}")
        else:
            print(f"{Fore.RED}Failed to create server: {name}.{Fore.RESET}")
    except Exception as e:
        print(f"{Fore.RED}An error occurred while creating servers: {e}.{Fore.RESET}")
