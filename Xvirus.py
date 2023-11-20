from util import *

class menus:
    def cred():
        print(f'''
    {Fore.BLUE}[{Fore.RED}Github{Fore.BLUE}] @DXVVAY(DEXV), @Xvirus0, @2l2cgit(AdminX)
    {Fore.BLUE}[{Fore.RED}Twitter{Fore.BLUE}] @dexvisnotgay
    {Fore.BLUE}[{Fore.RED}Discord{Fore.BLUE}] .gg/xvirustool, @dexv, @adminxfr
        ''')
        Output.PETC()

    def change_log():
        print(f'''
    1. Xvirus Free Full Recode
    2. Xvirus Self DEAD -> Xvirus Raider FR
    3. Multiple Tokens Support
    4. Added Token Joiner/Leaver
    5. Added Channel Spammer
    6. Better Config System 
    7. Added Better Proxy Support
    8. Better Settings
    9. All tools unflagged
    10. Unflagged All Profile Changers
    11. Added Soundboard Spammer (Must Be In A VC)
    12. Added Fake Typer
    13. Added Message Mass Report
        ''')
        Output.PETC()

    def notes():
        print(f'''<!> IMPORTANT NOTES!

    1. When you wanna save your tokens make sure your txt file has every new token in a new line.
        ''')
        Output.PETC()

    def joiner_menu():
        utility.make_menu(f"Normal Mode", f"RestoreCord Mode {Fore.RED}(bypass captcha)")
        choice = utility.ask("Choice")
        if choice == '1':
            token_joiner()
        else:
            gui.not_free()
    
    def checker_menu():
        utility.make_menu("Cache Checker", "Custom Checker", "Server Checker")
        choice = utility.ask("Choice")
        if choice == '1':
            tokens = TokenManager.get_tokens()
            token_checker(tokens)
        elif choice == '2':
            path = utility.ask("Enter the custom path to load tokens from").strip()
            tokens = TokenManager.custom_path(path)
            token_checker(tokens)
        elif choice == '3':
            gui.not_free()

class gui:
    def get_tokens():
        f = config.read('xvirus_tokens')
        tokens = f.strip().splitlines()
        tokens = [token for token in tokens if token not in [" ", "", "\n"]]
        return tokens
    
    def get_proxies():
        f = config.read('xvirus_proxies')
        proxies = f.strip().splitlines()
        proxies = [proxy for proxy in proxies if proxy not in [" ", "", "\n"]]
        return proxies
    
    def not_free():
        Output.set_title("This Option Is Not Free")
        Output("info").notime("You can unlock this options by purchasing the premium version of xvirus!")
        Output.PETC()
    
    def WIP():
        Output.set_title("This Option Is A Work In Progress")
        Output("info").notime("This options is currently unavailable, please be patient and it will be added later.")
        Output.PETC()

    def print_menu():
        pc_username = config._get("xvirus_username")
        theme = config._get("xvirus_theme")
        theme = getattr(Fore, theme)
        lb = Fore.LIGHTBLACK_EX
        r = theme
        logo = f'''{r}
                                                                                  
                                         ,.   (   .      )        .      "        
                                       ("     )  )'     ,'        )  . (`     '`   
                                     .; )  ' (( (" )    ;(,     ((  (  ;)  "  )"  │Tokens: {len(gui.get_tokens())}
                                    _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.. │Proxies: {len(gui.get_proxies())}
                                    ██╗  ██╗██╗   ██╗██╗██████╗ ██╗   ██╗ ██████╗ ├─────────────
                                    ╚██╗██╔╝██║   ██║██║██╔══██╗██║   ██║██╔════╝ │Running on:
                                     ╚███╔╝ ╚██╗ ██╔╝██║██████╔╝██║   ██║╚█████╗  │{pc_username}\'s PC
                                     ██╔██╗  ╚████╔╝ ██║██╔══██╗██║   ██║ ╚═══██╗ ├─────────────
                                    ██╔╝╚██╗  ╚██╔╝  ██║██║  ██║╚██████╔╝██████╔╝ │Discord link:          
> [TM] Made by Xvirus™              ╚═╝  ╚═╝   ╚═╝   ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝  │.gg/xvirustool
> [?] {THIS_VERSION} Changelog                                                                                     Notes [NOTE] <
> [!] Settings                                                                                     Manage Tokens [TKN] <'''

        options = f'''{r} 
{r}╔═══                              ═══╗ ╔═══                               ═══╗ ╔═══                                 ═══╗
{r}║   ({lb}01{r}) {lb}> Token Joiner              {r}║ ║   {r}({lb}10{r}) {lb}> Global Nick Changer        {r}║ ║   {r}({lb}19{r}) {lb}> User Mass Friend{r}             ║
{r}    ({lb}02{r}) {lb}> Token Leaver                    {r}({lb}11{r}) {lb}> Server Nick Changer              {r}({lb}20{r}) {lb}> User Mass DM{r}
{r}    ({lb}03{r}) {lb}> Token Spammer                   {r}({lb}12{r}) {lb}> HypeSquad Changer                {r}({lb}21{r}) {lb}> Mass Report{r}
{r}    ({lb}04{r}) {lb}> Multi Checker                   {r}({lb}13{r}) {lb}> Bio Changer                      {r}({lb}22{r}) {lb}> Mass Thread{r}
{r}    ({lb}05{r}) {lb}> Bypass Rules                    {r}({lb}14{r}) {lb}> Pronouns Changer                 {r}({lb}23{r}) {lb}> WebHook Tool{r}
{r}    ({lb}06{r}) {lb}> Bypass RestoreCord              {r}({lb}15{r}) {lb}> Voice Chat Joiner                {r}({lb}24{r}) {lb}> N/A{r}
{r}    ({lb}07{r}) {lb}> Bypass Sledge Hammer            {r}({lb}16{r}) {lb}> Sound Board Spammer              {r}({lb}25{r}) {lb}> N/A{r}
{r}    ({lb}08{r}) {lb}> Button Presser                  {r}({lb}17{r}) {lb}> Fake Typer                       {r}({lb}26{r}) {lb}> N/A{r}
{r}║   ({lb}09{r}) {lb}> Message Reactor           {r}║ ║   {r}({lb}18{r}) {lb}> Forum Spammer               {r}║ ║  {r}({lb}27{r}) {lb}> N/A{r}                          ║
{r}╚═══                              ═══╝ ╚═══                                ═══╝ ╚═══                                ═══╝'''

        ascii = pystyle.Center.XCenter(logo)
        ops = pystyle.Center.XCenter(options)
        print(ascii)
        print(ops)

    def main_menu():
        while True:
            theme = config._get("xvirus_theme")
            theme = getattr(Fore, theme)
            lb = Fore.LIGHTBLACK_EX
            r = theme
            utility.clear()
            Output.set_title(f"Xvirus {THIS_VERSION}")
            gui.print_menu()
            pc_username = config._get("xvirus_username")
            print(f'{r}┌──<{pc_username}@Xvirus>─[~]')
            choicee = input(f'└──╼ $ {Fore.BLUE}').lstrip("0")
            choice = choicee.upper()

            try:
                options = {
                    '1': menus.joiner_menu,
                    '2': token_leaver,
                    '3': channel_spammer,
                    '4': menus.checker_menu,
                    '5': bypass_rules,
                    '6': gui.not_free,
                    '7': gui.not_free,
                    '8': gui.not_free,
                    '9': gui.not_free,
                    '10': global_nicker,
                    '11': server_nicker,
                    '12': hypesquad_changer,
                    '13': token_bio_changer,
                    '14': token_pron_changer,
                    '15': gui.WIP,
                    '16': soundboard_spammer,
                    '17': token_typer,
                    '18': gui.not_free,
                    '19': gui.not_free,
                    '20': gui.not_free,
                    '21': mass_report,
                    '22': gui.not_free,
                    '23': webhook_tool,
                    '!': settings,
                    'TKN': token_manager,
                    'TM': menus.cred,
                    '?': menus.change_log,
                    'NOTE': menus.notes,

                }
                choosen = options.get(choice)
                if choosen:
                    choosen()
                    time.sleep(1)
                else:
                    Output("bad").notime("Invalid choice, please try again!")
                    sleep(1)

            except Exception as e:
                Output("bad").notime(e)
                input()

            gui.main_menu()

if __name__ == "__main__":
    utility.clear()
    Output.set_title("Xvirus Loading")
    gui.main_menu()
