# coding: utf-8
# Copyright (C) 2023 github.com/Xvirus-Team

from util import *

def send(channel_id, sounds: list[dict[str, typing.Union[str, int]]], token):
    session = Client.get_session(token)
    while True:
        sound = random.choice(sounds)
        data = {
            "sound_id":sound.get("sound_id"),
            "emoji_id":None,
            "emoji_name":sound.get("emoji_name"),
            "override_path": sound.get("override_path")
        }
        result = session.post(f"https://discord.com/api/v9/channels/{channel_id}/voice-channel-effects", json=data)
        if result.status_code == 204:
            Output("good", token).log(f"Success -> {token} {Fore.LIGHTBLACK_EX}({result.status_code})")
        elif result.status_code == 429:
            pass
        else:
            Output.error_logger(token, result.text, result.status_code)

def soundboard_spammer():
    Output.set_title(f"Sound Board Spammer")
    tokenn = TokenManager.get_random_token()
    session = Client.get_session(tokenn)
    headerss = session.headers
    channel_id = utility.ask("Channel ID")
    max_threads = utility.ask("Thread Count")
    sounds = requests.get("https://discord.com/api/v9/soundboard-default-sounds", headers=headerss).json()
    utility.run_threads(max_threads=max_threads, func=leave, args=[channel_id, sounds])
