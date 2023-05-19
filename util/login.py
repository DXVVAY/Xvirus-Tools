import requests
import Xvirus

from time import sleep
from selenium import webdriver
from colorama import Fore, Back

from util.plugins.common import get_driver, getheaders

def TokenLogin(token):
    j = requests.get("https://discord.com/api/v10/users/@me", headers=getheaders(token)).json()
    user = j["username"] + "#" + str(j["discriminator"])
    script = """
            document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"%s"`
            location.reload();
        """ % (token)
    type_ = get_driver()

    if type_ == "chromedriver.exe":
        opts = webdriver.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
    elif type_ == "operadriver.exe":
        opts = webdriver.opera.options.ChromeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Opera(options=opts)
    elif type_ == "msedgedriver.exe":
        opts = webdriver.EdgeOptions()
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])
        opts.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opts)
    else:
        print(f'{Fore.RESET}[{Fore.RED}Error{Fore.RESET}] : Coudln\'t find a driver to automate the proccess of login in to {user}')
        sleep(3)
        print(f"{Fore.YELLOW}Paste this script into the console of a browser:{Fore.RESET}\n\n{Back.RED}{script}\n{Back.RESET}")
        print("Enter anything to continue. . . ", end="")
        input()
        Xvirus.main()

    print(f"{Fore.GREEN}Logging into {Fore.BLUE}{user}")
    driver.get("https://discordapp.com/login")
    driver.execute_script(script)
    Xvirus.main()