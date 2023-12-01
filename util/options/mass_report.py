# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(channel_id, message_id, token):
    while True:
        reasons = {
            31: "MESSAGE_SPAM",
            34: "ABUSE_OR_HARASSMENT"
        }
        reason = random.choice(list(reasons.keys()))
        data = {
            "version": "1.0",
            "variant": "3",
            "language": "en",
            "breadcrumbs": [
                3,
                reason
            ],
            "elements": {},
            "name": "message",
            "channel_id": channel_id,
            "message_id": message_id
        }
        session = Client.get_session(token)
        result = session.post(f"https://discord.com/api/v9/reporting/message", json=data)

        if result.status_code == 200:
            Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
        else:
            Output.error_logger(token, result.text, result.status_code)

def mass_report():
    Output.set_title(f"Mass Report")
    message = utility.message_info()
    channel_id = message["channel_id"]
    message_id = message["message_id"]
    max_threads = utility.ask("Thread Count")
    utility.run_threads(max_threads=max_threads, func=send, args=[channel_id, message_id])
