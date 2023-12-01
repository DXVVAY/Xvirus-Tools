# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

class proxy_setting():
    def toggle_proxy():
        cs = config._get("use_proxies")

        if cs == True:
            config._set("use_proxies", False)
            Output("info").notime(f"Proxy Use Toggled {Fore.RED}OFF")
            sleep(1)
        else:
            config._set("use_proxies", True)
            Output("info").notime(f"Proxy Use Toggled {Fore.RED}ON")
            sleep(1)

    def clear_proxy():
        config.reset("xvirus_proxies")
        Output("info").notime("Proxy Cache Cleared")
        sleep(1)   

    def add_proxies():
        path = utility.ask(f'Enter the path to the txt file containing proxies')
        folder_path = os.path.join(os.getenv('LOCALAPPDATA'), 'xvirus_free')
        file_path = os.path.join(folder_path, 'xvirus_proxies')
        proxy_setting.clear_proxy()

        with open(path, 'r') as file:
            proxies = file.read()

        with open(file_path, 'w') as f:
            f.write(proxies)

        Output("info").notime("Successfully Wrote New Proxies")
        sleep(1) 

def theme_settings():
    print(
        f'''
{Fore.RED}[01] RED           {Fore.BLUE}[02] BLUE         {Fore.GREEN}[03] GREEN        {Fore.CYAN}[04] CYAN
{Fore.LIGHTWHITE_EX}[05] WHITE         {Fore.YELLOW}[06] YELLOW       {Fore.MAGENTA}[07] MAGENTA      {Fore.LIGHTRED_EX}[08] LIGHT RED
{Fore.LIGHTBLUE_EX}[09] LIGHT BLUE    {Fore.LIGHTGREEN_EX}[10] LIGHT GREEN {Fore.LIGHTCYAN_EX} [11] LIGHT CYAN   {Fore.LIGHTBLACK_EX}[12] LIGHT BLACK
    '''
    )
    choice = utility.ask('Theme').lstrip("0")
    themes = {
        '1': 'RED',
        '2': 'BLUE',
        '3': 'GREEN',
        '4': 'CYAN',
        '5': 'LIGHTWHITE_EX',
        '6': 'YELLOW',
        '7': 'MAGENTA',
        '8': 'LIGHTRED_EX',
        '9': 'LIGHTBLUE_EX',
        '10': 'LIGHTGREEN_EX',
        '11': 'LIGHTCYAN_EX',
        '12': 'LIGHTBLACK_EX',
    }
    selected_theme = themes.get(choice)
    if selected_theme:
        config._set("xvirus_theme", selected_theme)
        Output("info").notime(f"Theme set to {selected_theme}")
        sleep(1.5)
    else:
        Output("bad").notime("Invalid choice, theme not changed.")
        sleep(2)

def settings():
    utility.make_menu("Theme Changer", 
                      "Change Username", 
                      "Proxy Settings", 
                      "Toggle Debug Mode", 
                      f"{Fore.RED}Exit... "
                     )
    choice = utility.ask('Setting')
    if choice not in ["1", "2", "3", "4", "5"]:
        Output("bad").notime(f'Invalid Setting')
        sleep(1)

    elif choice == "1":
        theme_settings()

    elif choice == "2":
        name = utility.ask('Username')
        config._set("xvirus_username", name)
        Output("info").notime(f'Change Userrname To {Fore.RED}{name}')
        sleep(1)

    elif choice == "3":
        utility.make_menu("Toggle Proxy Use", 
                          "Clear Proxy Cache", 
                          "Add own Proxies to Cache"
                         )
        proxychoice = utility.ask('Choice')
        if proxychoice == '1':
            proxy_setting.toggle_proxy()
        elif proxychoice == '2':
            proxy_setting.clear_proxy()
        elif proxychoice == '3':
            proxy_setting.add_proxies()
        else:
            Output("bad").notime("Invalid Choice")

    elif choice == '4':
        cs = config._get("debug_mode")

        if cs == True:
            config._set("debug_mode", False)
            Output("info").notime(f"Debug Mode Toggled {Fore.RED}OFF")
            sleep(1)
        else:
            config._set("debug_mode", True)
            Output("info").notime(f"Debug Mode Toggled {Fore.RED}ON")
            sleep(1)

    elif choice == "5":
        choice = utility.ask('Are you sure you want to exit Xvirus? (Y to confirm)')
        if choice.upper() == 'Y':
            utility.clear()
            os._exit(0)
        else:
            sleep(0.5)
    else:
        utility.clear()
