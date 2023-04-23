import requests
import os
import shutil
import re
import sys

from zipfile import ZipFile
from time import sleep
from bs4 import BeautifulSoup
from colorama import Fore

from util.plugins.common import *


def search_for_updates():
    # Will add back soon
    clear()
    setTitle("Xvirus Checking For Updates. . .")
    r = requests.get("https://github.com/Xvirus0/Xvirus-Tools/releases/latest")

    soup = str(BeautifulSoup(r.text, "html.parser"))
    s1 = re.search("<title>", soup)
    s2 = re.search("·", soup)
    result_string = soup[s1.end() : s2.start()]

    if THIS_VERSION not in result_string:
        setTitle("Hazard Nuker New Update Found!")
        print(
            f"""{Fore.YELLOW}
                ███╗   ██╗███████╗██╗    ██╗    ██╗   ██╗██████╗ ██████╗  █████╗ ████████╗███████╗██╗
                ████╗  ██║██╔════╝██║    ██║    ██║   ██║██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
                ██╔██╗ ██║█████╗  ██║ █╗ ██║    ██║   ██║██████╔╝██║  ██║███████║   ██║   █████╗  ██║
                ██║╚██╗██║██╔══╝  ██║███╗██║    ██║   ██║██╔═══╝ ██║  ██║██╔══██║   ██║   ██╔══╝  ╚═╝
                ██║ ╚████║███████╗╚███╔███╔╝    ╚██████╔╝██║     ██████╔╝██║  ██║   ██║   ███████╗██╗
                ╚═╝  ╚═══╝╚══════╝ ╚══╝╚══╝      ╚═════╝ ╚═╝     ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝
                              {Fore.RED}Looks like this Hazard Nuker {THIS_VERSION} is outdated """.replace(
                "█", f"{Fore.WHITE}█{Fore.RED}"
            ),
            end="\n\n",
        )
        soup = BeautifulSoup(
            requests.get(
                "https://github.com/KDot227/hazard-nuker-mirror/releases"
            ).text,
            "html.parser",
        )
        for link in soup.find_all("a"):
            if "releases/download" in str(link):
                update_url = f"https://github.com/{link.get('href')}"
        choice = input(
            f"{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}You want to update to the latest version? (Y to update): {Fore.RED}"
        )

        if choice.lower() == "y" or choice.lower() == "yes":
            print(f"{Fore.WHITE}\nUpdating. . .")
            setTitle(f"Hazard Nuker Updating...")
            # if they are running hazard.exe
            if os.path.basename(sys.argv[0]).endswith("exe"):
                with open("HazardNuker.zip", "wb") as zipfile:
                    zipfile.write(requests.get(update_url).content)
                with ZipFile("HazardNuker.zip", "r") as filezip:
                    filezip.extractall()
                os.remove("HazardNuker.zip")
                cwd = os.getcwd() + "\\HazardNuker\\"
                shutil.copyfile(cwd + "Changelog.md", "Changelog.md")
                try:
                    shutil.copyfile(
                        cwd + os.path.basename(sys.argv[0]), "HazardNuker.exe"
                    )
                except Exception:
                    pass
                shutil.copyfile(cwd + "README.md", "README.md")
                shutil.rmtree("HazardNuker")
                setTitle("Hazard Nuker Update Complete!")
                print(f"{Fore.GREEN}Update Successfully Finished!")
                sleep(2)
                os.startfile("HazardNuker.exe")
                os._exit(0)
            # if they are running hazard source code
            else:
                new_version_source = requests.get(
                    "https://github.com/KDot227/hazard-nuker-mirror/archive/refs/heads/main.zip"
                )
                with open("Hazard-Nuker-master.zip", "wb") as zipfile:
                    zipfile.write(new_version_source.content)
                with ZipFile("Hazard-Nuker-master.zip", "r") as filezip:
                    filezip.extractall()
                os.remove("Hazard-Nuker-master.zip")
                cwd = os.getcwd() + "\\Hazard-Nuker-master"
                shutil.copytree(cwd, os.getcwd(), dirs_exist_ok=True)
                shutil.rmtree(cwd)
                setTitle("Hazard Nuker Update Complete!")
                print(f"{Fore.GREEN}Update Successfully Finished!")
                sleep(2)
                if os.path.exists(os.getcwd() + "setup.bat"):
                    os.startfile("setup.bat")
                elif os.path.exists(os.getcwd() + "start.bat"):
                    os.startfile("start.bat")
                os._exit(0)
