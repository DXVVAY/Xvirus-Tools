import random
import string
import requests
import os
import concurrent.futures
from colorama import Fore
from util.plugins.common import *

def generate_random_numbers(length):
    numbers = string.digits
    return ''.join(random.choice(numbers) for _ in range(length))

def generate_random_letters_digits(length):
    letters_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_digits) for _ in range(length))

def check_webhook_validity(webhook_url):
    try:
        response = requests.get(webhook_url)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def save_valid_webhook(webhook):
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)
    output_file = os.path.join(output_directory, "validwebhooks.txt")
    with open(output_file, "a") as file:
        file.write(webhook + "\n")

def generate_and_save_valid_webhook():
    def find_valid_webhook():
        while True:
            random_part1 = generate_random_numbers(19)
            random_part2 = generate_random_letters_digits(43)
            webhook_url = f"https://discord.com/api/webhooks/{random_part1}/{random_part2}"
            with concurrent.futures.ThreadPoolExecutor() as executor:
                future = executor.submit(check_webhook_validity, webhook_url)
                is_valid = future.result()
            if is_valid:
                return webhook_url
            else:
                print(f"{Fore.RED}Invalid webhook:", webhook_url)

    valid_webhook = find_valid_webhook()
    print(f"{Fore.BLUE}Valid webhook:", valid_webhook)

    save_valid_webhook(valid_webhook)
    print("Valid webhook saved to output/validwebhooks.txt.")

