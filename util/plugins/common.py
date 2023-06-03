import os
import re
import io
import sys
import time
import json
import ctypes
import random
import zipfile
import requests
import pkg_resources
import subprocess
import threading
import multiprocessing
import keyboard
import base64
import colorama
import shutil
import os.path
import string
import tempfile
from zipfile import ZipFile
from time import sleep
from colorama import Fore
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from distutils.version import LooseVersion
from bs4 import BeautifulSoup
import urllib.request
from urllib.request import urlopen, urlretrieve

def CHANGE_LOG():
    input(f'''
    1. New GUI
    2. Username system
    3. Discord onliner
    4. Discord server link gen
    5. Token onliner''')
    
THIS_VERSION = "1.6.1"
TARGET_VERSION = 0

def search_for_updates():
    clear()
    setTitle("Xvirus Checking For Updates. . .")
    
    latest_version_url = "https://cloud.xvirus.xyz/latest_version.txt"
    r = requests.get(latest_version_url)
    latest_version = r.text.strip()

    if THIS_VERSION != latest_version:
        setTitle("New Update Found!")
        print(
            f"""{Fore.YELLOW}
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗  ██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝  ██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗    ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝    ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗  ██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝  ╚═╝
                              {Fore.RED}Looks like Xvirus {THIS_VERSION} is outdated """.replace(
                "█", f"{Fore.WHITE}█{Fore.RED}"
            ),
            end="\n\n",
        )

        update_url = f"https://cloud.xvirus.xyz/Xvirus-Tools-main.zip"
        choice = input(
            f"{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Do you want to update to the latest version? (Y to update N to continue using this version): {Fore.RED}"
        )

        if choice.lower() == "y" or choice.lower() == "yes":
            print(f"{Fore.WHITE}\nUpdating. . .")
            setTitle(f"Xvirus Updating...")
            new_version_source = requests.get(update_url)
            with open("Xvirus-Tools-main.zip", "wb") as zipfile:
                zipfile.write(new_version_source.content)
            with ZipFile("Xvirus-Tools-main.zip", "r") as filezip:
                filezip.extractall()
            os.remove("Xvirus-Tools-main.zip")
            cwd = os.getcwd() + "\\Xvirus-Tools-main"
            shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
            shutil.rmtree(cwd)
            setTitle("Xvirus Update Complete!")
            print(f"{Fore.GREEN}Update Successfully Finished!")
            sleep(2)
            if os.path.exists(os.getcwd() + "setup.bat"):
                os.startfile("setup.bat")
            elif os.path.exists(os.getcwd() + "start.bat"):
                os.startfile("start.bat")
            os._exit(0)


def update():
    clear()
    setTitle("Xvirus Checking For Updates. . .")

    setTitle("New Update Found!")
    print(
        f"""{Fore.YELLOW}
        ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗  ██╗
        ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝  ██║
        ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗    ██║
        ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝    ╚═╝
        ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗  ██╗
         ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝  ╚═╝
        {Fore.RED}Looks like your Xvirus is outdated """.replace(
            "█", f"{Fore.WHITE}█{Fore.RED}"
        ),
        end="\n\n",
    )

    update_url = f"https://github.com/Xvirus0/Xvirus-Tools/archive/refs/heads/main.zip"
    choice = input(
        f"{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Do you want to update to the latest dev branch (Remember that the dev branch might be unstable)? (Y to update N to continue using this version): {Fore.RED}"
    )

    if choice.lower() == "y" or choice.lower() == "yes":
        print(f"{Fore.WHITE}\nUpdating. . .")
        setTitle(f"Xvirus Updating...")
        new_version_source = requests.get(update_url)
        with open("Xvirus-Tools-main.zip", "wb") as zipfile:
            zipfile.write(new_version_source.content)
        with ZipFile("Xvirus-Tools-main.zip", "r") as filezip:
            filezip.extractall()
        os.remove("Xvirus-Tools-main.zip")
        cwd = os.getcwd() + "\\Xvirus-Tools-main"
        shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
        shutil.rmtree(cwd)
        setTitle("Xvirus Update Complete!")
        print(f"{Fore.GREEN}Update Successfully Finished!")
        sleep(2)
        if os.path.exists(os.getcwd() + "setup.bat"):
            os.startfile("setup.bat")
        elif os.path.exists(os.getcwd() + "start.bat"):
            os.startfile("start.bat")
        os._exit(0)


class Chrome_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://chromedriver.storage.googleapis.com/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if TARGET_VERSION:
            self.target_version = TARGET_VERSION

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "chromedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_chromedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open(self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect


    def get_release_version_number(self):
        path = (
            "LATEST_RELEASE"
            if not self.target_version
            else f"LATEST_RELEASE_{self.target_version}"
        )
        return LooseVersion(urlopen(self.__class__.DL_BASE + path).read().decode())

    def fetch_chromedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract(self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Edge_Installer(object):
    installed = False
    target_version = None
    DL_BASE = "https://msedgedriver.azureedge.net/"

    def __init__(self, executable_path=None, target_version=None, *args, **kwargs):
        self.platform = sys.platform

        if TARGET_VERSION:
            self.target_version = TARGET_VERSION

        if target_version:
            self.target_version = target_version

        if not self.target_version:
            self.target_version = self.get_release_version_number().version[0]

        self._base = base_ = "edgedriver{}"

        exe_name = self._base
        if self.platform in ("win32",):
            exe_name = base_.format(".exe")
        if self.platform in ("linux",):
            self.platform += "64"
            exe_name = exe_name.format("")
        if self.platform in ("darwin",):
            self.platform = "mac64"
            exe_name = exe_name.format("")
        self.executable_path = executable_path or exe_name
        self._exe_name = exe_name

        if not os.path.exists(self.executable_path):
            self.fetch_edgedriver()
            if not self.__class__.installed:
                if self.patch_binary():
                    self.__class__.installed = True

    @staticmethod
    def random_cdc():
        cdc = random.choices('abcdefghijklmnopqrstuvwxyz', k=26)
        cdc[-6:-4] = map(str.upper, cdc[-6:-4])
        cdc[2] = cdc[0]
        cdc[3] = "_"
        return "".join(cdc).encode()

    def patch_binary(self):
        linect = 0
        replacement = self.random_cdc()
        with io.open("ms"+self.executable_path, "r+b") as fh:
            for line in iter(lambda: fh.readline(), b""):
                if b"cdc_" in line:
                    fh.seek(-len(line), 1)
                    newline = re.sub(b"cdc_.{22}", replacement, line)
                    fh.write(newline)
                    linect += 1
            return linect


    def get_release_version_number(self):
        path = (
            "LATEST_STABLE"
            if not self.target_version
            else f"LATEST_RELEASE_{str(self.target_version).split('.', 1)[0]}"
        )
        urlretrieve(
            f"{self.__class__.DL_BASE}{path}",
            filename=f"{os.getenv('temp')}\\{path}",
        )
        with open(f"{os.getenv('temp')}\\{path}", "r+") as f:
            _file = f.read().strip("\n")
            content = ""
            for char in [x for x in _file]:
                for num in ("0","1","2","3","4","5","6","7","8","9","."):
                    if char == num:
                        content += char
        return LooseVersion(content)

    def fetch_edgedriver(self):
        base_ = self._base
        zip_name = base_.format(".zip")
        ver = self.get_release_version_number().vstring
        if os.path.exists(self.executable_path):
            return self.executable_path
        print(f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip")
        urlretrieve(
            f"{self.__class__.DL_BASE}{ver}/{base_.format(f'_{self.platform}')}.zip",
            filename=zip_name,
        )
        with zipfile.ZipFile(zip_name) as zf:
            zf.extract("ms"+self._exe_name)
        os.remove(zip_name)
        if sys.platform != "win32":
            os.chmod(self._exe_name, 0o755)
        return self._exe_name

class Opera_Installer(object):
    _os_bit = 64
    def __init__(self, *args, **kwargs):
        if os.environ.get('PROCESSOR_ARCHITECTURE').lower() == 'x86' and os.environ.get('PROCESSOR_ARCHITEW6432') is None: 
            self.__class__._os_bit = 32
            
        r = requests.get("https://github.com/operasoftware/operachromiumdriver/releases")
        soup = str(BeautifulSoup(r.text, 'html.parser'))
        print(soup.get_text())

def get_driver():
    #supported drivers
    drivers = ["chromedriver.exe", "msedgedriver.exe", "operadriver.exe"]

    print(f"\n{Fore.BLUE}Checking Driver. . .")
    sleep(0.5)

    for driver in drivers:
        #Checking if driver already exists
        if os.path.exists(os.getcwd() + os.sep + driver):
            print(f"{Fore.GREEN}{driver} already exists, continuing. . .{Fore.RESET}")
            sleep(0.5)
            return driver
    else:
        print(f"{Fore.RED}Driver not found! Installing it for you")
        #get installed browsers + install driver + return correct driver
        if os.path.exists(os.getenv('localappdata') + '\\Google'):
            Chrome_Installer()
            print(f"{Fore.GREEN}chromedriver.exe Installed!{Fore.RESET}")
            return "chromedriver.exe"
        elif os.path.exists(os.getenv('appdata') + '\\Opera Software\\Opera Stable'):
            Opera_Installer()
            print(f"{Fore.GREEN}operadriver.exe Installed!{Fore.RESET}")
            return "operadriver.exe"
        elif os.path.exists(os.getenv('localappdata') + '\\Microsoft\\Edge'):
            Edge_Installer()
            print(f"{Fore.GREEN}msedgedriver.exe Installed!{Fore.RESET}")
            return "msedgedriver.exe"
        else:
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : No compatible driver found. . . Proceeding with chromedriver')
            Chrome_Installer()
            print(f"{Fore.GREEN}trying to install chromedriver.exe{Fore.RESET}")
            return "chromedriver.exe"

def clear():
    system = os.name
    if system == 'nt':
        #if its windows
        os.system('cls')
    elif system == 'posix':
        #if its linux
        os.system('clear')
    else:
        print('\n'*120)
    return

def setTitle(_str):
    system = os.name
    if system == 'nt':
        #if its windows
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} | Made By Xvirus")
    elif system == 'posix':
        #if its linux
        os.system(f"\033]0;{_str} | Made By Xvirus\a", end='', flush=True)
    else:
        #if its something else or some err happend for some reason, we do nothing
        pass

def print_slow(_str):
    for letter in _str:
        #slowly print out the words 
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def validateToken(token):
    headers = getheaders(token)
    url = 'https://discord.com/api/v10/users/@me'
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print(f"{Fore.GREEN}Valid Token.{Fore.RESET}")
        # Token is valid
    else:
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)
        __import__("Xvirus").main()

def validateWebhook(hook):
    try:
        response = requests.get(hook)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        sleep(1)
        __import__("Xvirus").main()

    try:
        json_data = response.json()
        j = json_data["name"]
        print(f"{Fore.GREEN}Valid webhook! ({j})")
    except (KeyError, json.decoder.JSONDecodeError):
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        sleep(1)


def fetch_proxies(url, custom_regex, proxies_log):
    try:
        proxy_list = requests.get(url, timeout=5).text
        proxy_list = proxy_list.replace('null', '')
    except requests.exceptions.RequestException:
        return

    custom_regex = custom_regex.replace('%ip%', r'([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})')
    custom_regex = custom_regex.replace('%port%', r'([0-9]{1,5})')

    for proxy in re.findall(re.compile(custom_regex), proxy_list):
        proxies_log.append(f"{proxy[0]}:{proxy[1]}")


def proxy_scrape():
    temp_path = os.path.join(os.getenv("temp"), "xvirus_proxies")

    if os.path.isfile(temp_path) and os.stat(temp_path).st_size > 0:
        return

    proxies_log = []
    setTitle("Scraping Proxies")
    start_time = time.time()

    while True:
        Anime.Fade((logo), Colors.rainbow, Colorate.Vertical, time=5)
        proxy_sources = [
            ["http://spys.me/proxy.txt","%ip%:%port% "],
            ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
            ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
            ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
            ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
            ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
            ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
            ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
            ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
            ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
            ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
        ]

        threads = []
        for url, custom_regex in proxy_sources:
            t = threading.Thread(target=fetch_proxies, args=(url, custom_regex, proxies_log))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        unique_proxies = list(set(proxies_log))
        with open(temp_path, "w") as f:
            for proxy in unique_proxies:
                for _ in range(random.randint(7, 10)):
                    f.write(f"{proxy}\n")

        execution_time = (time.time() - start_time)
        if len(unique_proxies) > 0:
            break

    print(f"{Fore.GREEN}Done! Scraped{Fore.MAGENTA}{len(unique_proxies): >5}{Fore.GREEN} in total => {Fore.RED}{temp_path}{Fore.RESET} | {execution_time}ms")
    setTitle(f"Xvirus {THIS_VERSION}")

def proxy():
    temp = os.getenv("temp") + "\\xvirus_proxies"
    
    if not os.path.isfile(temp) or os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = proxies[0]

    with open(temp, 'r+') as fp:
        #read all lines
        lines = fp.readlines()
        #get the first line
        fp.seek(0)
        #remove the proxy
        fp.truncate()
        fp.writelines(lines[1:])
    return ({'http://': f'http://{proxy}', 'https://': f'https://{proxy}'})

heads = [
    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0"
    },

    {
        "Content-Type": "application/json",
        'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0'
    },

    {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0"
    },

    {
       "Content-Type": "application/json",
       "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
    }
]
def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return header

def check_wifi_connection():
    try:
        urllib.request.urlopen('https://www.google.com')
        pass
    except:
        while True:
            offline()
            for i in range(5, 0, -1):
                print(f"{Fore.RED}                                Retrying in {Fore.BLUE}{i} {Fore.RED}seconds", end='\r')
                time.sleep(1)
            clear()

def check_version():
        try:
            assert sys.version_info >= (3,7)
        except AssertionError:
            print(f"{Fore.RED}Woopsie daisy, your Python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with xvirus, please download Python 3.7+")
            sleep(5)
            print("exiting. . .")
            sleep(1.5)
            os._exit(0)

def ping(host):
    while True:
        output = subprocess.check_output(["ping", host]).decode("utf-8")
        print(output)



def get_username():
    temp_dir = tempfile.gettempdir()
    
    username_file = os.path.join(temp_dir, 'xvirus_username')

    if os.path.isfile(username_file):
        with open(username_file, 'r') as f:
            username = f.read().strip()
    else:
        clear()
        usernamelogo()
        username = input(f"""                            {Fore.BLUE}Your Username: """)
        
        with open(username_file, 'w') as f:
            f.write(username)
    
    return username

    
def usernamelogo():
                print(f"""







                    {Fore.RED}███████╗{Fore.BLUE}███╗  ██╗{Fore.RED}████████╗{Fore.BLUE}███████╗{Fore.RED}██████╗   {Fore.BLUE}██╗   ██╗{Fore.RED} █████╗ {Fore.BLUE}██╗   ██╗{Fore.RED}██████╗   
                    {Fore.RED}██╔════╝{Fore.BLUE}████╗ ██║{Fore.RED}╚══██╔══╝{Fore.BLUE}██╔════╝{Fore.RED}██╔══██╗  {Fore.BLUE}╚██╗ ██╔╝{Fore.RED}██╔══██╗{Fore.BLUE}██║   ██║{Fore.RED}██╔══██╗  
                    {Fore.RED}█████╗  {Fore.BLUE}██╔██╗██║{Fore.RED}   ██║   {Fore.BLUE}█████╗  {Fore.RED}██████╔╝  {Fore.BLUE} ╚████╔╝ {Fore.RED}██║  ██║{Fore.BLUE}██║   ██║{Fore.RED}██████╔╝  
                    {Fore.RED}██╔══╝  {Fore.BLUE}██║╚████║{Fore.RED}   ██║   {Fore.BLUE}██╔══╝  {Fore.RED}██╔══██╗  {Fore.BLUE}  ╚██╔╝  {Fore.RED}██║  ██║{Fore.BLUE}██║   ██║{Fore.RED}██╔══██╗  
                    {Fore.RED}███████╗{Fore.BLUE}██║ ╚███║{Fore.RED}   ██║   {Fore.BLUE}███████╗{Fore.RED}██║  ██║  {Fore.BLUE}   ██║   {Fore.RED}╚█████╔╝{Fore.BLUE}╚██████╔╝{Fore.RED}██║  ██║  
                    {Fore.RED}╚══════╝{Fore.BLUE}╚═╝  ╚══╝{Fore.RED}   ╚═╝   {Fore.BLUE}╚══════╝{Fore.RED}╚═╝  ╚═╝  {Fore.BLUE}   ╚═╝   {Fore.RED} ╚════╝ {Fore.BLUE} ╚═════╝ {Fore.RED}╚═╝  ╚═╝  

                          {Fore.BLUE}██╗   ██╗{Fore.RED} ██████╗{Fore.BLUE}███████╗{Fore.RED}██████╗ {Fore.BLUE}███╗  ██╗{Fore.RED} █████╗ {Fore.BLUE}███╗   ███╗{Fore.RED}███████╗
                          {Fore.BLUE}██║   ██║{Fore.RED}██╔════╝{Fore.BLUE}██╔════╝{Fore.RED}██╔══██╗{Fore.BLUE}████╗ ██║{Fore.RED}██╔══██╗{Fore.BLUE}████╗ ████║{Fore.RED}██╔════╝
                          {Fore.BLUE}██║   ██║{Fore.RED}╚█████╗ {Fore.BLUE}█████╗  {Fore.RED}██████╔╝{Fore.BLUE}██╔██╗██║{Fore.RED}███████║{Fore.BLUE}██╔████╔██║{Fore.RED}█████╗  
                          {Fore.BLUE}██║   ██║{Fore.RED} ╚═══██╗{Fore.BLUE}██╔══╝  {Fore.RED}██╔══██╗{Fore.BLUE}██║╚████║{Fore.RED}██╔══██║{Fore.BLUE}██║╚██╔╝██║{Fore.RED}██╔══╝  
                          {Fore.BLUE}╚██████╔╝{Fore.RED}██████╔╝{Fore.BLUE}███████╗{Fore.RED}██║  ██║{Fore.BLUE}██║ ╚███║{Fore.RED}██║  ██║{Fore.BLUE}██║ ╚═╝ ██║{Fore.RED}███████╗
                          {Fore.BLUE} ╚═════╝ {Fore.RED}╚═════╝ {Fore.BLUE}╚══════╝{Fore.RED}╚═╝  ╚═╝{Fore.BLUE}╚═╝  ╚══╝{Fore.RED}╚═╝  ╚═╝{Fore.BLUE}╚═╝     ╚═╝{Fore.RED}╚══════╝
                                                                                                 """)

username = get_username()


def setUsername(new: str):
    temp_dir = tempfile.gettempdir()
    username_file = os.path.join(temp_dir, 'xvirus_username')

    with open(username_file, 'w') as f:
        f.write(new)
#########################################################################################################################################################################
def blackwhite(text):
    os.system("")
    faded = ""
    gradient_steps = 10  # Number of gradient steps
    step_size = 255 // gradient_steps  # Calculate step size for each color channel

    red = 0
    green = 0
    blue = 0

    for line in text.splitlines():
        faded += f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n"
        
        red += step_size
        green += step_size
        blue += step_size

        if red > 255:
            red = 255
        if green > 255:
            green = 255
        if blue > 255:
            blue = 255

    return faded

def getTheme():
    themes = ["xeme", "dark", "fire", "aqua", "neon"]
    with open(os.getenv("temp")+"\\xvirus_theme", 'r') as f:
        text = f.read()
        if not any(s in text for s in themes):
            print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Invalid theme was given, Switching to default. . .')
            setTheme('xeme')
            sleep(2.5)
            __import__("Xvirus").main()
        return text

def setTheme(new: str):
    with open(os.getenv("temp")+"\\xvirus_theme", 'w'): pass
    with open(os.getenv("temp")+"\\xvirus_theme", 'w') as f:
        f.write(new)

def banner(theme=None):
    if theme == "dark":
        print(bennerTheme(blackwhite, blackwhite))
    elif theme == "fire":
        print(Colorate.Vertical(Colors.red_to_yellow, (bannerTheme)))
    elif theme == "aqua":
        print(Colorate.Vertical(Colors.cyan_to_blue, (bannerTheme)))
    elif theme == "neon":
        print(Colorate.Vertical(Colors.blue_to_purple, (bannerTheme)))
    else:
       print(f'''{Fore.RED}

                                        ,.   (   .      )        .      "
                                       ("     )  )'     ,'        )  . (`     '`
                                     .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
                                     _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
                                    ██╗  ██╗██╗   ██╗██╗██████╗ ██╗   ██╗ ██████╗
                                    ╚██╗██╔╝██║   ██║██║██╔══██╗██║   ██║██╔════╝
                                     ╚███╔╝ ╚██╗ ██╔╝██║██████╔╝██║   ██║╚█████╗
                                     ██╔██╗  ╚████╔╝ ██║██╔══██╗██║   ██║ ╚═══██╗
                                    ██╔╝╚██╗  ╚██╔╝  ██║██║  ██║╚██████╔╝██████╔╝
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
> [?] {THIS_VERSION} Changelog                                                                                     Update [UPD] <
> [!] Settings                                                                                          Xside gpt [ai] <
{Fore.WHITE} ┌─────────────────────────────────────┬────────────────────────────────────────┬─────────────────────────────────────┐
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Nuke Account                 {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Block Friends                    {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Disabler                {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Unfriend all friends         {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Profile Changer                  {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Discord Rat Bot               {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Delete and leave all servers {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Brute-Force                {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Vanity Sniper                 {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Spam Create New servers      {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Grabber                    {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Dm Clearer (WIP)              {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Dm Deleter                   {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} QR Code grabber                  {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Nitro Generator               {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Dm                      {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Report                      {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Server Link Generator         {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Enable Seizure Mode          {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} GroupChat Spammer                {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Onliner                 {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Info                   {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Webhook Destroyer                {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]                 {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Log into an account          {Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Mass Checker               {Fore.WHITE}│  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]                 {Fore.WHITE}│
{Fore.WHITE} └─────────────────────────────────────┴────────────────────────────────────────┴─────────────────────────────────────┘
Welcome {username}!''')
                                                                                                                    



bannerTheme = f"""

                                        ,.   (   .      )        .      "
                                       ("     )  )'     ,'        )  . (`     '`
                                     .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
                                     _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
                                    ██╗  ██╗██╗   ██╗██╗██████╗ ██╗   ██╗ ██████╗
                                    ╚██╗██╔╝██║   ██║██║██╔══██╗██║   ██║██╔════╝
                                     ╚███╔╝ ╚██╗ ██╔╝██║██████╔╝██║   ██║╚█████╗
                                     ██╔██╗  ╚████╔╝ ██║██╔══██╗██║   ██║ ╚═══██╗
                                    ██╔╝╚██╗  ╚██╔╝  ██║██║  ██║╚██████╔╝██████╔╝
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
> [?] {THIS_VERSION} Changelog                                                                                     Update [UPD] <
> [!] Settings                                                                                          Xside gpt [ai] <
 ┌─────────────────────────────────────┬────────────────────────────────────────┬─────────────────────────────────────┐
 │  [01] Nuke Account                  │  [10] Block Friends                    │  [19] Token Disabler                │
 │  [02] Unfriend all friends          │  [11] Profile Changer                  │  [20] Discord Rat Bot               │
 │  [03] Delete and leave all servers  │  [12] Token Brute-Force                │  [21] Vanity Sniper                 │
 │  [04] Spam Create New servers       │  [13] Token Grabber                    │  [22] Dm Clearer (WIP)              │
 │  [05] Dm Deleter                    │  [14] QR Code grabber                  │  [23] Nitro Generator               │
 │  [06] Mass Dm                       │  [15] Mass Report                      │  [24] Server Link Generator         │
 │  [07] Enable Seizure Mode           │  [16] GroupChat Spammer                │  [25] Token Onliner                 │
 │  [08] Token Info                    │  [17] Webhook Destroyer                │  [26] [Coming Soon]                 │
 │  [09] Log into an account           │  [18] Token Mass Checker               │  [27] [Coming Soon]                 │
 └─────────────────────────────────────┴────────────────────────────────────────┴─────────────────────────────────────┘
Welcome {username}!"""

def bennerTheme(type1, type2):
    return type1(f'''

                                        ,.   (   .      )        .      "
                                       ("     )  )'     ,'        )  . (`     '`
                                     .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
                                     _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
                                    ██╗  ██╗██╗   ██╗██╗██████╗ ██╗   ██╗ ██████╗
                                    ╚██╗██╔╝██║   ██║██║██╔══██╗██║   ██║██╔════╝
                                     ╚███╔╝ ╚██╗ ██╔╝██║██████╔╝██║   ██║╚█████╗
                                     ██╔██╗  ╚████╔╝ ██║██╔══██╗██║   ██║ ╚═══██╗
                                    ██╔╝╚██╗  ╚██╔╝  ██║██║  ██║╚██████╔╝██████╔╝
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝
> [?] {THIS_VERSION} Changelog                                                                                     Update [UPD] <
> [!] Settings                                                                                          Xside gpt [ai] <''')+type2(f'''
 ┌─────────────────────────────────────┬────────────────────────────────────────┬─────────────────────────────────────┐
 │  [01] Nuke Account                  │  [10] Block Friends                    │  [19] Token Disabler                │
 │  [02] Unfriend all friends          │  [11] Profile Changer                  │  [20] Discord Rat Bot               │
 │  [03] Delete and leave all servers  │  [12] Token Brute-Force                │  [21] Vanity Sniper                 │
 │  [04] Spam Create New servers       │  [13] Token Grabber                    │  [22] Dm Clearer (WIP)              │
 │  [05] Dm Deleter                    │  [14] QR Code grabber                  │  [23] Nitro Generator               │
 │  [06] Mass Dm                       │  [15] Mass Report                      │  [24] Server Link Generator         │
 │  [07] Enable Seizure Mode           │  [16] GroupChat Spammer                │  [25] Token Onliner                 │
 │  [08] Token Info                    │  [17] Webhook Destroyer                │  [26] [Coming Soon]                 │
 │  [09] Log into an account           │  [18] Token Mass Checker               │  [27] [Coming Soon]                 │
 └─────────────────────────────────────┴────────────────────────────────────────┴─────────────────────────────────────┘
Welcome {username}!''')

def offline():
                print(f"""{Fore.RED}







                              ██╗   ██╗ █████╗ ██╗   ██╗██████╗    █████╗ ██████╗ ███████╗
                              ╚██╗ ██╔╝██╔══██╗██║   ██║██╔══██╗  ██╔══██╗██╔══██╗██╔════╝
                               ╚████╔╝ ██║  ██║██║   ██║██████╔╝  ███████║██████╔╝█████╗  
                                ╚██╔╝  ██║  ██║██║   ██║██╔══██╗  ██╔══██║██╔══██╗██╔══╝  
                                 ██║   ╚█████╔╝╚██████╔╝██║  ██║  ██║  ██║██║  ██║███████╗
                                 ╚═╝    ╚════╝  ╚═════╝ ╚═╝  ╚═╝  ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
                               █████╗ ███████╗███████╗██╗     ██╗███╗  ██╗███████╗  ██╗
                              ██╔══██╗██╔════╝██╔════╝██║     ██║████╗ ██║██╔════╝  ██║
                              ██║  ██║█████╗  █████╗  ██║     ██║██╔██╗██║█████╗    ██║
                              ██║  ██║██╔══╝  ██╔══╝  ██║     ██║██║╚████║██╔══╝    ╚═╝
                              ╚█████╔╝██║     ██║     ███████╗██║██║ ╚███║███████╗  ██╗
                               ╚════╝ ╚═╝     ╚═╝     ╚══════╝╚═╝╚═╝  ╚══╝╚══════╝  ╚═╝{Fore.RED}""")



logo = r"""
Please wait while Xvirus Scrapes proxies for you!










                                                        ██╗  ██╗
                                                        ╚██╗██╔╝
                                                         ╚███╔╝ 
                                                         ██╔██╗ 
                                                        ██╔╝╚██╗
                                                        ╚═╝  ╚═╝





"""[1:]


startuplogo = r"""
██╗  ██╗
╚██╗██╔╝
 ╚███╔╝ 
 ██╔██╗ 
██╔╝╚██╗
╚═╝  ╚═╝
"""[1:]

#################################################################################################################################################################################

