import requests
import Xvirus

from datetime import datetime
from colorama import Fore

from util.plugins.common import getheaders

def Info(token):
    r = requests.get('https://discord.com/api/v10/users/@me', headers=getheaders(token))
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

    flags = r.json().get('flags', 0)
    if flags & Discord_Employee:
        badges += "Staff, "
    if flags & Partnered_Server_Owner:
        badges += "Partner, "
    if flags & HypeSquad_Events:
        badges += "Hypesquad Event, "
    if flags & Bug_Hunter_Level_1:
        badges += "Green Bughunter, "
    if flags & House_Bravery:
        badges += "Hypesquad Bravery, "
    if flags & House_Brilliance:
        badges += "HypeSquad Brillance, "
    if flags & House_Balance:
        badges += "HypeSquad Balance, "
    if flags & Early_Supporter:
        badges += "Early Supporter, "
    if flags & Bug_Hunter_Level_2:
        badges += "Gold BugHunter, "
    if flags & Early_Verified_Bot_Developer:
        badges += "Verified Bot Developer, "
    if not badges:
        badges = "None"

    userName = r.json().get('username') + '#' + r.json().get('discriminator')
    userID = r.json().get('id')
    phone = r.json().get('phone')
    email = r.json().get('email')
    language = r.json().get('locale')
    mfa = r.json().get('mfa_enabled')
    avatar_id = r.json().get('avatar')
    has_nitro = False
    res = requests.get('https://discordapp.com/api/v10/users/@me/billing/subscriptions', headers=getheaders(token))
    nitro_data = res.json()
    has_nitro = bool(nitro_data)
    avatar_url = f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp'
    creation_date = datetime.utcfromtimestamp(((int(userID) >> 22) + 1420070400000) / 1000).strftime('%d-%m-%Y %H:%M:%S UTC')

    if has_nitro:
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)

    billing_info = []
    for x in requests.get('https://discordapp.com/api/v10/users/@me/billing/payment-sources', headers=getheaders(token)).json():
        y = x.get('billing_address', {})
        name = y.get('name')
        address_1 = y.get('line_1')
        address_2 = y.get('line_2')
        city = y.get('city')
        postal_code = y.get('postal_code')
        state = y.get('state')
        country = y.get('country')
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
    [{Fore.RED}Expires in{Fore.RESET}]      {days_left if has_nitro else ""}
    {Fore.RESET}{Fore.GREEN}<───────Billing Information──────->{Fore.RESET}''')

    for info in billing_info:
        print(f'''
        {Fore.RESET}{Fore.GREEN}<<───────{info['Payment Type']}──────->>{Fore.RESET}
        [{Fore.RED}Valid{Fore.RESET}]               {info['Valid']}
        [{Fore.RED}Default Payment{Fore.RESET}]    {info['Default Payment']}
        [{Fore.RED}Address 1{Fore.RESET}]          {info['Address 1']}
        [{Fore.RED}Address 2{Fore.RESET}]          {info['Address 2']}
        [{Fore.RED}City{Fore.RESET}]                {info['City']}
        [{Fore.RED}Postal Code{Fore.RESET}]         {info['Postal Code']}
        [{Fore.RED}State{Fore.RESET}]               {info['State']}
        [{Fore.RED}Country{Fore.RESET}]             {info['Country']}''')

    print(f'{Fore.RESET}{Fore.GREEN}<<───────────────End──────────────->>{Fore.RESET}')
