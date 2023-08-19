import asyncio
import aiohttp
import threading
from colorama import Fore
from util.plugins.common import *

BATCH_SIZE = 5

def getheaders(token):
    return {'Authorization': token}

async def check_tokens_batch(session, tokens, valid_tokens, invalid_tokens, locked_tokens):
    tasks = []
    for token in tokens:
        extracted_token = extract(token)
        task = check_token(session, extracted_token, valid_tokens, invalid_tokens, locked_tokens)
        tasks.append(task)
    await asyncio.gather(*tasks)

async def check_token(session, token, valid_tokens, invalid_tokens, locked_tokens):
    try:
        async with session.get('https://discord.com/api/v9/users/@me', headers=getheaders(token)) as response:
            if response.status == 200:
                valid_tokens.append(token)
                print(f"{Fore.GREEN} <*> Valid{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status})")
            elif response.status == 401 or response.status == 403:
                locked_tokens.append(token)
                print(f"{Fore.LIGHTBLACK_EX} <~> Locked{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status})")
            elif response.status == 404:
                invalid_tokens.append(token)
                print(f"{Fore.RED} <!> Invalid{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status})")
            else:
                print(f"{Fore.LIGHTRED_EX} <!> Error{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} ({response.status})")
    except Exception as e:
        locked_tokens.append(token)
        print(f"{Fore.LIGHTBLACK_EX} <~> Locked{Fore.BLUE} {token}{Fore.LIGHTBLACK_EX} (Error: {e})")

def threaded_checker(tokens, valid_tokens, invalid_tokens, locked_tokens):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def token_checker():
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit_per_host=5)) as session:
            for i in range(0, len(tokens), BATCH_SIZE):
                batch = tokens[i:i + BATCH_SIZE]
                await check_tokens_batch(session, batch, valid_tokens, invalid_tokens, locked_tokens)

    loop.run_until_complete(token_checker())

def token_checker_threaded(tokens):
    valid_tokens = []
    invalid_tokens = []
    locked_tokens = []

    threads = []
    num_threads = len(tokens) // BATCH_SIZE + 1

    for i in range(num_threads):
        start_idx = i * BATCH_SIZE
        end_idx = (i + 1) * BATCH_SIZE
        thread_tokens = tokens[start_idx:end_idx]
        t = threading.Thread(target=threaded_checker, args=(thread_tokens, valid_tokens, invalid_tokens, locked_tokens))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    return valid_tokens, invalid_tokens, locked_tokens

def checktokens():
    path = input(f" {Fore.RED}<~> Enter the path to the tokens file: {Fore.BLUE}")
    with open(path, 'r') as f:
        tokens = [line.strip() for line in f]

    valid_tokens, invalid_tokens, locked_tokens = token_checker_threaded(tokens)

    print("\n")
    print(f"{Fore.GREEN} <*> Valid: {len(valid_tokens)}{Fore.RED}\n <!> Invalid: {len(invalid_tokens)}{Fore.LIGHTBLACK_EX}\n <~> Locked: {len(locked_tokens)} ")

    with open(path, 'w') as f:
        for token in valid_tokens:
            f.write(token + "\n")