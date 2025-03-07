import os
import sys
import time
import random
import base64
import hashlib
import json
from itertools import cycle
from colorama import Fore, Style

# ✨ लोडिंग एनिमेशन
def loading_animation(text="LOADING", delay=0.2, cycles=3):
    animation = cycle(["|", "/", "-", "\\"])
    for _ in range(cycles):
        sys.stdout.write(f"\r{Fore.GREEN}{text} {next(animation)}{Style.RESET_ALL}")
        sys.stdout.flush()
        time.sleep(delay)
    print("\r", end="")

# 🎭 लोगो एनिमेशन
def print_animated_logo(logo, delay=0.05):
    for char in logo:
        sys.stdout.write(Fore.CYAN + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

# 🔰 लोगो डिजाइन
logo = """
  ______ _           _     _           
 |  ____| |         (_)   | |          
 | |__  | | ___  ___ _  __| | ___ _ __ 
 |  __| | |/ _ \/ __| |/ _` |/ _ \ '__|
 | |____| |  __/\__ \ | (_| |  __/ |   
 |______|_|\___||___/_|\__,_|\___|_|   
                                       
"""

# 🔄 स्क्रिप्ट स्टार्टअप
os.system('clear')
loading_animation("Starting Chat Loader")
print_animated_logo(logo)

# ⏳ समय दिखाएं
print(f"{Fore.YELLOW}START TIME: {time.strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}\n")

# 🔒 पासवर्ड एंटर करने का ऑप्शन
def password_prompt():
    print(f"{Fore.CYAN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>{Style.RESET_ALL}")
    password = input(f"{Fore.GREEN}𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗 ➜ {Style.RESET_ALL}")
    print(f"{Fore.CYAN}<<━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━>>{Style.RESET_ALL}")

    correct_password = "yourpassword123"  # इसे अपने हिसाब से सेट करें
    if password != correct_password:
        print(f"{Fore.RED}𝗜𝗡𝗖𝗢𝗥𝗥𝗘𝗖𝗧 𝗣𝗔𝗦𝗦𝗪𝗢𝗥𝗗!{Style.RESET_ALL}")
        sys.exit()
    else:
        print(f"{Fore.GREEN}𝗔𝗖𝗖𝗘𝗦𝗦 𝗚𝗥𝗔𝗡𝗧𝗘𝗗!{Style.RESET_ALL}")
        time.sleep(1)

password_prompt()

# 📂 इनपुट ऑप्शन 
cookies_file = input(f"{Fore.CYAN}Cookies फाइल नाम ➜ {Style.RESET_ALL}")
uid = input(f"{Fore.CYAN}Encrypted UID ➜ {Style.RESET_ALL}")
header_name = input(f"{Fore.CYAN}हेटर नाम ➜ {Style.RESET_ALL}")
message_file = input(f"{Fore.CYAN}मैसेज फाइल नाम ➜ {Style.RESET_ALL}")
speed_seconds = float(input(f"{Fore.CYAN}स्पीड (सेकंड) ➜ {Style.RESET_ALL}"))

# 🔐 एन्क्रिप्शन और डिक्रिप्शन फंक्शन
def encrypt_message(message, key):
    key = hashlib.sha256(key.encode()).digest()
    encoded = base64.b64encode(message.encode()).decode()
    return encoded

def decrypt_message(encoded, key):
    key = hashlib.sha256(key.encode()).digest()
    decoded = base64.b64decode(encoded).decode()
    return decoded

# 📝 मैसेज लोड करें
try:
    with open(message_file, 'r', encoding='utf-8') as f:
        messages = f.readlines()
except:
    print(f"{Fore.RED}मैसेज फाइल नहीं मिली!{Style.RESET_ALL}")
    sys.exit()

# 🎭 चैट स्टार्ट करें
print(f"{Fore.GREEN}\n🔰 चैट स्टार्ट हो रही है...{Style.RESET_ALL}")
time.sleep(2)

for message in messages:
    message = message.strip()
    if not message:
        continue
    
    encrypted_msg = encrypt_message(message, uid)
    decrypted_msg = decrypt_message(encrypted_msg, uid)

    print(f"\n{Fore.BLUE}📩 सेंडिंग ➜ {header_name}:{Style.RESET_ALL} {encrypted_msg}")
    time.sleep(speed_seconds)
    print(f"{Fore.MAGENTA}📥 रिसीव्ड ➜ {header_name}:{Style.RESET_ALL} {decrypted_msg}")
    time.sleep(speed_seconds)

print(f"\n{Fore.GREEN}✅ चैट समाप्त!{Style.RESET_ALL}")
