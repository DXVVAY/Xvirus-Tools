import requests
import threading
from colorama import Fore

def MassReport(token, guild_id, channel_id, message_id, reason):
    for i in range(500, 1000):
        while True:
            threading.Thread(target=Report, args=(token, guild_id, channel_id, message_id, reason)).start()

def Report(token, guild_id, channel_id, message_id, reason):
    responses = {
        '401: Unauthorized': f'{Fore.RED}Invalid Discord token.',
        'Missing Access': f'{Fore.RED}Missing access to channel or guild.',
        'You need to verify your account in order to perform this action.': f'{Fore.RED}Unverified.'
    }

    report_data = {
        'channel_id': channel_id,
        'message_id': message_id,
        'guild_id': guild_id,
        'reason': reason
    }

    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'sv-SE',
        'User-Agent': 'Discord/21295 CFNetwork/1128.0.1 Darwin/19.6.0',
        'Content-Type': 'application/json',
        'Authorization': token
    }

    report = requests.post('https://discordapp.com/api/v10/report', json=report_data, headers=headers)
    
    status = report.status_code
    if status == 201:
        print(f"{Fore.GREEN}Report successfully sent!\n")
    elif status in (401, 403):
        error_message = report.json()['message']
        print(responses.get(error_message, f"{Fore.RED}Unknown error occurred.\n"))
    else:
        print(f"{Fore.RED}Error: {report.text} | Status Code: {status}\n")
