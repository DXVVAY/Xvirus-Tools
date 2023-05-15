# Import the necessary modules
import openai
import os
import getpass
from subprocess import Popen, PIPE, STDOUT

# Set the API key and some initial parameter values
api_key = str(input(f"""Paste In Your OpenAI API : """))
temperature = 0.5 # 0 to 1
max_tokens = 2000 # max 4000
personality = ""
directory = os.getcwd()

# Check the operating system and set the appropriate command to clear the terminal screen
if os.name == 'nt':
    clear = lambda: os.system('cls')
else:
    clear = lambda: os.system('clear')

# Define a function to clear the terminal screen
def clearScreen():
  clear()
  print("""
██╗  ██╗ ██████╗██╗██████╗ ███████╗   █████╗ ██╗
╚██╗██╔╝██╔════╝██║██╔══██╗██╔════╝  ██╔══██╗██║
 ╚███╔╝ ╚█████╗ ██║██║  ██║█████╗    ███████║██║
 ██╔██╗  ╚═══██╗██║██║  ██║██╔══╝    ██╔══██║██║
██╔╝╚██╗██████╔╝██║██████╔╝███████╗  ██║  ██║██║
╚═╝  ╚═╝╚═════╝ ╚═╝╚═════╝ ╚══════╝  ╚═╝  ╚═╝╚═╝
/xside (Prompt) To use the ai                   """)

# Call the function to clear the terminal screen
clearScreen()

# Prompt the user for their API key if it hasn't been provided in the code already
if api_key == "":
  openai.api_key = getpass.getpass(prompt="OpenAI API Key")
else:
  openai.api_key = api_key

# Enter a while loop to continually prompt the user for input and generate responses from the OpenAI API
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

    # Print the generated response
    print("[AI]:" + response["choices"][0]["text"].strip())
  else:
    # Execute the command as a normal terminal command
    process = Popen(user_input, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
    output, errors = process.communicate()
    print(output.decode())
