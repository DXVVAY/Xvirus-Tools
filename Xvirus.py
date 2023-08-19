from util import *

threads = 3
current_dir = os.path.dirname(os.path.abspath(__file__))


def settings():
    print(f'''
        {Fore.BLUE}[{Fore.RED}1{Fore.BLUE}] Theme changer
        {Fore.BLUE}[{Fore.RED}2{Fore.BLUE}] Change Username
        {Fore.BLUE}[{Fore.RED}3{Fore.BLUE}] Go Into GUI Mode
        {Fore.BLUE}[{Fore.RED}4{Fore.BLUE}] {Fore.RED}Exit...    
                        ''')
    secondchoice = input(f'{Fore.RED} <~> Setting: {Fore.BLUE}')
    if secondchoice not in ["1", "2", "3", "4"]:
        print(f'{Fore.RED} <!> Invalid Setting')
        sleep(1)
    if secondchoice == "1":
        print(f"""
    {Fore.RED}Xeme: 1
    {Fore.LIGHTBLACK_EX}Dark: 2
    {Fore.YELLOW}Fire: 3
    {Fore.BLUE}Aqua: 4
    {Fore.CYAN}N{Fore.MAGENTA}e{Fore.CYAN}o{Fore.MAGENTA}n{Fore.CYAN}:{Fore.MAGENTA} 5
    {Fore.RED}R{Fore.BLUE}a{Fore.GREEN}i{Fore.CYAN}n{Fore.BLUE}b{Fore.MAGENTA}o{Fore.RED}w{Fore.BLUE}:{Fore.GREEN} 6""")
        themechoice = input(f'{Fore.RED} <~> Theme: {Fore.BLUE}')
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
        elif themechoice == "6":
            setTheme('rainbow')
        else:
            print(f'{Fore.RED} <!> Invalid Theme')
            sleep(1.5)
        print_slow(f"{Fore.RED} <*> Theme set to {Fore.BLUE}{getTheme()}")
        sleep(0.5)

    elif secondchoice == "2":
        new_username = input(f'{Fore.BLUE} <~> Enter your new username: {Fore.BLUE}')
        setUsername(new_username)
        print_slow(f"{Fore.RED} <*> Username set to {Fore.BLUE}{new_username}\n{Fore.RED} <!> Restarting tool")
        sleep(2)
        subprocess.run("Xvirus-Tools.exe", shell=True)
        exit()

    elif secondchoice == "3":
        print_slow(f"{Fore.RED} <!> Remember that this option is a WIP so there might be lots of bugs!")
        sleep(1)
        XTitle(f"Xvirus {THIS_VERSION} Debug Console ")
        clear()
        print(f"{Fore.RED} <!> This is the dev console the background info will be printed here:{Fore.BLUE}\n")
        main1()

    elif secondchoice == "4":
        XTitle("Exiting")
        choice = input(f'{Fore.RED} <~> Are you sure you want to exit? (Y to confirm): {Fore.BLUE}')
        if choice.upper() == 'Y':
            clear()
            os._exit(0)
        else:
            sleep(0.5)
    else:
        clear()

def main():
    XTitle(f"Xvirus {THIS_VERSION}")
    clear()
    global threads
    main_banner()
    choice = input(f'{Fore.RED} [{username}] <~>: {Fore.BLUE}').lstrip("0")
    choice = choice.upper()

    if choice == "1":
        print(" <!> This option is unavailable on the exe version")#tokenlogin()
        PETC()
        main()

    elif choice == '2':
        getinfo()
        PETC()
        main()

    elif choice == '3':
        notfree()
        PETC()
        main()
                
    elif choice == '4':
        tokenbrute()
        PETC()
        main()

    elif choice == '5':
        notfree()
        PETC()
        main()

    elif choice == '6':
        checktokens()
        PETC()
        main()

    elif choice == '7':
        Xvirus_Nuke()
        PETC()
        main()

    elif choice == '8':
        notfree()
        PETC()
        main()

    elif choice == '9':
        discordrat()
        PETC()
        main()

    elif choice == '10':
        Seizure()
        PETC()
        main()

    elif choice == '11':
        Leaver()
        PETC()
        main()

    elif choice == '12':
        UnFriender()
        PETC()
        main()

    elif choice == '13':
        BlockAll()
        PETC()
        main()

    elif choice == '14':
        massdm()
        PETC()
        main()
    
    elif choice == '15':
        deletedms()
        PETC()
        main()

    elif choice == "16":
        dmclearer()
        PETC()
        main()

    elif choice == '17':
        ProfileChanger()
        PETC()
        main()

    elif choice == '18':
        snipe()
        PETC()
        main()

    elif choice == '19':
        webhooktool()
        PETC()
        main()

    elif choice == '20':
        notfree()
        PETC()
        main()

    elif choice == '21':
        notfree()
        PETC()
        main()

    elif choice == '22':
        notfree()
        PETC()
        main()

    elif choice == '23':
        notfree()
        PETC()
        main()

    elif choice == '24':
        GcSpammer()
        PETC()
        main()

    elif choice == '25':
        selfbotspammer()
        PETC()
        main()

    elif choice == '26':
        notfree()
        PETC()
        main()

    elif choice == '27':
        notfree()
        PETC()
        main()

    elif choice == '?':
        CHANGE_LOG()
        PETC()
        main()

    elif choice == 'ai':
        exec(open('util/gpt.py', encoding='utf-8').read())
        PETC()
        main()

    elif choice == 'TM':
        print(f"""                                            Development Networks:\n\n                                                GitHub:    @DXVVAY(DEXV), @Xvirus0, @2l2cgit(AdminX)\n\n\n                                            Other Networks\n\n                                                Twitter:   @DXVVAY\n                                                Discord:   .gg/xvirus, @dexvmaster, @morelikethis, @pernillevermund\n\n\n\n""")
        PETC()
        main()
    
    elif choice == 'UPD':
        update()

    elif choice == 'BUY':
        redirect()
        main
    
    elif choice == 'RPC':
        toggle_rpc()
        main()

    elif choice == '!':
        setting()
        PETC()
        main()

if __name__ == "__main__":
    import sys
    XTitle("Xvirus Loading...")
    set_terminal_width(xvirus_width)
    check_version()
    search_for_updates()
    get_username()
    proxy_scrape()
    if not os.path.exists(os.getenv("temp") + "\\xvirus_theme"):
        setTheme('xeme')
    sleep(1.5)
    main()

