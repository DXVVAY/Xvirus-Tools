import openai
import os
import getpass
from subprocess import Popen, PIPE, STDOUT

api_key = str(input(f""" <~> OpenAI API KEY: """))
temperature = 0.5
max_tokens = 2000
personality = ""
directory = os.getcwd()

if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

def banner():
  clear()
  print("""
██╗  ██╗ ██████╗██╗██████╗ ███████╗   █████╗ ██╗
╚██╗██╔╝██╔════╝██║██╔══██╗██╔════╝  ██╔══██╗██║
 ╚███╔╝ ╚█████╗ ██║██║  ██║█████╗    ███████║██║
 ██╔██╗  ╚═══██╗██║██║  ██║██╔══╝    ██╔══██║██║
██╔╝╚██╗██████╔╝██║██████╔╝███████╗  ██║  ██║██║
╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝ ╚══════╝  ╚═╝  ╚═╝╚═╝
/xside (Prompt) To use the ai                   """)

banner()

if api_key == "":
  openai.api_key = getpass.getpass(prompt="OpenAI API Key")
else:
  openai.api_key = api_key

while True:
  user_input = input(directory + ">")
  
  if user_input.startswith('/xside'):
    response = openai.Completion.create(
      model="text-davinci-003",
      prompt=personality + user_input[1:],
      temperature=temperature,
      max_tokens=max_tokens,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )

    print("[AI]:" + response["choices"][0]["text"].strip())
  else:
    process = Popen(user_input, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output, errors = process.communicate()
    print(output.decode())
