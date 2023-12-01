# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def spammer(webhook, Message):
    session = Client.get_simple_session()
    result = session.post(webhook, json={"content": Message})
    if result.status_code == 204:
        Output("good").log(f"Sent -> {Message[:70]} {Fore.LIGHTBLACK_EX}({result.status_code})")
    else:
        Output.error_logger(Message, result.text, result.status_code)

def webhook_spammer():
    webhook = utility.ask("Webhook")
    message = utility.ask("Message")
    utility.CheckWebhook(webhook)
    max_threads = utility.asknum("Thread Count")
    max_threads = int(max_threads)

    def thread_complete(future):
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

    while True:
        with ThreadPoolExecutor(max_workers=max_threads) as executor:
            try:
                args = [webhook, message]
                future = executor.submit(spammer, *args)
                future.add_done_callback(thread_complete)
                time.sleep(0.1)
            except Exception as e:
                Output("bad").log(f"Error: {e}")

def webhook_tool():
    Output.set_title(f"Webhook Tool")
    utility.make_menu("Webhook Spammer", "Webhook Deleter")
    choice = utility.ask("Choice")

    if choice == '1':
        webhook_spammer()
    
    if choice == '2':
        session = Client.get_simple_session()
        webhook = utility.ask("Webhook")
        Checker('webhook', webhook)
        session.delete(webhook)
        Output("good").notime("Webhook successfully deleted")

