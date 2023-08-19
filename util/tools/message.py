import ctypes
import os
import threading
from datetime import datetime
from pathlib import Path

import requests
from colorama import Fore

from util.plugins.common import *


def send_message(token, channel_id, message):
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json'
    }
    payload = {
        'content': message
    }
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
    if r.status_code == 200:
        print(f" <*> Message sent: {message}")
    else:
        print(f" <!> Error sending message: {r.status_code} {r.text}")

def read_messages(token, channel_id):
    headers = {
        'Authorization': f'Bot {token}',
        'Content-Type': 'application/json'
    }
    last_message_id = None
    url = f'https://discord.com/api/v9/channels/{channel_id}/messages'
    while True:
        params = {'after': last_message_id} if last_message_id else None
        r = requests.get(url, headers=headers, params=params)
        if r.status_code == 200:
            messages = r.json()
            if messages:
                for message in messages:
                    if message.get('type') == 0:
                        timestamp = message['timestamp']
                        content = message['content']
                        formatted_timestamp = format_timestamp(timestamp)
                        print(f"[{formatted_timestamp}] {content}")
                    last_message_id = message['id']
        else:
            print(f" <!> Error reading messages: {r.status_code} {r.text}")

def format_timestamp(timestamp):
    dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def send_and_receive_messages(token, channel_id, is_bot=False):
    if is_bot:
        send_thread = threading.Thread(target=send_messages, args=(token, channel_id))
    else:
        send_thread = threading.Thread(target=send_user_messages, args=(token, channel_id))
    receive_thread = threading.Thread(target=read_messages, args=(token, channel_id))
    receive_thread.start()
    send_thread.start()
    receive_thread.join()
    send_thread.join()

def send_messages(token, channel_id):
    while True:
        message = input(" <~> Enter message: ")
        send_message(token, channel_id, message)

def send_user_messages(token, channel_id):
    while True:
        message = input(" <~> Enter message: ")
        headers = {
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        payload = {
            'content': message
        }
        r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
        if r.status_code == 200:
            print(f" <*> Message sent: {message}")
        else:
            print(f" <!> Error sending message: {r.status_code} {r.text}")

def messanger():
    XTitle("Console Based Discord Client")
    token = input(f"{Fore.RED} <~> Token: {Fore.BLUE}")
    is_bot = input(" <~> Is it a bot token? (y/n): ").lower() == "y"
    channel_id = input(" <~> Enter channel id: ")
    os.system("pause")
    os.system("cls")
    send_and_receive_messages(token, channel_id, is_bot)