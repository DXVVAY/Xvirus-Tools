import requests

def send_message(username, message):
    url = 'https://chat.xvirus.xyz//send'
    data = {'username': username, 'message': message}
    response = requests.post(url, json=data)
    print(response.text)

def get_messages():
    url = 'https://chat.xvirus.xyz//messages'
    response = requests.get(url)
    messages = response.json()
    return messages

username = input('Enter your username: ')

while True:
    message = input('Enter a message (or "exit" to quit): ')
    if message == 'exit':
        break
    send_message(username, message)
    received_messages = get_messages()
    for msg in received_messages:
        print(f"{msg['username']}: {msg['message']}")
