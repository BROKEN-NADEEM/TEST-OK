import requests
import time
import sys
import os
from datetime import datetime

# एनीमेशन फंक्शन (टेक्स्ट को धीरे-धीरे प्रिंट करेगा)
def animated_text(text, delay=0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# लोडिंग एनिमेशन
def loading_animation(message, duration=3):
    animation = "|/-\\"
    for i in range(duration * 4):  
        sys.stdout.write(f"\r{message} {animation[i % len(animation)]}")
        sys.stdout.flush()
        time.sleep(0.2)
    print("\r" + " " * (len(message) + 2), end="\r")  

# क्लियर स्क्रीन और लोगो दिखाएं (एनिमेशन के साथ)
os.system("clear")
logo = """
\x1b[1;36m
  _          _______    ______     _______    _______    _______      _______    _         _________
 ( (    /|  (  ___  )  (  __  \   (  ____ \  (  ____ \  (       )    (  ___  )  ( \        \__   __/
 |  \  ( |  | (   ) |  | (  \  )  | (    \/  | (    \/  | () () |    | (   ) |  | (           ) (   
 |   \ | |  | (___) |  | |   ) |  | (__      | (__      | || || |    | (___) |  | |           | |   
 | (\ \) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |    |  ___  |  | |           | |   
 | | \   |  | (   ) |  | |   ) |  | (        | (        | |   | |    | (   ) |  | |           | |   
 | )  \  |  | )   ( |  | (__/  )  | (____/\  | (____/\  | )   ( |    | )   ( |  | (____/\  ___) (___
 |/    )_)  |/     \|  (______/   (_______/  (_______/  |/     \|    |/     \|  (_______/  \_______/                                                                                                   
"""
animated_text(logo, 0.001)

# स्टार्ट टाइम दिखाएं
print("\033[92mSTART TIME :", time.strftime("%Y-%m-%d %H:%M:%S"))

# पासवर्ड एंटर करने का एनिमेशन
def pas():
    animated_text("\n\033[1;32mChecking Password...\n")
    time.sleep(1)
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜  ") 
    mmm = requests.get('https://pastebin.com/raw/8pEpSkpa').text

    if mmm not in password:
        animated_text("\033[1;33m𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗! \n")
        sys.exit()
    animated_text("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 𝗖𝗢𝗥𝗥𝗘𝗖𝗧! 𝗟𝗢𝗚𝗜𝗡 𝗦𝗨𝗖𝗖𝗘𝗦𝗦𝗙𝗨𝗟.\n")
pas()

# लोडिंग स्क्रीन दिखाएं
loading_animation("𝗟𝗼𝗮𝗱𝗶𝗻𝗴 𝗧𝗼𝗼𝗹𝘀", 5)

# यूज़र इनपुट्स
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
animated_text("\033[1;32mReading Token File...\n")
time.sleep(1)

# Access Token लोड करें
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

num_user_ids = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗡𝗨𝗠𝗕𝗘𝗥 𝗢𝗙 𝗣𝗢𝗦𝗧𝗦 ➜ "))

user_messages = {}
haters_name = {}

# User Input Collection Animation
for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗣𝗢𝗦𝗧 𝗜𝗗 ➜ ")
    hater_name = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗘𝗥'𝗦 𝗡𝗔𝗠𝗘 ➜ ")
    haters_name[user_id] = hater_name
    message_file = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘 ➜ ")
    user_messages[user_id] = message_file

delay_time = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 𝗜𝗡 𝗦𝗘𝗖𝗢𝗡𝗗𝗦 ➜ "))

# कमेंट भेजने का एनिमेशन
def send_message(access_token, user_id, message):
    url = f"https://graph.facebook.com/v15.0/{user_id}/comments"
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {'message': message}

    animated_text("\n\033[1;33mSending Comment...")
    loading_animation("𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧", 3)

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print(f"\n\033[1;32m𝗖𝗼𝗺𝗺𝗲𝗻𝘁 𝗦𝗲𝗻𝘁 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆 𝗧𝗼 {user_id}: {message}")
        return True
    else:
        print(f"\n\033[1;31m𝗙𝗮𝗶𝗹𝗲𝗱 𝗧𝗼 𝗦𝗲𝗻𝗱 𝗖𝗼𝗺𝗺𝗲𝗻𝘁 𝗧𝗼 {user_id}.")
        return False

# मैसेज भेजने का प्रोसेस
while True:
    for i, access_token in enumerate(access_tokens):
        for user_id, message_file in user_messages.items():
            with open(message_file, 'r') as f:
                messages = f.read().splitlines()
            hater_name = haters_name[user_id]
            message = random.choice(messages)

            send_message(access_token, user_id, hater_name + ' ' + message)
            time.sleep(delay_time)  

    print("\n\033[1;34m𝗔𝗹𝗹 𝗖𝗼𝗺𝗺𝗲𝗻𝘁𝘀 𝗦𝗲𝗻𝘁! 𝗥𝗲𝗽𝗲𝗮𝘁𝗶𝗻𝗴 𝗦𝗼𝗼𝗻...\n")
    time.sleep(5)
