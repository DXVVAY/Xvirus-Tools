import json
import threading

import requests
from colorama import Fore

from util.plugins.common import *


def remove_friend(token, friend_id):
    url = f'https://discord.com/api/v9/users/@me/relationships/{friend_id}'
    response = requests.delete(url, headers=getheaders(token))
    return response.status_code == 204


def UnFriender():
    XTitle("Unfriend All Friends")
    token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
    CheckToken(token)

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships", headers=getheaders(token)).json()

    def batch_remove(start, end):
        removed_friends = []
        for friend in friendIds[start:end]:
            if remove_friend(token, friend['id']):
                removed_friends.append(friend['user']['username'] + "#" + friend['user']['discriminator'])
        return removed_friends

    thread_count = 5
    chunk_size = len(friendIds) // thread_count

    threads = []
    for i in range(thread_count):
        start = i * chunk_size
        end = (i + 1) * chunk_size if i < thread_count - 1 else len(friendIds)
        thread = threading.Thread(target=batch_remove, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    all_removed_friends = [friend for thread in threads for friend in thread.result]
    print(f"{Fore.BLUE} <*> Removed {len(all_removed_friends)} friends:{Fore.RED}")
    for friend in all_removed_friends:
        print(friend + Fore.RESET)
