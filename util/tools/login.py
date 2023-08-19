from time import sleep

import requests
from colorama import Back, Fore
from selenium import webdriver

from util.plugins.common import *


def TokenLoging(token):
    j = requests.get("https://discord.com/api/v10/users/@me", headers=getheaders(token)).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    type_ = get_driver()

    if  type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opts)
    else:
        print(f'{Fore.RED} <!> Coudln\'t find a driver to automate the proccess of login in to {user}')
        sleep(3)
        print(f"{Fore.YELLOW} <*> Paste this script into the console of a browser:\n\n{Back.RED}{script}\n{Back.RESET}")

    print(f"{Fore.GREEN}Logging into {Fore.BLUE}{user}")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)


def tokenlogin():
    token = input(f' <~> {Fore.RED}Token: {Fore.RED}')
    validateToken(token)
    TokenLoging(token)