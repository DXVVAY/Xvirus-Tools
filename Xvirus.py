import util.accountNuke
import util.dmclear
import util.dmdeleter
import util.friend_blocker
import util.groupchat_spammer
import util.info
import util.infoscraper
import util.login
import util.massdm
import util.message
import util.profilechanger
import util.rat
import util.seizure
import util.server_leaver
import util.spammer
import util.tokenbrute
import util.tokenchecker
import util.unfriender
import util.vanitysniper
import util.webhookspammer
from util.plugins.common import *

threads = 3
cancel_key = "ctrl+x"
current_dir = os.path.dirname(os.path.abspath(__file__))
         
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
    if choice == "1":
        util.accountNuke.Xvirus_Nuke()
        main()

    elif choice == '2':
        util.unfriender.UnFriender()
        main()

    elif choice == '3':
        util.server_leaver.Leaver()
        main()
                
    elif choice == '4':
        notfree()
        main()

    elif choice == '5':
        util.dmdeleter.deletedms()
        main()

    elif choice == '6':
        util.massdm.massdm()
        main()

    elif choice == '7':
        util.seizure.Seizure()
        main()

    elif choice == '8':
        util.info.getinfo()
        main()

    elif choice == '9':
        util.login.tokenlogin()
        main()

    elif choice == '10':
        util.friend_blocker.BlockAll()
        main()

    elif choice == '11':
        util.profilechanger.ProfileChanger()
        main()

    elif choice == '12':
        util.tokenbrute.tokenbrute()
        main()

    elif choice == '13':
        notfree()
        main()

    elif choice == '14':
        notfree()
        main()

    elif choice == "16":
        util.groupchat_spammer.groupspammer()
        main()

    elif choice == '17':
        util.webhookspammer.webhooktool()
        main()

    elif choice == '18':
        util.tokenchecker.tokenchecker() 
        main()

    elif choice == '19':
        notfree()
        main()

    elif choice == '20':
        util.rat.discordrat()
        main()

    elif choice == '21':
        util.vanitysniper.snipe()
        main()

    elif choice == '22':
        util.dmclear.dmclearer()
        main()

    elif choice == '23':
        notfree()
        main()

    elif choice == '24':
        notfree()
        main()

    elif choice == '25':
        notfree()
        main()

    elif choice == '26':
        notfree()
        main()

    elif choice == '27':
        notfree()
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
    
    elif choice == 'UPD':
        update()

    elif choice == 'BUY':
        count_and_redirect()
        main
        
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

