# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from colorama import Fore
from time import sleep
import tls_client
import threading
import requests
import getpass
import pystyle
import ctypes
import random
import string
import typing
import httpx
import time
import json
import re
import os

from util import *

THIS_VERSION = "1.7.1"

class Config:
    def __init__(self):
        os.system("cls")
        self.folder_path = os.path.join(os.getenv('LOCALAPPDATA'), 'xvirus_free')
        self.file = os.path.join(self.folder_path, 'config.json')
        os.makedirs(self.folder_path, exist_ok=True)
        self.xvirus_files = ['xvirus_tokens', 'xvirus_proxies']
        for file_name in self.xvirus_files:
            file_path = os.path.join(self.folder_path, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as file:
                    pass
        self.content = {
            "xvirus_theme": "RED",
            "xvirus_username": "",
            "use_proxies": False,
            "debug_mode": False
        }
        self.update_config()

    def update_config(self):
        if not os.path.exists(self.file):
            with open(self.file, 'w') as f:
                json.dump(self.content, f, indent=3)
            print(f"{Fore.BLUE}<!> Created Config File")
            pc_username = getpass.getuser()
            self._set("xvirus_username", pc_username)
            sleep(2)
        else:
            existing_config = self._load('config.json')

            if all(key in existing_config for key in self.content.keys()):
                print(f"{Fore.BLUE}<!> Config file is up to date -> {THIS_VERSION}")
                sleep(1)
            else:
                with open(self.file, 'w') as f:
                    json.dump(self.content, f, indent=3)
                print(f"{Fore.BLUE}<!> Config file has been updated to the latest and reset.")
                pc_username = getpass.getuser()
                self._set("xvirus_username", pc_username)
                sleep(2)

    def _load(self, file_name):
        file_path = os.path.join(self.folder_path, file_name)
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError as e:
            print(f"JSON decoding error: {e}")
            return {}

    def _save(self, file_name, data):
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def _set(self, key, value):
        config_data = self._load('config.json')
        config_data[key] = value
        self._save('config.json', config_data)

    def _get(self, key, default=None):
        config_data = self._load('config.json')
        return config_data.get(key, default) if default is not None else config_data.get(key)

    def _remove(self, key):
        config_data = self._load('config.json')
        if key in config_data:
            del config_data[key]
            self._save('config.json', config_data)

    def add(self, file_name, data):
        if file_name not in self.xvirus_files:
            raise ValueError(f"Error: {file_name} is not a valid file name.")
        
        file_path = os.path.join(self.folder_path, file_name)
        with open(file_path, 'a') as file:
            file.write(data + '\n')

    def read(self, file_name):
        if file_name not in self.xvirus_files:
            raise ValueError(f"Error: {file_name} is not a valid file name.")
        
        file_path = os.path.join(self.folder_path, file_name)
        try:
            with open(file_path, 'r') as file:
                return file.read().strip()
        except FileNotFoundError:
            raise FileNotFoundError(f"Error: {file_name} not found.")
    
    def reset(self, file_name):
        if file_name not in self.xvirus_files:
            raise ValueError(f"Error: {file_name} is not a valid file name.")
        
        file_path = os.path.join(self.folder_path, file_name)
        try:
            with open(file_path, 'w') as file:
                pass
        except Exception as e:
            print(f"{e}")

config = Config()

class Output:
    def __init__(self, level, token=None):
        self.level = level
        self.token = token
        self.color_map = {
            "info": (Fore.BLUE, "<*>"),
            "bad": (Fore.RED, "<!>"),
            "good": (Fore.GREEN, "<+>"),
            "dbg": (Fore.MAGENTA, "</>"),
        }

    def should_hide(self):
        return not config._get('debug_mode', True)

    def hide_token(self, text):
        if self.should_hide() and self.token:
            token_length = len(self.token)
            if token_length >= 10:
                censored_part = '*' * 10
                text = text.replace(self.token[-10:], censored_part)
        return text

    def notime(self, *args, **kwargs):
        color, text = self.color_map.get(self.level, (Fore.LIGHTWHITE_EX, self.level))
        base = f"{color}{text.upper()}"
        for arg in args:
            arg = self.hide_token(arg)
            base += f" {arg}"
        if kwargs:
            for key, value in kwargs.items():
                value = self.hide_token(value)
                base += f" {key}={value}"
        print(base)

    def log(self, *args, **kwargs):
        color, text = self.color_map.get(self.level, (Fore.LIGHTWHITE_EX, self.level))
        time_now = datetime.now().strftime("%H:%M:%S")
        base = f"{Fore.RED}│{Fore.BLUE}{time_now}{Fore.RED}│ {color}{text.upper()}"
        updated_args = []

        for arg in args:
            arg = self.hide_token(arg)
            updated_args.append(arg)

        for arg in updated_args:
            base += f" {arg}"

        if kwargs:
            for key, value in kwargs.items():
                value = self.hide_token(value)
                base += f" {key}={value}"
        print(base)

    @staticmethod
    def PETC():
        print()
        Output("info").notime(f"Press ENTER to continue")
        input()
        __import__("Xvirus").gui.main_menu()
    
    @staticmethod
    def set_title(text):
        system = os.name
        if system == 'nt':
            ctypes.windll.kernel32.SetConsoleTitleW(f"{text} - Discord API Tool | https://xvirus.lol | Made By Xvirus™")
        else:
            pass

    # PLEASE IGNORE THIS IK ITS SHIT WOW
    @staticmethod
    def error_logger(token, res_text, res_status_code):
        errors = {
            '{"captcha_key"': "(Captcha)",
            '{"message": "401: Unauthorized': "(Unauthorized)",
            'Cloudflare': "(CloudFlare Blocked)",
            '\"code\": 40007': "(Token Banned)",
            '\"code\": 40002': "(Locked Token)",
            '\"code\": 10006': "(Invalid Invite)",
            '\"code\": 10004': "(Not In Server)",
            '\"code\": 50013:': "(No Access)",
            '\"code\": 50001:': "(No Access)",
            'Unknown Message': "(Unknown)",
            '\"code\": 50033:': "(Invalid Recipient)"
        }

        for key, value in errors.items():
            if key in res_text:
                Output("bad", token).log(f"Error -> {token} {Fore.LIGHTBLACK_EX}({res_status_code}) {Fore.RED}{value}")
                return

        Output("bad", token).log(f"Error -> {token} {Fore.LIGHTBLACK_EX}({res_status_code}) {Fore.RED}({res_text})")


# static headers which might get flagged over the time ong
headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'sv,sv-SE;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9016 Chrome/108.0.5359.215 Electron/22.3.12 Safari/537.36',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Europe/Stockholm',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDE2Iiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDUiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6InN2IiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMTYgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMTIgU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6IjIyLjMuMTIiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyMTg2MDQsIm5hdGl2ZV9idWlsZF9udW1iZXIiOjM1MjM2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',}

class Client:
    def get_cookies(session):
        cookies = dict(
            session.get("https://discord.com").cookies
        )
        cookies["__cf_bm"] = (
            "0duPxpWahXQbsel5Mm.XDFj_eHeCKkMo.T6tkBzbIFU-1679837601-0-"
            "AbkAwOxGrGl9ZGuOeBGIq4Z+ss0Ob5thYOQuCcKzKPD2xvy4lrAxEuRAF1Kopx5muqAEh2kLBLuED6s8P0iUxfPo+IeQId4AS3ZX76SNC5F59QowBDtRNPCHYLR6+2bBFA=="
        )
        cookies["locale"] = "en-US"
        return cookies

    def get_session(token:str):
        session = tls_client.Session(
            client_identifier=f"chrome_{random.randint(110, 116)}",
            random_tls_extension_order = True
        )  

        session.headers = headers
        session.headers.update({"Authorization": token})

        cookie = Client.get_cookies(session)
        session.headers.update({
            "cookie": f"__cfruid={cookie['__cfruid']}; __dcfduid={cookie['__dcfduid']}; __sdcfduid={cookie['__sdcfduid']}",
        })
        
        if config._get("use_proxies"):
            proxy = ProxyManager.clean_proxy(ProxyManager.random_proxy())
            if isinstance(proxy, str):
                proxy_dict = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}"
                }
            elif isinstance(proxy, dict):
                proxy_dict = proxy

            session.proxies = proxy_dict

        return session

    def get_simple_session() -> tls_client.Session:
        session = tls_client.Session(
            client_identifier=f"chrome_{random.randint(110, 116)}",
            random_tls_extension_order=True
        )   

        if config._get("use_proxies"):
            proxy = ProxyManager.clean_proxy(ProxyManager.random_proxy())
            if isinstance(proxy, str):
                proxy_dict = {
                    "http": f"http://{proxy}",
                    "https": f"http://{proxy}"
                }
            elif isinstance(proxy, dict):
                proxy_dict = proxy
            session.proxies = proxy_dict

        return session

class ProxyManager:
    def get_proxies():
        f = config.read('xvirus_proxies')
        proxies = f.strip().splitlines()
        proxies = [proxy for proxy in proxies if proxy not in [" ", "", "\n"]]
        return proxies
        
    def random_proxy():
        try:
            return random.choice(ProxyManager.get_proxies())
        except:
            return {}

    def clean_proxy(proxy):
        if isinstance(proxy, str):
            parts = proxy.split(':')
            if '@' in proxy or len(parts) == 2:
                return proxy
            elif len(parts) == 4:
                return f'{parts[2:]}@{parts[:2]}'
            elif '.' in parts[0]:
                return f'{parts[2:]}@{parts[:2]}'
            else:
                return f'{parts[:2]}@{parts[2:]}'
        elif isinstance(proxy, dict):
            http_proxy = proxy.get("http") or proxy.get("https")
            https_proxy = proxy.get("https") or proxy.get("http")
            if http_proxy or https_proxy:
                return {
                    "http://": http_proxy,
                    "https://": https_proxy
                }
            elif proxy in [dict(), {}]:
                return {}
        return proxy

class TokenManager:
    @classmethod
    def get_tokens(cls):
        f = config.read('xvirus_tokens')
        tokens = f.strip().splitlines()
        tokens = [token for token in tokens if token not in [" ", "", "\n"]]
        return tokens
    
    @classmethod
    def custom_path(cls, custom_path):
        try:
            with open(custom_path, 'r') as file:
                tokens = file.read().strip().splitlines()
                tokens = [token for token in tokens if token.strip()]
                return tokens
        except FileNotFoundError:
            Output("bad").notime(f"File not found: {custom_path}")
            return None

    @staticmethod
    def OnlyToken(tokenn):
        r = re.compile(r"(.+):(.+):(.+)")
        if r.match(tokenn):
            return tokenn.split(":")[2]
        else:
            token = tokenn
        return token
    
    @classmethod
    def delete_token(cls, token):
        f = Config.read('xvirus_tokens')
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if token not in line:
                f.write(line)
        f.truncate()
    
    @classmethod
    def get_random_token(cls):
        tokens = cls.get_tokens()
        if tokens:
            return random.choice(tokens)
        else:
            return None

class Checker:
    def __init__(self, typ, thing):
        if typ == 'token':
            session= Client.get_session(thing)
            response = session.get('https://discord.com/api/v9/users/@me')
            if response.status_code == 200:
                json_data = response.json()
                name = json_data.get["username"]
                Output("good").log(f"Valid Token! ({name})")
            else:
                Output("bad").log("Invalid Token.")
                sleep(1)
                __import__("Xvirus").gui.main_menu()

        elif typ == 'webhook':
            response = requests.get(thing)
            if response.status_code == 200:
                json_data = response.json()
                name = json_data.get("name", "Webhook")
                Output("good").log(f"Valid webhook! ({name})")
            else:
                Output("bad").log("Invalid Webhook.")
                sleep(1)
                __import__("Xvirus").gui.main_menu()
        else:
            pass

class utility:
    def clear():
        system = os.name
        if system == 'nt':
            os.system('cls')
        else:
            print('\n'*120)
        return

    def rand_str(length:int) -> str:
        return ''.join(random.sample(string.ascii_lowercase+string.digits, length))

    def make_menu(*options):
        print()
        for num, option in enumerate(options, start=1):
            label = f"    {Fore.BLUE}[{Fore.RED}{num}{Fore.BLUE}] {Fore.RED}{option}"
            print(label)
        print()
    
    def ask(text: str = ""):
        ask = input(f"{Fore.RED}<~> {text}: {Fore.BLUE}")
        if ask == "back":
            Output("info").notime(f"Going Back...")
            sleep(2)
            __import__("Xvirus").gui.main_menu()
        return ask

    def message_info(message_link = None):
        if message_link is None:
            message_link = utility.ask("Message link")
        pattern = re.compile(r"^https:\/\/(ptb\.|canary\.)?discord\.com\/channels\/\d+\/\d+\/\d+$")
        if pattern.match(message_link):
            link_parts = message_link.split("/")
            guild_id, channel_id, message_id = link_parts[4], link_parts[5], link_parts[6]
            return {
                "guild_id": guild_id,
                "channel_id": channel_id,
                "message_id": message_id
            }
        else:
            Output("bad").notime("Invalid message link")
            return None

    def run_threads(max_threads, func, args=[]):
        def thread_complete(future):
            debug = config._get("debug_mode")
            try:
                result = future.result()
            except Exception as e:
                if debug:
                    if "failed to do request" in str(e):
                        message = f"Proxy Error -> {str(e)[:80]}..."
                    else:
                        message = f"Error -> {e}"
                    Output("dbg").log(message)
                else:
                    pass

        tokens = TokenManager.get_tokens()
        max_threads = int(max_threads)

        if tokens:
            with ThreadPoolExecutor(max_workers=max_threads) as executor:
                for token in tokens:
                    try:
                        token = TokenManager.OnlyToken(token)
                        args.append(token)
                        future = executor.submit(func, *args)
                        future.add_done_callback(thread_complete)
                        args.remove(token)
                    except Exception as e:
                        Output("bad").log(f"{e}")

            Output.PETC()
        else:
            Output("bad").log(f"No tokens were found in cache")
            Output.PETC()
    
    def get_server_name(invite):
        req = requests.get(f"https://discord.com/api/v9/invites/{invite}?with_counts=true&with_expiration=true")
        if req.status_code == 200:
            res = req.json()
            name = res['guild']['name']
            return name
        else:
            return None
