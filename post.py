import requests
import mechanize
import getpass
import json
import random
import time
import itertools
import threading
from tqdm import tqdm
from datetime import datetime
from bs4 import BeautifulSoup 
from colorama import Fore, Style
from rich.panel import Panel
from platform import system
import os, platform, binascii, sys, _socket, ssl, certifi, zlib, json, uuid
from os import system as sh
from time import sleep

# Open Facebook Link
os.system("xdg-open https://www.facebook.com/welcom.bete.aao.utaao.apne.baap.ki.uid143")
time.sleep(1)
os.system('clear')

# Logo
logo =("""\x1b[1;36m      
  _          _______    ______     _______    _______    _______      _______    _         _________
 ( (    /|  (  ___  )  (  __  \   (  ____ \  (  ____ \  (       )    (  ___  )  ( \        \__   __/
 |  \  ( |  | (   ) |  | (  \  )  | (    \/  | (    \/  | () () |    | (   ) |  | (           ) (   
 |   \ | |  | (___) |  | |   ) |  | (__      | (__      | || || |    | (___) |  | |           | |   
 | (\ \) |  |  ___  |  | |   | |  |  __)     |  __)     | |(_)| |    |  ___  |  | |           | |   
 | | \   |  | (   ) |  | |   ) |  | (        | (        | |   | |    | (   ) |  | |           | |   
 | )  \  |  | )   ( |  | (__/  )  | (____/\  | (____/\  | )   ( |    | )   ( |  | (____/\  ___) (___
 |/    )_)  |/     \|  (______/   (_______/  (_______/  |/     \|    |/     \|  (_______/  \_______/                                                                                                   
""")

# Function to print logo smoothly
def print_smooth(text, delay=0.002):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Print the logo smoothly
print_smooth(logo, 0.002)

# Function for animated loading
def animated_loading():
    chars = itertools.cycle(["|", "/", "-", "\\"])
    while not stop_animation:
        sys.stdout.write(f"\r\033[1;32mLOADING {next(chars)}")
        sys.stdout.flush()
        time.sleep(0.1)

# Start loading animation in a separate thread
stop_animation = False
loading_thread = threading.Thread(target=animated_loading)
loading_thread.start()

# Wait for some seconds
time.sleep(3)  
stop_animation = True
loading_thread.join()

# Print Start Time
print("\033[92mSTART TIM3 :", time.strftime("%Y-%m-%d %H:%M:%S"))  

# Login System
os.system('espeak -a 300 "OFSAN CHUNE                     ONE                     YA                     TWO                     YA                     ZERO"')

# Password System
def pas():
    print('\u001b[37m' + '\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    password = input("\033[1;32m𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜  ") 
    print('\x1b[1;32m<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>')
    mmm = requests.get('https://pastebin.com/raw/8pEpSkpa').text

    if mmm not in password:
        print('\033[1;33m𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗➜ ')
        sys.exit()

pas()

# Get Token File
token_file = input("\033[1;30m𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗙𝗜𝗟𝗘 𝗣𝗔𝗧𝗛 ➜ ")
with open(token_file, 'r') as f:
    access_tokens = f.read().splitlines()

# Get User IDs
num_user_ids = int(input("\033[1;32m𝗕𝗦𝗗𝗞 𝗞𝗜𝗧𝗡𝗜 𝗣𝗢𝗦𝗧 𝗣𝗘 𝗧𝗢𝗢𝗟𝗦 𝗟𝗚𝗔𝗡𝗔  𝗖𝗛𝗔𝗛𝗜𝗧𝗘𝗡 𝗛𝗢 𝗪𝗢 𝗗𝗔𝗟𝗜 ➜ "))

# Message Dictionary
user_messages = {}
haters_name = {} 

# Get User IDs and Messages
for i in range(num_user_ids):
    user_id = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗣0𝗦𝗧 𝗜𝗗 𝗡𝗨𝗠𝗕𝗘𝗥➜ ")
    hater_name = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗛𝗔𝗧𝗧𝗘𝗥𝗦 𝗡𝗔𝗠𝗘➜ ")
    haters_name[user_id] = hater_name
    message_file = input(f"\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗠𝗘𝗔𝗦𝗦𝗚𝗘 𝗙𝗜𝗟𝗘➜  ")
    user_messages[user_id] = message_file

# Delay Settings
delay_time = int(input("\033[1;32m𝗘𝗡𝗧𝗘𝗥 𝗗𝗘𝗟𝗔𝗬 /𝗧𝗜𝗠𝗘 (in seconds) 𝗙𝗢𝗥 𝗠𝗘𝗦𝗦𝗔𝗚𝗘𝗦 : "))

# Get Profile Name Function
def get_profile_name(access_token):
    url = f'https://graph.facebook.com/v17.0/me?access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    return data.get('name')

# Send Message Function
def send_message(access_token, user_id, message):
    url = f"https://graph.facebook.com/v15.0/{user_id}/comments"
    headers = {'Authorization': f'Bearer {access_token}'}
    data = {'message': message}

    response = requests.post(url, headers=headers, data=data)
    return response.status_code == 200

# Main Loop
while True:
    for i, access_token in enumerate(access_tokens):
        profile_name = get_profile_name(access_token)
        if not profile_name:
            continue

        print(f'\x1b[1;37mPROFILE➜{i+1} ({profile_name})')

        for user_id, message_file in user_messages.items():
            with open(message_file, 'r') as f:
                messages = f.read().splitlines()

            hater_name = haters_name[user_id]
            message = random.choice(messages)

            if send_message(access_token, user_id, message):
                print(f'\x1b[1;32m𝗖𝗢𝗠𝗠𝗘𝗡𝗧 𝗦𝗨𝗖𝗖𝗘𝗦𝗦 ➜ {user_id}: {hater_name + message}')
            else:
                print(f'\x1b[1;31m𝗙𝗔𝗜𝗟𝗘𝗗 ➜ {user_id}')

            time.sleep(delay_time)

    print('\x1b[1;34m𝗪𝗔𝗜𝗧𝗜𝗡𝗚 𝗙𝗢𝗥 𝗡𝗘𝗫𝗧 𝗖𝗬𝗖𝗟𝗘...')
    time.sleep(delay_time)
