# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

# Fire Code!!!!! but it works so eh TODO make this better since its shit
def send(token, message, channel_id):  
    try:
        session = Client.get_simple_session()
        while True:
            try:
                session.headers = headers
                session.headers.update({"Authorization":token})
                data = {'session_id': utility.rand_str(32), "content": f"{message} | {utility.rand_str(7)}"}
                result = session.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", json=data)

                if result.status_code == 200:
                    Output("good", token).log(f"Success {Fore.LIGHTBLACK_EX}->{Fore.GREEN} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code})")
                elif result.text.startswith('{"captcha_key"'):
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(Captcha)")
                elif result.text.startswith('{"message": "401: Unauthorized'):
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(Unauthorized)")   
                elif result.status_code == 429:
                    pass
                elif "\"code\": 50001" in result.text:
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(No Access)")    
                elif "Cloudflare" in result.text:
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(CloudFlare Blocked)")
                elif "\"code\": 40007" in result.text:
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(Token Banned)")
                elif "\"code\": 40002" in result.text:
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(Locked Token)")
                elif "\"code\": 10006" in result.text:
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(Invalid Invite)")
                elif "\"code\": 50013" in result.text:
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}(No Access)")
                else:
                    Output("bad", token).log(f"Error {Fore.LIGHTBLACK_EX}->{Fore.RED} {message[:20]}... {Fore.LIGHTBLACK_EX}-> {token[:50]} {Fore.LIGHTBLACK_EX}({result.status_code}) {Fore.RED}({result.text})")
            except Exception as e:
                Output("bad").log(f"{e}")
    except Exception as e:
        Output("bad").log(f"{e}")

def channel_spammer():
    Output.set_title(f"Channel Spammer")
    tokens = TokenManager.get_tokens()
    channel_id = utility.ask("Channel ID")
    message = utility.ask("Message")
    max_threads = utility.ask("Thread Count")
    max_threads = int(max_threads)

    while True:
        if tokens:
            def thread_send(token):
                try:
                    token = TokenManager.OnlyToken(token)
                    args = [token, message, channel_id]
                    send(*args)
                except Exception as e:
                    print(f"{e}")

            threads = []
            for token in tokens:
                thread = threading.Thread(target=thread_send, args=(token,))
                thread.start()
                threads.append(thread)

            for thread in threads:
                thread.join()
        else:
            return
