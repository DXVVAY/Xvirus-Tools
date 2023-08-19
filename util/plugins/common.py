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
import time
import webbrowser

def CHANGE_LOG():
    input(f'''
    1. New CUI (Similar to the premium versions CUI)!
    2. Fixed many of the visuals
    3. New App Structure
    4. Added the option to chnage pronouns and display name in profile chnager
    5. Fixed Token checker
    6. Fixed the Ratbot not compiling
    7. Added a toggleable Discord RPC
    8. Fixed Token Login not installing MSEDGE driver''')
    
THIS_VERSION = "1.6.7"
TARGET_VERSION = 0

def search_for_updates():
    clear()
    XTitle("Xvirus Checking For Updates. . .")
    
    latest_version_url = "https://cloud.xvirus.xyz/latest_version.txt"
    r = requests.get(latest_version_url)
    latest_version = r.text.strip()

    if THIS_VERSION != latest_version:
        XTitle("New Update Found!")
        print(
            f"""{Fore.RED}
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗  ██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝  ██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗    ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝    ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗  ██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝  ╚═╝
                    {Fore.RED}Looks like Xvirus {THIS_VERSION} is outdated. Latest version is {latest_version}\n""")

        update_url = f"https://cloud.xvirus.xyz/Xvirus-Tools-main.zip"
        choice = input(
            f" <~> {Fore.RED}Do you want to update to the latest version? (Y to update N to continue using this version): {Fore.RED}"
        )

        if choice.lower() == "y" or choice.lower() == "yes":
            print(f"{Fore.WHITE}\n <*> Updating. . .")
            XTitle(f"Xvirus Updating...")
            new_version_source = requests.get(update_url)
            with open("Xvirus-Tools-main.zip", "wb") as zipfile:
                zipfile.write(new_version_source.content)
            with ZipFile("Xvirus-Tools-main.zip", "r") as filezip:
                filezip.extractall()
            os.remove("Xvirus-Tools-main.zip")
            cwd = os.getcwd() + "\\Xvirus-Tools-main"
            shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
            shutil.rmtree(cwd)
            XTitle("Xvirus Update Complete!")
            print(f"{Fore.GREEN} <*> Update Successfully Finished!")
            sleep(2)
            if os.path.exists(os.getcwd() + "setup.bat"):
                os.startfile("setup.bat")
            elif os.path.exists(os.getcwd() + "start.bat"):
                os.startfile("start.bat")
            os._exit(0)


def update():
    clear()
    XTitle("Xvirus Checking For Updates. . .")

    XTitle("New Update Found!")
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
        f" <~> {Fore.RED}Do you want to update to the latest dev branch (Remember that the dev branch might be unstable)?\n(Y to update N to continue using this version): {Fore.RED}"
    )

    if choice.lower() == "y" or choice.lower() == "yes":
        print(f"{Fore.WHITE}\nUpdating. . .")
        XTitle(f"Xvirus Updating...")
        new_version_source = requests.get(update_url)
        with open("Xvirus-Tools-main.zip", "wb") as zipfile:
            zipfile.write(new_version_source.content)
        with ZipFile("Xvirus-Tools-main.zip", "r") as filezip:
            filezip.extractall()
        os.remove("Xvirus-Tools-main.zip")
        cwd = os.getcwd() + "\\Xvirus-Tools-main"
        shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
        shutil.rmtree(cwd)
        XTitle("Xvirus Update Complete!")
        print(f"{Fore.GREEN}Update Successfully Finished!")
        sleep(2)
        if os.path.exists(os.getcwd() + "setup.bat"):
            os.startfile("setup.bat")
        elif os.path.exists(os.getcwd() + "start.bat"):
            os.startfile("start.bat")
        os._exit(0)


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
        
def get_driver():
    drivers = ["msedgedriver.exe"]

    print(f"\n{Fore.BLUE} <!> Checking Driver. . .")
    sleep(0.5)

    for driver in drivers:
        if os.path.exists(os.getcwd() + os.sep + driver):
            print(f" <!>{Fore.BLUE}{driver} already exists, continuing. . .{Fore.RESET}")
            sleep(0.5)
            return driver
    else:
        print(f"{Fore.RED} <!> Driver not found! Installing it for you")
        if os.path.exists(os.getenv('localappdata') + '\\Microsoft\\Edge'):
            Edge_Installer()
            print(f"{Fore.GREEN} <*> msedgedriver.exe Installed!{Fore.RESET}")
            return "msedgedriver.exe"
        else:
            print(f'<!> No compatible driver found. . . Proceeding with msedgedriver')
            Chrome_Installer()
            print(f"{Fore.GREEN} <!> trying to install msedgedriver.exe{Fore.RESET}")
            return "msedgedriver.exe"


def clear():
    system = os.name
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    return

def XTitle(_str):
    system = os.name
    if system == 'nt':
        ctypes.windll.kernel32.SetConsoleTitleW(f"{_str} - Discord API Tools | https://xvirus.xyz | Made By Xvirus™")
    elif system == 'posix':
        os.system(f"\033]0;{_str} - Discord API Tools | https://xvirus.xyz | Made By Xvirus™\a", end='', flush=True)
    else:
        pass

def print_slow(_str):
    for letter in _str:
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def print015(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)
    sys.stdout.write("\n")

def print01(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.015)

def CheckToken(token):
    url = 'https://discord.com/api/v9/users/@me'
    response = requests.get(url, headers=getheaders(token))
    if response.status_code == 200:
        print(f"{Fore.BLUE} <*> Valid Token.")
    else:
        print(f"\n{Fore.RED} <!> Invalid Token.")
        sleep(1)
        __import__("Xvirus").main1()

def CheckWebhook(hook):
    try:
        response = requests.get(hook)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print(f"\n{Fore.RED} <!> Invalid Webhook.")
        sleep(1)
        __import__("Xvirus").main1()

    try:
        json_data = response.json()
        j = json_data["name"]
        print(f"{Fore.BLUE} <*> Valid webhook! ({j})")
    except (KeyError, json.decoder.JSONDecodeError):
        print(f"\n{Fore.RED} <!> Invalid Webhook.")
        sleep(1)

def proxy_scrape(): 
    proxieslog = []
    XTitle("Scraping Proxies")
    startTime = time.time()
    temp = os.getenv("temp")+"\\xvirus_proxies"
    Anime.Fade((logo), Colors.rainbow, Colorate.Vertical, time=5)

    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    proxysources = [
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
    for url in proxysources:
        t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp, "w") as f:
        for proxy in proxies:
            for i in range(random.randint(7, 10)):
                f.write(f"{proxy}\n")
    execution_time = (time.time() - startTime)
    print(f"{Fore.BLUE} <!> Done! Scraped{Fore.MAGENTA}{len(proxies): >5}{Fore.RED} in total => {Fore.RED}{temp} | {execution_time}ms")

def proxy():
    temp = os.getenv("temp") + "\\xvirus_proxies"

    if not os.path.isfile(temp) or os.stat(temp).st_size == 0:
        proxy_scrape()
    proxies = open(temp).read().split('\n')
    proxy = random.choice(proxies)

    with open(temp, 'r+') as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        fp.writelines(lines[1:])
    return {'http': f'http://{proxy}', 'https': f'https://{proxy}'}

def get_proxies():
    temp_folder = os.path.join(os.environ.get("TEMP", "C:\\temp"), "xvirus_proxies")
    
    with open(temp_folder, "w") as f:
        proxies = f.read().strip().splitlines()
    proxies = [proxy for proxy in proxies if proxy.strip()]
    return proxies

def clean_proxy(proxy):
        if isinstance(proxy, str):
            if '@' in proxy:
                return proxy
            elif len(proxy.split(':')) == 2:
                return proxy
            elif len(proxy.split(':')) == 4:
                return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
            else:
                if '.' in proxy.split(':')[0]:
                    return ':'.join(proxy.split(':')[2:]) + '@' + ':'.join(proxy.split(':')[:2])
                else:
                    return ':'.join(proxy.split(':')[:2]) + '@' + ':'.join(proxy.split(':')[2:])
        elif isinstance(proxy, dict):
            if proxy.get("http://") or proxy.get("https://"):
                return proxy
            else:
                if proxy in [dict(), {}]:
                    return {}
                return {
                    "http://": proxy.get("http") or proxy.get("https"),
                    "https://": proxy.get("https") or proxy.get("http")
                }

def get_random_proxy():
        try:
            return random.choice(get_proxies())
        except:
            return {}

def get_proxy_type():
    h = "http"
    if "socks5" in h:
        h = "socks5"
    return h

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
    }]

def getheaders(token=None):
    headers = random.choice(heads)
    if token:
        headers.update({"Authorization": token})
    return headers

def check_wifi_connection():
    domains = ['https://www.google.com', 'https://www.facebook.com', 'https://www.apple.com']
    for domain in domains:
        try:
            urllib.request.urlopen(domain)
            return
        except urllib.error.URLError:
            pass

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
            print(f"{Fore.RED} <!> Woopsie daisy, your Python version ({sys.version_info[0]}.{sys.version_info[1]}.{sys.version_info[2]}) is not compatible with xvirus, please download Python 3.7+")
            sleep(5)
            print(" <!> exiting. . .")
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

def notfree():
    print_slow(" <!> This feature is not availabe on the free version of Xvirus\n <!> check https://xvirus.xyz and or https://discord.gg/xvirus to buy the premium version!")
    sleep(1.5)

def PETC():
    input(f'{Fore.RED}\n <~> Press ENTER to continue{Fore.RED}')

def redirect(): 
    redirect = input("Do you want to redirect to https://xvirus.xyz and https://discord.gg/xvirus? (y/n): ")
    if redirect.lower() == 'y':
        webbrowser.open("https://xvirus.xyz")
        webbrowser.open("https://discord.gg/xvirus")
    elif redirect.lower() == 'n':
        print(" <!> Redirect not requested.")
    else:
        print(" <!> Invalid input. Redirect not requested.")

def set_terminal_width(width):
    handle = ctypes.windll.kernel32.GetStdHandle(-11)

    new_size = ctypes.wintypes._COORD(width, ctypes.wintypes._COORD().Y)

    ctypes.windll.kernel32.SetConsoleScreenBufferSize(handle, new_size)
    ctypes.windll.kernel32.SetConsoleWindowInfo(handle, True, ctypes.byref(new_size))

xvirus_width = 120

lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLACK_EX
r = Fore.RED

def main_banner():
    if getTheme() == "xeme":
        banner()
    elif getTheme() == "dark":
        banner("dark")
    elif getTheme() == "fire":
        banner("fire")
    elif getTheme() == "aqua":
        banner("aqua")
    elif getTheme() == "neon":
        banner("neon")

def getTheme():
    themes = ["xeme", "dark", "fire", "aqua", "neon"]
    with open(os.getenv("temp")+"\\xvirus_theme", 'r') as f:
        text = f.read()
        if not any(s in text for s in themes):
            print(f'{Fore.RED} <*>  Invalid theme was given, Switching to default. . .')
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
        print(Colorate.Vertical(Colors.black_to_white, (bannerTheme)))
    elif theme == "fire":
        print(Colorate.Vertical(Colors.red_to_yellow, (bannerTheme)))
    elif theme == "aqua":
        print(Colorate.Vertical(Colors.cyan_to_blue, (bannerTheme)))
    elif theme == "neon":
        print(Colorate.Vertical(Colors.blue_to_red, (bannerTheme)))
    elif theme == "rainbow":
        print(Colorate.Horizontal(Colors.rainbow, (bannerTheme)))
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
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝                     Buy Premium [BUY] <
> [?] {THIS_VERSION} Changelog                                                                                     Update [UPD] <
> [!] Settings                                                                                          Xside gpt [ai] <
{r} ╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                               ═══╗
{r} ║   ({lb}01{r}) {lb}> Token Login               {r}║ ║   {r}({lb}10{r}) {lb}> Seizure                    {r}║ ║   {r}({lb}19{r}) {lb}> Webhook Tool{r}               ║
{r}     ({lb}02{r}) {lb}> Token Info                      {r}({lb}11{r}) {lb}> Leave And Delete Servers         {r}({lb}20{r}) {lb}> Webhook Generator{r}
{r}     ({lb}03{r}) {lb}> Token Disabler                  {r}({lb}12{r}) {lb}> Remove Friends                   {r}({lb}21{r}) {lb}> Nitro Generator{r}
{r}     ({lb}04{r}) {lb}> Token Brute-Force               {r}({lb}13{r}) {lb}> Block Friends                    {r}({lb}22{r}) {lb}> Server Link Generator{r}
{r}     ({lb}05{r}) {lb}> Token Grabber                   {r}({lb}14{r}) {lb}> Dm @everyone                     {r}({lb}23{r}) {lb}> Server Nuker{r}
{r}     ({lb}06{r}) {lb}> Token Checker                   {r}({lb}15{r}) {lb}> Delete DMs                       {r}({lb}24{r}) {lb}> Group Spammer{r}
{r}     ({lb}07{r}) {lb}> Token Nuker                     {r}({lb}16{r}) {lb}> Clear DMs                        {r}({lb}25{r}) {lb}> SelfBot Spammer{r}
{r}     ({lb}08{r}) {lb}> QR Token Grabber                {r}({lb}17{r}) {lb}> Change Profile                   {r}({lb}26{r}) {lb}> Threads Spammer{r}
{r} ║   ({lb}09{r}) {lb}> Discord RAT Bot           {r}║ ║   {r}({lb}18{r}) {lb}> Vanity Sniper              {r}║ ║   {r}({lb}27{r}) {lb}> Next Page  {r}                ║
{r} ╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                               ═══╝''')
                                                                                                                    



bannerTheme = f"""

                                        ,.   (   .      )        .      "
                                       ("     )  )'     ,'        )  . (`     '`
                                     .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"
                                     _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '..
                                    ██╗  ██╗██╗   ██╗██╗██████╗ ██╗   ██╗ ██████╗
                                    ╚██╗██╔╝██║   ██║██║██╔══██╗██║   ██║██╔════╝
                                     ╚███╔╝ ╚██╗ ██╔╝██║██████╔╝██║   ██║╚█████╗
                                     ██╔██╗  ╚████╔╝ ██║██╔══██╗██║   ██║ ╚═══██╗
> [RPC] Toggle RPC                  ██╔╝╚██╗  ╚██╔╝  ██║██║  ██║╚██████╔╝██████╔╝
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝                     Buy Premium [BUY] <
> [?] {THIS_VERSION} Changelog                                                                                     Update [UPD] <
> [!] Settings                                                                                          Xside gpt [ai] <
 ╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                               ═══╗
 ║   (01) > Token Login               ║ ║   (10) > Seizure                    ║ ║   (19) > Webhook Tool               ║
     (02) > Token Info                      (11) > Leave And Delete Servers         (20) > Webhook Generator
     (03) > Token Disabler                  (12) > Remove Friends                   (21) > Nitro Generator
     (04) > Token Brute-Force               (13) > Block Friends                    (22) > Server Link Generator
     (05) > Token Grabber                   (14) > Dm @everyone                     (23) > Server Nuker
     (06) > Token Checker                   (15) > Delete DMs                       (24) > Group Spammer
     (07) > Token Nuker                     (16) > Clear DMs                        (25) > SelfBot Spammer
     (08) > QR Token Grabber                (17) > Change Profile                   (26) > Threads Spammer
 ║   (09) > Discord RAT Bot           ║ ║   (18) > Vanity Sniper              ║ ║   (27) > Next Page                  ║
 ╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                               ═══╝"""



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
> [RPC] Toggle RPC                  ██╔╝╚██╗  ╚██╔╝  ██║██║  ██║╚██████╔╝██████╔╝
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝                     Buy Premium [BUY] <
> [?] {THIS_VERSION} Changelog                                                                                     Update [UPD] <
> [!] Settings                                                                                          Xside gpt [ai] <''')+type2(f'''
 ╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                               ═══╗
 ║   (01) > Token Login               ║ ║   (10) > Seizure                    ║ ║   (19) > Webhook Tool               ║
     (02) > Token Info                      (11) > Leave And Delete Servers         (20) > Webhook Generator
     (03) > Token Disabler                  (12) > Remove Friends                   (21) > Nitro Generator
     (04) > Token Brute-Force               (13) > Block Friends                    (22) > Server Link Generator
     (05) > Token Grabber                   (14) > Dm @everyone                     (23) > Server Nuker
     (06) > Token Checker                   (15) > Delete DMs                       (24) > Group Spammer
     (07) > Token Nuker                     (16) > Change Profile                   (25) > SelfBot Spammer
     (08) > QR Token Grabber                (17) > Change Profile                   (26) > Threads Spammer
 ║   (09) > Discord RAT Bot           ║ ║   (18) > Vanity Sniper              ║ ║   (27) > Next Page                  ║
 ╚═══                              ═══╝ ╚═══                               ═══╝ ╚═══                               ═══╝''')

def offline():
                print(f"""{Fore.RED}







                              ██╗   ██╗ █████╗ ██╗   ██╗   █████╗ ██████╗ ███████╗
                              ╚██╗ ██╔╝██╔══██╗██║   ██║  ██╔══██╗██╔══██╗██╔════╝
                               ╚████╔╝ ██║  ██║██║   ██║  ███████║██████╔╝█████╗  
                                ╚██╔╝  ██║  ██║██║   ██║  ██╔══██║██╔══██╗██╔══╝  
                                 ██║   ╚█████╔╝╚██████╔╝  ██║  ██║██║  ██║███████╗
                                 ╚═╝    ╚════╝  ╚═════╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
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