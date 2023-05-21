from common import *

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

def purplepink(text):
    os.system("")
    faded = ""
    red = 40
    gradient_steps = 10
    step_size = (255 - red) // gradient_steps

    for line in text.splitlines():
        faded += f"\033[38;2;{red};0;220m{line}\033[0m\n"
        red += step_size
        if red > 255:
            red = 255

    return faded


def greenblue(text):
    os.system("")
    faded = ""
    blue = 100
    gradient_steps = 10
    step_size = (255 - blue) // gradient_steps

    for line in text.splitlines():
        faded += f"\033[38;2;0;255;{blue}m{line}\033[0m\n"
        blue += step_size
        if blue > 255:
            blue = 255

    return faded

def pinkred(text):
    os.system("")
    faded = ""
    blue = 255
    gradient_steps = 10
    step_size = blue // gradient_steps

    for line in text.splitlines():
        faded += f"\033[38;2;255;0;{blue}m{line}\033[0m\n"
        blue -= step_size
        if blue < 0:
            blue = 0

    return faded


def purpleblue(text):
    os.system("")
    faded = ""
    red = 110
    gradient_steps = 10
    step_size = red // gradient_steps

    for line in text.splitlines():
        faded += f"\033[38;2;{red};0;255m{line}\033[0m\n"
        red -= step_size
        if red < 0:
            red = 0

    return faded


def aqua(text):
    os.system("")
    faded = ""
    green = 10
    gradient_steps = 10
    step_size = (255 - green) // gradient_steps

    for line in text.splitlines():
        faded += f"\033[38;2;0;{green};255m{line}\033[0m\n"
        green += step_size
        if green > 255:
            green = 255

    return faded


def fire(text):
    os.system("")
    faded = ""
    green = 250
    gradient_steps = 10
    step_size = green // gradient_steps

    for line in text.splitlines():
        faded += f"\033[38;2;255;{green};0m{line}\033[0m\n"
        green -= step_size
        if green < 0:
            green = 0

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
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  
> [?] {THIS_VERSION} Changelog
> [!] Settings                                                                                          Xside gpt [ai] <
{Fore.WHITE}───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RED}
{Fore.RED}[{Fore.RED}01{Fore.RED}]{Fore.LIGHTBLACK_EX} Nuke Account                                |{Fore.RED}[{Fore.RED}10{Fore.RED}]{Fore.LIGHTBLACK_EX} Block Friends                 |{Fore.RED}[{Fore.RED}19{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Disabler
{Fore.RED}[{Fore.RED}02{Fore.RED}]{Fore.LIGHTBLACK_EX} Unfriend all friends                        |{Fore.RED}[{Fore.RED}11{Fore.RED}]{Fore.LIGHTBLACK_EX} Profile Changer               |{Fore.RED}[{Fore.RED}20{Fore.RED}]{Fore.LIGHTBLACK_EX} Discord Rat Bot 
{Fore.RED}[{Fore.RED}03{Fore.RED}]{Fore.LIGHTBLACK_EX} Delete and leave all servers                |{Fore.RED}[{Fore.RED}12{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Brute-Force             |{Fore.RED}[{Fore.RED}21{Fore.RED}]{Fore.LIGHTBLACK_EX} Vanity Sniper
{Fore.RED}[{Fore.RED}04{Fore.RED}]{Fore.LIGHTBLACK_EX} Spam Create New servers                     |{Fore.RED}[{Fore.RED}13{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Grabber                 |{Fore.RED}[{Fore.RED}22{Fore.RED}]{Fore.LIGHTBLACK_EX} Dm Clearer (WIP)
{Fore.RED}[{Fore.RED}05{Fore.RED}]{Fore.LIGHTBLACK_EX} Dm Deleter                                  |{Fore.RED}[{Fore.RED}14{Fore.RED}]{Fore.LIGHTBLACK_EX} QR Code grabber               |{Fore.RED}[{Fore.RED}23{Fore.RED}]{Fore.LIGHTBLACK_EX} Nitro Generator
{Fore.RED}[{Fore.RED}06{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Dm                                     |{Fore.RED}[{Fore.RED}15{Fore.RED}]{Fore.LIGHTBLACK_EX} Mass Report                   |{Fore.RED}[{Fore.RED}24{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
{Fore.RED}[{Fore.RED}07{Fore.RED}]{Fore.LIGHTBLACK_EX} Enable Seizure Mode                         |{Fore.RED}[{Fore.RED}16{Fore.RED}]{Fore.LIGHTBLACK_EX} GroupChat Spammer             |{Fore.RED}[{Fore.RED}25{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
{Fore.RED}[{Fore.RED}08{Fore.RED}]{Fore.LIGHTBLACK_EX} Get information from a targetted account    |{Fore.RED}[{Fore.RED}17{Fore.RED}]{Fore.LIGHTBLACK_EX} Webhook Destroyer             |{Fore.RED}[{Fore.RED}26{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
{Fore.RED}[{Fore.RED}09{Fore.RED}]{Fore.LIGHTBLACK_EX} Log into an account                         |{Fore.RED}[{Fore.RED}18{Fore.RED}]{Fore.LIGHTBLACK_EX} Token Mass Validator          |{Fore.RED}[{Fore.RED}27{Fore.RED}]{Fore.LIGHTBLACK_EX} [Coming Soon]
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
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  
> [?] {THIS_VERSION} Changelog
> [!] Settings                                                                                         Xside gpt [ai] <''')+type2('''  
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
[01] Nuke Account                                |[10] Block Friends                 |[19] Token Disabler
[02] Unfriend all friends                        |[11] Profile Changer               |[20] Discord Rat Bot 
[03] Delete and leave all servers                |[12] Token Brute-Force             |[21] Vanity Sniper
[04] Spam Create New servers                     |[13] Token Grabber                 |[22] Dm Clearer (WIP)
[05] Dm Deleter                                  |[14] QR Code grabber               |[23] Nitro Generator
[06] Mass Dm                                     |[15] Mass Report                   |[24] [Coming Soon]
[07] Enable Seizure Mode                         |[16] GroupChat Spammer             |[25] [Coming Soon]
[08] Get information from a targetted account    |[17] Webhook Destroyer             |[26] [Coming Soon]
[09] Log into an account                         |[18] Token Mass Validator          |[27] [Coming Soon]
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')


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


