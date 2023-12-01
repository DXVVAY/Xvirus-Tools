# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def token_manager():
    Output.set_title(f"Token Manager")
    utility.make_menu("Save Tokens", "Clear Tokens")
    choice = utility.ask("Choice")

    if choice == '1':
        check = utility.ask("Check Tokens And Only Save Valid Ones (y/n)")
        if check == 'y':
            checker()
        else:
            saver()

    if choice == '2':
        config.reset('xvirus_tokens')
        Output("info").notime("Tokens Cache Emptied.")
        Output.PETC()
    
    if choice == '3':
        choose_store()

def checker():
    valid = 0
    locked = 0
    invalid = 0
    error = 0
    
    token_file_path = utility.ask("Enter the path to the text file containing tokens").strip()
    tokens = TokenManager.custom_path(token_file_path)

    def check_token(token):
        nonlocal valid, locked, invalid, error
        session = Client.get_simple_session()
        session.headers = headers
        session.headers.update({"Authorization":token})
        result = session.get("https://discord.com/api/v9/users/@me/settings")

        if result.status_code == 200:
            Output("good", token).log(f"Valid -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
            valid += 1
            config.add('xvirus_tokens', token)
        elif "You need to verify your account in order to perform this action." in result.text:
            Output("info", token).log(f"Locked -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
            locked += 1
        elif "Unauthorized" in result.text:
            Output("bad", token).log(f"Invalid -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
            invalid += 1
        else:
            error += 1

    def thread_complete(future):
        nonlocal valid, locked, invalid, error
        debug = config._get("debug_mode")
        try:
            result = future.result()
        except Exception as e:
            if debug:
                if "failed to do request" in str(e):
                    message = f"Proxy Error -> {str(e)[:80]}..."
                else:
                    message = f"Error -> {e}"
                Output("dbg").log(message)
            else:
                pass

    max_threads = utility.ask("Thread Count")
    max_threads = int(max_threads)

    if tokens:
        start_time = time.time()

        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            for token in tokens:
                try:
                    token = TokenManager.OnlyToken(token)
                    args = [token]
                    future = executor.submit(check_token, *args)
                    future.add_done_callback(thread_complete)
                    time.sleep(0.1)
                except Exception as e:
                    Output("bad").log(f"{e}")

        elapsed_time = time.time() - start_time
        Output("info").notime(f"Checked {len(tokens)} Tokens In {elapsed_time:.2f} Seconds")

        info = [
            f"{Fore.LIGHTGREEN_EX}Valid: {str(valid)}",
            f"{Fore.LIGHTBLACK_EX}Locked: {str(locked)}",
            f"{Fore.LIGHTRED_EX}Invalid: {str(invalid)}",
            f"{Fore.LIGHTCYAN_EX}Errors: {str(error)}"
        ]

        status = f"{Fore.RED} | ".join(info) + f"{Fore.RED}\n"
        print(f" {status}")
        
        Output.PETC()
    else:
        Output("bad").log(f"No tokens were found in the specified text file")
        Output.PETC()

def saver():
    token_file_path = utility.ask("Enter the path to the text file containing tokens").strip()
    tokens = TokenManager.custom_path(token_file_path)
    for token in tokens:
        tokne = TokenManager.OnlyToken(token)
        config.add('xvirus_tokens', token)
        Output("good").log(f"Saved -> {token}") 
        sleep(0.1)

    Output.PETC()
