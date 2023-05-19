import requests
import os
import ctypes
import threading
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

def send_message(token, channel_id, message):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    payload = {
        'content': message
    }
    r = requests.post(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers, json=payload)
    if r.status_code == 200:
        print(f"Message sent: {message}")
    else:
        print(f"Error sending message: {r.status_code} {r.text}")

def read_messages(token, channel_id, log_file):
    headers = {
        'Authorization': token,
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
                        write_to_xml(log_file, formatted_timestamp, content)
                    last_message_id = message['id']
        else:
            print(f"Error reading messages: {r.status_code} {r.text}")

def format_timestamp(timestamp):
    dt = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%f%z')
    return dt.strftime('%Y-%m-%d %H:%M:%S')

def write_to_xml(file_path, timestamp, content):
    root = ET.Element("messages")
    tree = ET.ElementTree(root)
    message_element = ET.SubElement(root, "message")
    timestamp_element = ET.SubElement(message_element, "timestamp")
    timestamp_element.text = timestamp
    content_element = ET.SubElement(message_element, "content")
    content_element.text = content
    tree.write(file_path, encoding="utf-8", xml_declaration=True)

def send_and_receive_messages(token, channel_id, log_file):
    send_thread = threading.Thread(target=send_messages, args=(token, channel_id))
    receive_thread = threading.Thread(target=read_messages, args=(token, channel_id, log_file))
    receive_thread.start()
    send_thread.start()
    receive_thread.join()
    send_thread.join()

def send_messages(token, channel_id):
    while True:
        message = input("Enter message: ")
        send_message(token, channel_id, message)

def main():
    token = input("Enter token: ")
    channel_id = input("Enter channel id: ")

    # Create XML log file in Downloads directory
    downloads_dir = Path.home() / 'Downloads'
    log_file = downloads_dir / 'discord_log.xml'

    os.system("pause")
    ctypes.windll.kernel32.SetConsoleTitleW("Console Based Discord Client")
    os.system("cls")
    send_and_receive_messages(token, channel_id, log_file)

if __name__ == "__main__":
    main()
