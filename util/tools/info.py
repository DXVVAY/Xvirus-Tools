from datetime import datetime

import requests
from colorama import Fore

from util.plugins.common import *


def get_cc_digits():
    return {
        'american express': '3',
        'visa': '4',
        'mastercard': '5'
    }

def get_badges(flags):
    badge_flags = {
        1: "Staff",
        2: "Partner",
        4: "Hypesquad Events",
        8: "Bug Hunter Level 1",
        16: "House Bravery",
        32: "House Brilliance",
        64: "House Balance",
        128: "Early Supporter",
        256: "Team User",
        512: "System",
        1024: "Bug Hunter Level 2",
        4096: "Verified Bot",
        16384: "Early Verified Bot Developer",
        65536: "Discord Certified Moderator"
    }

    badges = [badge_flags[flag] for flag in badge_flags if flag & flags]
    return ', '.join(badges) if badges else "None"

def get_creation_date(userID):
    timestamp = ((int(userID) >> 22) + 1420070400000) / 1000
    return datetime.utcfromtimestamp(timestamp).strftime('%d-%m-%Y %H:%M:%S UTC')

def get_avatar_url(userID, avatar_id):
    return f'https://cdn.discordapp.com/avatars/{userID}/{avatar_id}.webp' if avatar_id else ""

def get_payment_info(token):
    payment_info = []
    billing_sources_url = 'https://discord.com/api/v9/users/@me/billing/payment-sources'
    billing_sources = requests.get(billing_sources_url, headers=getheaders(token)).json()

    cc_digits = get_cc_digits()
    for source in billing_sources:
        billing_address = source.get('billing_address', {})
        payment_type = ""
        data = {
            'Valid': not source['invalid'],
            'Default Payment': source['default'],
            'Address 1': billing_address.get('line_1', ""),
            'Address 2': billing_address.get('line_2', ""),
            'City': billing_address.get('city', ""),
            'Postal Code': billing_address.get('postal_code', ""),
            'State': billing_address.get('state', ""),
            'Country': billing_address.get('country', "")
        }

        if source['type'] == 1:
            cc_brand = source['brand']
            cc_first = cc_digits.get(cc_brand)
            cc_last = source['last_4']
            cc_month = str(source['expires_month'])
            cc_year = str(source['expires_year'])
            payment_type = 'Credit Card'
            data.update({
                'Payment Type': payment_type,
                'CC Holder Name': billing_address.get('name', ""),
                'CC Brand': cc_brand.title(),
                'CC Number': ''.join(z if (i + 1) % 2 else z + ' ' for i, z in enumerate((cc_first if cc_first else '*') + ('*' * 11) + cc_last)),
                'CC Exp. Date': ('0' + cc_month if len(cc_month) < 2 else cc_month) + '/' + cc_year[2:4],
            })
        elif source['type'] == 2:
            payment_type = 'PayPal'
            data.update({
                'Payment Type': payment_type,
                'PayPal Name': billing_address.get('name', ""),
                'PayPal Email': source['email']
            })
        payment_info.append(data)

    return payment_info

def Info(token):
    XTitle("Getting Token Info")
    user_info_url = 'https://discord.com/api/v9/users/@me'
    user_info = requests.get(user_info_url, headers=getheaders(token)).json()

    flags = user_info.get('flags', 0)
    badges = get_badges(flags)

    userID = user_info.get('id')
    userName = user_info.get('username')
    discriminator = user_info.get('discriminator')


    if discriminator == "0":
        discriminator = "N/A (New Username System)"
    else:
        discriminator = discriminator.lstrip('#')

    if discriminator:
        full_username = f"{userName}#{discriminator}"
    else:
        full_username = userName
    language = user_info.get('locale')
    mfa_enabled = user_info.get('mfa_enabled')
    avatar_id = user_info.get('avatar')
    email = user_info.get('email')
    phone = user_info.get('phone')


    has_nitro = False
    nitro_subscriptions_url = 'https://discord.com/api/v9/users/@me/billing/subscriptions'
    nitro_data = requests.get(nitro_subscriptions_url, headers=getheaders(token)).json()
    if nitro_data:
        has_nitro = True
        d1 = datetime.strptime(nitro_data[0]["current_period_end"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        d2 = datetime.strptime(nitro_data[0]["current_period_start"].split('.')[0], "%Y-%m-%dT%H:%M:%S")
        days_left = abs((d2 - d1).days)
    else:
        days_left = ""

    avatar_url = get_avatar_url(userID, avatar_id)
    creation_date = get_creation_date(userID)

    billing_info = get_payment_info(token)

    print(f'''
    {Fore.BLUE}<<────────────{userName}────────────>>
    {Fore.RED}[Discriminator]   {discriminator}
    {Fore.RED}[User ID]         {userID}
    {Fore.RED}[Created at]      {creation_date}
    {Fore.RED}[Language]        {language}
    {Fore.RED}[Badges]          {badges}
    {Fore.RED}[Avatar URL]      {avatar_url}
    {Fore.RED}[Token]           {token}
    {Fore.BLUE}<───────────Security Info───────────>
    {Fore.RED}[2 Factor]        {mfa_enabled}
    {Fore.RED}[Email]           {email}
    {Fore.RED}[Phone number]    {phone if phone else ""}
    {Fore.BLUE}<────────────Nitro Info─────────────>
    {Fore.RED}[Nitro Status]    {has_nitro}
    {Fore.RED}[Expires in]      {days_left if has_nitro else ""}
    {Fore.BLUE}<───────Billing Information───────>''')

    for info in billing_info:
        print(f'''
        {Fore.BLUE}<<───────{info['Payment Type']}──────->>
        {Fore.RED}[Valid]               {info['Valid']}
        {Fore.RED}[Default Payment]    {info['Default Payment']}
        {Fore.RED}[Address 1]          {info['Address 1']}
        {Fore.RED}[Address 2]          {info['Address 2']}
        {Fore.RED}[City]                {info['City']}
        {Fore.RED}[Postal Code]         {info['Postal Code']}
        {Fore.RED}[State]               {info['State']}
        {Fore.RED}[Country]             {info['Country']}
        ''')
        


def getinfo():
        token = input(f'{Fore.RED} <~> Token: {Fore.BLUE}')
        CheckToken(token)
        Info(token)
